#Simple in-memory rate limiter for a single Railway/uvicorn instance.

from __future__ import annotations

import time
from collections import defaultdict, deque
from threading import Lock
from typing import Deque, Dict, Tuple

from fastapi import HTTPException, Request


class RateLimiter:
    def __init__(self) -> None:
        self._hits: Dict[str, Deque[float]] = defaultdict(deque)
        self._lock = Lock()

    def check(self, key: str, limit: int, window_seconds: int = 60) -> None:
        """Raise 429 if `key` exceeded `limit` hits in the last window."""
        now = time.monotonic()
        with self._lock:
            q = self._hits[key]
            cutoff = now - window_seconds
            while q and q[0] < cutoff:
                q.popleft()
            if len(q) >= limit:
                raise HTTPException(
                    status_code=429,
                    detail=(
                        f"Too many requests. Limit is {limit} per {window_seconds}s. "
                        "Please slow down (demo accounts are rate-limited)."
                    ),
                )
            q.append(now)


limiter = RateLimiter()


def client_ip(request: Request) -> str:
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    if request.client:
        return request.client.host or "unknown"
    return "unknown"


def rate_limit(request: Request, *, bucket: str, limit: int, window: int = 60) -> None:
    """Combine IP + bucket name so login and creates have separate budgets."""
    ip = client_ip(request)
    limiter.check(f"{bucket}:{ip}", limit=limit, window_seconds=window)
