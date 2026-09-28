import { useEffect, useLayoutEffect, useRef, useState } from "react";
import { createPortal } from "react-dom";
import { cn } from "../../lib/utils";

/**
 * Dropdown that portals the menu to document.body so it is never clipped by
 * parent overflow / CSS columns (e.g. Notes masonry cards).
 */
export function Dropdown({ trigger, children, align = "right", className }) {
  const [open, setOpen] = useState(false);
  const [coords, setCoords] = useState({ top: 0, left: 0 });
  const triggerRef = useRef(null);
  const menuRef = useRef(null);

  const updatePosition = () => {
    const el = triggerRef.current;
    if (!el) return;
    const rect = el.getBoundingClientRect();
    const menuWidth = 192; // min-w-[12rem]
    let left = align === "right" ? rect.right - menuWidth : rect.left;
    // Keep on screen horizontally
    left = Math.max(8, Math.min(left, window.innerWidth - menuWidth - 8));
    let top = rect.bottom + 8;
    // If near bottom of viewport, open upward
    const estimatedHeight = 160;
    if (top + estimatedHeight > window.innerHeight - 8) {
      top = Math.max(8, rect.top - estimatedHeight - 8);
    }
    setCoords({ top, left });
  };

  useLayoutEffect(() => {
    if (!open) return;
    updatePosition();
    const onScrollOrResize = () => updatePosition();
    window.addEventListener("scroll", onScrollOrResize, true);
    window.addEventListener("resize", onScrollOrResize);
    return () => {
      window.removeEventListener("scroll", onScrollOrResize, true);
      window.removeEventListener("resize", onScrollOrResize);
    };
  }, [open, align]);

  useEffect(() => {
    if (!open) return;
    const onClick = (e) => {
      if (
        triggerRef.current?.contains(e.target) ||
        menuRef.current?.contains(e.target)
      ) {
        return;
      }
      setOpen(false);
    };
    const onKey = (e) => {
      if (e.key === "Escape") setOpen(false);
    };
    document.addEventListener("mousedown", onClick);
    document.addEventListener("keydown", onKey);
    return () => {
      document.removeEventListener("mousedown", onClick);
      document.removeEventListener("keydown", onKey);
    };
  }, [open]);

  return (
    <>
      <div
        ref={triggerRef}
        className="inline-flex"
        onClick={(e) => {
          e.stopPropagation();
          setOpen((o) => !o);
        }}
      >
        {trigger}
      </div>
      {open &&
        createPortal(
          <div
            ref={menuRef}
            style={{ top: coords.top, left: coords.left }}
            className={cn(
              "fixed z-[200] min-w-[12rem] rounded-2xl border border-line bg-surface p-1.5",
              "shadow-[var(--shadow-pop)] animate-fade-up",
              className
            )}
            onClick={() => setOpen(false)}
          >
            {children}
          </div>,
          document.body
        )}
    </>
  );
}

export function DropdownItem({ className, danger, children, ...props }) {
  return (
    <button
      type="button"
      className={cn(
        "flex w-full items-center gap-2.5 rounded-xl px-3 py-2 text-sm text-ink transition hover:bg-surface-muted",
        danger && "text-rose-600 hover:bg-rose-50",
        className
      )}
      {...props}
    >
      {children}
    </button>
  );
}

export function DropdownLabel({ children }) {
  return (
    <p className="px-3 py-1.5 text-xs font-medium text-ink-soft">{children}</p>
  );
}

export function DropdownSeparator() {
  return <div className="my-1 h-px bg-line" />;
}
