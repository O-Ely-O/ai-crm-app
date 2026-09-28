import { AuthBackground } from '../../components/backgrounds/AuthBackground';

export function AuthShell({ children }) {
  return (
    <main className="relative flex min-h-screen w-full items-center justify-center overflow-hidden bg-[#F9F8F4] px-4 py-8 sm:px-6 sm:py-12 lg:px-8">

      {/* =====================================================
          DECORATIVE CRM BACKGROUND
      ====================================================== */}

      <AuthBackground />

      {/* =====================================================
          CENTER CONTENT
      ====================================================== */}

      <div className="relative z-10 flex w-full max-w-md flex-col items-center">
        
        {/* Brand / database identity */}
        <div className="mb-6 flex flex-col items-center sm:mb-7">
          <div className="mt-4 text-center">
            <div className="mt-0.5 text-[10px] font-medium tracking-[0.18em] text-slate-400 uppercase">
              CRM Platform
            </div>
          </div>
        </div>

        {/* ===================================================
            LOGIN CARD
        ==================================================== */}

        <div
          className="
            w-full
            rounded-[28px]
            border
            border-white/90
            bg-white/75
            p-6
            shadow-[0_24px_80px_rgba(15,23,42,0.10)]
            backdrop-blur-2xl
            sm:rounded-[32px]
            sm:p-8
          "
        >
          <div className="animate-fade-up">
            {children}
          </div>
        </div>

        {/* Footer */}

        <p className="mt-6 text-center text-[11px] font-medium tracking-wide text-slate-400">
          © {new Date().getFullYear()} [Your Company Name] All rights reserved.
        </p>
      </div>
    </main>
  );
}