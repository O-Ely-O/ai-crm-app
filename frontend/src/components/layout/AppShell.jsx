import { AppBackground } from "../backgrounds/AppBackground";

export function AppShell({ children }) {
  return (
    <div className="relative min-h-screen">
      <AppBackground />

      <div className="relative">
        {children}
      </div>
    </div>
  );
}