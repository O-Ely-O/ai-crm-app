/* Shared domain constants kept in one place so UI + filters stay in sync
   with the backend enums. */

export const LEAD_STAGES = ["New", "Qualified", "Proposal", "Won", "Lost"];

export const PIPELINE_STAGES = ["New", "Qualified", "Proposal", "Won", "Lost"];

export const LEAD_PRIORITIES = ["Low", "Medium", "High"];

export const LEAD_SOURCES = [
  "Website",
  "Referral",
  "Cold Outreach",
  "Social",
  "Event",
  "Other",
];

export const TASK_STATUSES = ["Pending", "In Progress", "Completed"];
export const TASK_PRIORITIES = ["Low", "Medium", "High"];

/** Tailwind class tokens for each lead stage (badge + kanban accents). */
export const STAGE_STYLES = {
  New: {
    dot: "bg-sky-500",
    badge: "bg-sky-100/80 text-sky-800",
    bar: "bg-sky-500",
    column: "bg-sky-100/50 border-sky-200/70",
    columnActive: "border-sky-400 bg-sky-200/50",
  },

  Qualified: {
    dot: "bg-violet-500",
    badge: "bg-violet-100/80 text-violet-800",
    bar: "bg-violet-500",
    column: "bg-violet-100/50 border-violet-200/70",
    columnActive: "border-violet-400 bg-violet-200/50",
  },

  Proposal: {
    dot: "bg-amber-500",
    badge: "bg-amber-100/80 text-amber-800",
    bar: "bg-amber-500",
    column: "bg-amber-100/50 border-amber-200/70",
    columnActive: "border-amber-400 bg-amber-200/50",
  },

  Won: {
    dot: "bg-brand-500",
    badge: "bg-brand-100/80 text-brand-800",
    bar: "bg-brand-500",
    column: "bg-brand-100/50 border-brand-200/70",
    columnActive: "border-brand-400 bg-brand-200/50",
  },

  Lost: {
    dot: "bg-rose-500",
    badge: "bg-rose-100/80 text-rose-800",
    bar: "bg-rose-500",
    column: "bg-rose-100/50 border-rose-200/70",
    columnActive: "border-rose-400 bg-rose-200/50",
  },
};

export const PRIORITY_STYLES = {
  Low: "bg-slate-100 text-slate-600",
  Medium: "bg-amber-50 text-amber-700",
  High: "bg-rose-50 text-rose-700",
};

export const TASK_STATUS_STYLES = {
  Pending: "bg-slate-100 text-slate-600",
  "In Progress": "bg-sky-50 text-sky-700",
  Completed: "bg-brand-50 text-brand-700",
};
