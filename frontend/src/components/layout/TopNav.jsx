import { NavLink, useNavigate } from "react-router-dom";
import {
  Search,
  Bell,
  Menu,
  ChevronDown,
  User,
  LogOut,
  Sparkles,
} from "lucide-react";
import {
  Avatar,
  IconButton,
  Dropdown,
  DropdownItem,
  DropdownLabel,
  DropdownSeparator,
} from "../ui";
import { useAuth } from "../../context/AuthContext";
import { cn } from "../../lib/utils";

const LINKS = [
  { to: "/", label: "Dashboard", end: true },
  { to: "/leads", label: "Leads" },
  { to: "/pipeline", label: "Pipeline" },
  { to: "/contacts", label: "Contacts" },
  { to: "/tasks", label: "Follow-ups" },
];

export function TopNav({ onMenuClick }) {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  return (
    <header className="relative z-30 flex h-14 items-center gap-3 px-1 md:px-2">
      {/* Brand */}
      <div className="flex shrink-0 items-center gap-2.5 pr-1">
        <div className="brand-gradient flex h-9 w-9 items-center justify-center rounded-xl text-white shadow-sm">
          <Sparkles className="h-5 w-5" />
        </div>

        <span className="hidden font-display text-lg font-bold text-ink sm:block">
          [YOUR CRM]
        </span>
      </div>

      {/* Mobile menu */}
      <button
        onClick={onMenuClick}
        className="rounded-xl p-2 text-ink-soft transition hover:bg-white/70 hover:text-ink lg:hidden"
        aria-label="Open menu"
      >
        <Menu className="h-5 w-5" />
      </button>

      {/* Desktop navigation */}
      <nav className="mx-auto hidden items-center gap-1 rounded-full border border-white/70 bg-white/55 p-1 shadow-sm backdrop-blur-md lg:flex">
        {LINKS.map(({ to, label, end }) => (
          <NavLink
            key={to}
            to={to}
            end={end}
            className={({ isActive }) =>
              cn(
                "rounded-full px-4 py-1.5 text-sm font-medium transition",
                isActive
                  ? "bg-white text-ink shadow-sm"
                  : "text-ink-soft hover:bg-white/60 hover:text-ink"
              )
            }
          >
            {label}
          </NavLink>
        ))}
      </nav>

      {/* Right controls */}
      <div className="ml-auto flex shrink-0 items-center gap-1.5">
        <IconButton
          aria-label="Search"
          className="hidden sm:inline-flex"
        >
          <Search className="h-[18px] w-[18px]" />
        </IconButton>

        <IconButton
          aria-label="Notifications"
          className="relative"
        >
          <Bell className="h-[18px] w-[18px]" />

          <span className="absolute right-2.5 top-2.5 h-2 w-2 rounded-full bg-brand-500 ring-2 ring-white" />
        </IconButton>

        <Dropdown
          trigger={
            <button className="flex items-center gap-2 rounded-full border border-white/80 bg-white/70 py-1 pl-1 pr-2.5 shadow-sm transition hover:bg-white">
              <Avatar
                name={user?.name}
                src={user?.avatar}
                size="sm"
              />

              <ChevronDown className="h-4 w-4 text-ink-soft" />
            </button>
          }
        >
          <DropdownLabel>{user?.email}</DropdownLabel>

          <DropdownSeparator />

          <DropdownItem onClick={() => navigate("/settings")}>
            <User className="h-4 w-4" />
            Profile & settings
          </DropdownItem>

          <DropdownItem danger onClick={logout}>
            <LogOut className="h-4 w-4" />
            Log out
          </DropdownItem>
        </Dropdown>
      </div>
    </header>
  );
}