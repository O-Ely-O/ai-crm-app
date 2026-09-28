export function AppBackground() {
  return (
    <div
      aria-hidden="true"
      className="pointer-events-none fixed inset-0 z-0 overflow-hidden"
    >
      {/* Warm ivory base */}
      <div className="absolute inset-0 bg-[#F9F8F4]" />

      {/* Soft atmospheric glows */}
      <div
        className="absolute -right-40 -top-40 h-[34rem] w-[34rem] rounded-full blur-[140px]"
        style={{
          background:
            "radial-gradient(circle, rgba(34,211,238,0.16) 0%, rgba(56,189,248,0.06) 40%, transparent 72%)",
        }}
      />

      <div
        className="absolute -bottom-48 -left-48 h-[34rem] w-[34rem] rounded-full blur-[140px]"
        style={{
          background:
            "radial-gradient(circle, rgba(59,130,246,0.13) 0%, rgba(56,189,248,0.05) 42%, transparent 72%)",
        }}
      />

      {/* Soft blue dot field */}
      <div
        className="absolute inset-0"
        style={{
          backgroundImage:
            "radial-gradient(circle, rgba(14,165,233,0.32) 1px, transparent 1px)",
          backgroundSize: "20px 20px",
          maskImage:
            "radial-gradient(ellipse 80% 75% at center, black 0%, black 38%, transparent 88%)",
          WebkitMaskImage:
            "radial-gradient(ellipse 80% 75% at center, black 0%, black 38%, transparent 88%)",
        }}
      />

      {/* Secondary ultra-soft dot field */}
      <div
        className="absolute inset-0 opacity-60"
        style={{
          backgroundImage:
            "radial-gradient(circle, rgba(6,182,212,0.22) 0.8px, transparent 0.8px)",
          backgroundSize: "32px 32px",
          backgroundPosition: "10px 8px",
          maskImage:
            "radial-gradient(ellipse 70% 70% at center, black, transparent 82%)",
          WebkitMaskImage:
            "radial-gradient(ellipse 70% 70% at center, black, transparent 82%)",
        }}
      />

      {/* Very subtle overall light falloff */}
      <div
        className="absolute inset-0"
        style={{
          background:
            "radial-gradient(circle at center, transparent 35%, rgba(249,248,244,0.18) 72%, rgba(249,248,244,0.48) 100%)",
        }}
      />
    </div>
  );
}