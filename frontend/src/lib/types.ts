export type LeadStatus = "New" | "Qualified" | "Proposal" | "Won" | "Lost";
export type LeadPriority = "Low" | "Medium" | "High";
export type TaskStatus = "Pending" | "In Progress" | "Completed" | "On Hold" | "Cancelled";
export type TaskPriority = "Low" | "Medium" | "High";

export interface User {
  id: string;
  name: string;
  email: string;
  role: string;
  company?: string;
  avatar?: string;
  created_at?: string;
  updated_at?: string;
}

export interface Lead {
  id: string;
  owner_id: string;
  name: string;
  email?: string;
  phone?: string;
  company?: string;
  status: LeadStatus;
  priority: LeadPriority;
  source?: string;
  value: number;
  notes?: string;
  tags?: string[];
  ai_summary?: string;
  ai_risk_score?: number | null;
  order: number;
  created_at?: string;
  updated_at?: string;
}

export interface Contact {
  id: string;
  owner_id: string;
  name: string;
  email?: string;
  phone?: string;
  company?: string;
  title?: string;
  tags?: string[];
  notes?: string;
  favorite: boolean;
  created_at?: string;
  updated_at?: string;
}

export interface Note {
  id: string;
  owner_id: string;
  content: string;
  lead_id?: string | null;
  contact_id?: string | null;
  pinned: boolean;
  created_at?: string;
  updated_at?: string;
  lead?: { id: string; name: string; company?: string } | null;
  contact?: { id: string; name: string; company?: string } | null;
}

export interface Task {
  id: string;
  owner_id: string;
  title: string;
  description?: string;
  due_date?: string | null;
  status: TaskStatus;
  priority: TaskPriority;
  related_lead_id?: string | null;
  related_contact_id?: string | null;
  completed_at?: string | null;
  created_at?: string;
  updated_at?: string;
  related_lead?: { id: string; name: string; company?: string } | null;
  related_contact?: { id: string; name: string; company?: string } | null;
}

export interface AuthResponse {
  success: boolean;
  token: string;
  user: User;
}

export interface DashboardStats {
  revenueWon: number;
  pipelineValue: number;
  totalLeads: number;
  totalContacts: number;
  openTasks: number;
  conversionRate: number;
}