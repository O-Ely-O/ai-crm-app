-- =============================================================================
-- SME SCALE INDEXES (run AFTER schema.sql in Supabase SQL Editor)
-- Goal: keep list/filter/dashboard fast as you approach millions of rows
-- Safe to re-run: uses IF NOT EXISTS
-- =============================================================================

-- Leads: most common CRM filters
CREATE INDEX IF NOT EXISTS idx_leads_owner_status
  ON public.leads (owner_id, status);

CREATE INDEX IF NOT EXISTS idx_leads_owner_priority
  ON public.leads (owner_id, priority);

CREATE INDEX IF NOT EXISTS idx_leads_owner_order
  ON public.leads (owner_id, "order");

CREATE INDEX IF NOT EXISTS idx_leads_owner_created
  ON public.leads (owner_id, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_leads_owner_updated
  ON public.leads (owner_id, updated_at DESC);

-- Optional: faster ILIKE-style search later (enable extension once)
-- CREATE EXTENSION IF NOT EXISTS pg_trgm;
-- CREATE INDEX IF NOT EXISTS idx_leads_name_trgm ON public.leads USING gin (name gin_trgm_ops);

-- Contacts
CREATE INDEX IF NOT EXISTS idx_contacts_owner_name
  ON public.contacts (owner_id, name);

CREATE INDEX IF NOT EXISTS idx_contacts_owner_favorite
  ON public.contacts (owner_id, favorite DESC, name);

CREATE INDEX IF NOT EXISTS idx_contacts_owner_created
  ON public.contacts (owner_id, created_at DESC);

-- Notes
CREATE INDEX IF NOT EXISTS idx_notes_owner_created
  ON public.notes (owner_id, created_at DESC);

-- Tasks
CREATE INDEX IF NOT EXISTS idx_tasks_owner_status
  ON public.tasks (owner_id, status);

CREATE INDEX IF NOT EXISTS idx_tasks_owner_due
  ON public.tasks (owner_id, due_date);

CREATE INDEX IF NOT EXISTS idx_tasks_owner_created
  ON public.tasks (owner_id, created_at DESC);
