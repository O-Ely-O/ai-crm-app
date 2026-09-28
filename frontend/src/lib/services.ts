import api from "./api";
import type {
  AuthResponse,
  User,
  Lead,
  Contact,
  Note,
  Task,
} from "./types";

/** Map API id → frontend _id + camelCase dates for UI compatibility */
function withId<T extends { id: string }>(row: T): T & { _id: string } {
  const r = row as T & Record<string, unknown>;
  return {
    ...row,
    _id: row.id,
    // Lead/table UIs expect camelCase timestamps
    createdAt: r.createdAt ?? r.created_at,
    updatedAt: r.updatedAt ?? r.updated_at,
    dueDate: r.dueDate ?? r.due_date,
  } as T & { _id: string };
}

export type ListParams = Record<string, string | number | undefined>;

/* ── Auth ──────────────────────────────────────────────────────────── */
export const authApi = {
  register: (data: {
    name: string;
    email: string;
    password: string;
    company?: string;
  }) => api.post<AuthResponse>("/auth/register", data).then((r) => r.data),

  login: (data: { email: string; password: string }) =>
    api.post<AuthResponse>("/auth/login", data).then((r) => r.data),

  me: () =>
    api.get<{ success: boolean; user: User }>("/auth/me").then((r) => r.data),

  updateProfile: (data: Partial<User> & { password?: string }) =>
    api
      .put<{ success: boolean; user: User }>("/auth/profile", data)
      .then((r) => r.data),
};

/* ── Leads (paginated: pass page & limit) ──────────────────────────── */
export const leadsApi = {
  list: (params?: ListParams) =>
    api
      .get<{
        success: boolean;
        leads: Lead[];
        page?: { page: number; limit: number; total: number; has_more: boolean };
      }>("/leads", { params })
      .then((r) => ({
        ...r.data,
        leads: (r.data.leads || []).map(withId),
      })),

  get: (id: string) =>
    api
      .get<{ success: boolean; lead: Lead }>(`/leads/${id}`)
      .then((r) => ({ ...r.data, lead: withId(r.data.lead) })),

  create: (data: Partial<Lead>) =>
    api
      .post<{ success: boolean; lead: Lead }>("/leads", data)
      .then((r) => ({ ...r.data, lead: withId(r.data.lead) })),

  update: (id: string, data: Partial<Lead>) =>
    api
      .put<{ success: boolean; lead: Lead }>(`/leads/${id}`, data)
      .then((r) => ({ ...r.data, lead: withId(r.data.lead) })),

  remove: (id: string) =>
    api
      .delete<{ success: boolean; message: string }>(`/leads/${id}`)
      .then((r) => r.data),

  reorder: (updates: { id: string; status: string; order: number }[]) =>
    api
      .patch<{ success: boolean; message: string }>("/leads/reorder", {
        updates,
      })
      .then((r) => r.data),
};

/* ── Contacts ──────────────────────────────────────────────────────── */
export const contactsApi = {
  list: (params?: ListParams) =>
    api
      .get<{
        success: boolean;
        count: number;
        contacts: Contact[];
        page?: { page: number; limit: number; total: number; has_more: boolean };
      }>("/contacts", { params })
      .then((r) => ({
        ...r.data,
        contacts: (r.data.contacts || []).map(withId),
      })),

  get: (id: string) =>
    api
      .get<{ success: boolean; contact: Contact }>(`/contacts/${id}`)
      .then((r) => ({ ...r.data, contact: withId(r.data.contact) })),

  create: (data: Partial<Contact>) =>
    api
      .post<{ success: boolean; contact: Contact }>("/contacts", data)
      .then((r) => ({ ...r.data, contact: withId(r.data.contact) })),

  update: (id: string, data: Partial<Contact>) =>
    api
      .put<{ success: boolean; contact: Contact }>(`/contacts/${id}`, data)
      .then((r) => ({ ...r.data, contact: withId(r.data.contact) })),

  remove: (id: string) =>
    api
      .delete<{ success: boolean; message: string }>(`/contacts/${id}`)
      .then((r) => r.data),
};

/* ── Notes ─────────────────────────────────────────────────────────── */
export const notesApi = {
  list: (params?: ListParams) =>
    api
      .get<{
        success: boolean;
        count: number;
        notes: Note[];
        page?: { page: number; limit: number; total: number; has_more: boolean };
      }>("/notes", { params })
      .then((r) => ({
        ...r.data,
        notes: (r.data.notes || []).map(withId),
      })),

  create: (data: Partial<Note>) =>
    api
      .post<{ success: boolean; note: Note }>("/notes", data)
      .then((r) => ({ ...r.data, note: withId(r.data.note) })),

  update: (id: string, data: Partial<Note>) =>
    api
      .put<{ success: boolean; note: Note }>(`/notes/${id}`, data)
      .then((r) => ({ ...r.data, note: withId(r.data.note) })),

  remove: (id: string) =>
    api
      .delete<{ success: boolean; message: string }>(`/notes/${id}`)
      .then((r) => r.data),
};

/* ── Tasks ─────────────────────────────────────────────────────────── */
export const tasksApi = {
  list: (params?: ListParams) =>
    api
      .get<{
        success: boolean;
        count: number;
        tasks: Task[];
        page?: { page: number; limit: number; total: number; has_more: boolean };
      }>("/tasks", { params })
      .then((r) => ({
        ...r.data,
        tasks: (r.data.tasks || []).map(withId),
      })),

  create: (data: Partial<Task>) =>
    api
      .post<{ success: boolean; task: Task }>("/tasks", data)
      .then((r) => ({ ...r.data, task: withId(r.data.task) })),

  update: (id: string, data: Partial<Task>) =>
    api
      .put<{ success: boolean; task: Task }>(`/tasks/${id}`, data)
      .then((r) => ({ ...r.data, task: withId(r.data.task) })),

  remove: (id: string) =>
    api
      .delete<{ success: boolean; message: string }>(`/tasks/${id}`)
      .then((r) => r.data),
};

/* ── Analytics ─────────────────────────────────────────────────────── */
export const analyticsApi = {
  dashboard: () => api.get("/analytics/dashboard").then((r) => r.data),
  /** Alias used by Dashboard.jsx (same endpoint) */
  overview: () => api.get("/analytics/dashboard").then((r) => r.data),
};

/* ── AI ────────────────────────────────────────────────────────────── */
export const aiApi = {
  status: () => api.get("/ai/status").then((r) => r.data),
  leadSummary: (payload: { lead_id?: string; lead?: Partial<Lead> }) =>
    api.post("/ai/lead-summary", payload).then((r) => r.data),
  email: (payload: {
    lead_id?: string;
    lead?: Partial<Lead>;
    purpose?: string;
    tone?: string;
  }) => api.post("/ai/email", payload).then((r) => r.data),
  insights: (payload?: { pipeline_stats?: unknown }) =>
    api.post("/ai/insights", payload || {}).then((r) => r.data),
};