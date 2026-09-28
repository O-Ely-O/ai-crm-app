-- =============================================================================
-- DEMO SEED DATA (from original mockData.js) — makes Dashboard look lively
-- =============================================================================
-- HOW TO USE:
-- 1. Register / log in once in the CRM app (creates your row in auth.users + profiles)
-- 2. Supabase → SQL Editor → run this query to get your user id:
--
--      SELECT id, email FROM auth.users;
--
-- 3. Replace EVERY occurrence of 00000000-0000-4000-8000-000000000001 below
--    with your real UUID (use Find & Replace in the SQL editor).
-- 4. Run this whole script.
-- 5. Refresh the CRM Dashboard.
-- =============================================================================

-- Optional: wipe previous demo rows for this owner (safe if you only use demo data)
-- DELETE FROM public.tasks  WHERE owner_id = '00000000-0000-4000-8000-000000000001';
-- DELETE FROM public.notes  WHERE owner_id = '00000000-0000-4000-8000-000000000001';
-- DELETE FROM public.leads  WHERE owner_id = '00000000-0000-4000-8000-000000000001';
-- DELETE FROM public.contacts WHERE owner_id = '00000000-0000-4000-8000-000000000001';

-- Fixed UUIDs for demo entities (stable across re-runs if you delete first)
-- Leads
INSERT INTO public.leads (id, owner_id, name, email, company, status, priority, source, value, notes, tags, "order", created_at, updated_at)
VALUES
  ('11111111-1111-4111-8111-111111111101', '90be2c88-ce99-439b-8808-82858aca04f1', 'Dribbble Design', 'dribbbledesign@example.com', 'Acme Corp', 'New', 'High', 'Website', 89345, 'Inbound inbound from website form.', ARRAY['design','inbound'], 0, NOW() - INTERVAL '8 days', NOW() - INTERVAL '1 day'),
  ('11111111-1111-4111-8111-111111111102', '90be2c88-ce99-439b-8808-82858aca04f1', 'Google Pay', 'googlepay@example.com', 'Globex', 'Qualified', 'High', 'Referral', 124000, 'Warm referral from partner.', ARRAY['fintech'], 1, NOW() - INTERVAL '20 days', NOW() - INTERVAL '2 days'),
  ('11111111-1111-4111-8111-111111111103', '90be2c88-ce99-439b-8808-82858aca04f1', 'Amazon Shopping', 'amazon@example.com', 'Initech', 'Proposal', 'Medium', 'Cold Outreach', 32123, 'Sent proposal last week.', ARRAY['retail'], 2, NOW() - INTERVAL '35 days', NOW() - INTERVAL '3 days'),
  ('11111111-1111-4111-8111-111111111104', '90be2c88-ce99-439b-8808-82858aca04f1', 'Stripe', 'stripe@example.com', 'Umbrella Co', 'Won', 'High', 'Event', 76500, 'Closed at conference follow-up.', ARRAY['payments','won'], 3, NOW() - INTERVAL '60 days', NOW() - INTERVAL '5 days'),
  ('11111111-1111-4111-8111-111111111105', '90be2c88-ce99-439b-8808-82858aca04f1', 'Notion', 'notion@example.com', 'Soylent', 'New', 'Low', 'Social Media', 12400, 'Saw us on LinkedIn.', ARRAY['saas'], 4, NOW() - INTERVAL '4 days', NOW()),
  ('11111111-1111-4111-8111-111111111106', '90be2c88-ce99-439b-8808-82858aca04f1', 'Figma', 'figma@example.com', 'Hooli', 'Qualified', 'Medium', 'Website', 54000, 'Design team evaluating tools.', ARRAY['design'], 5, NOW() - INTERVAL '14 days', NOW() - INTERVAL '1 day'),
  ('11111111-1111-4111-8111-111111111107', '90be2c88-ce99-439b-8808-82858aca04f1', 'Linear', 'linear@example.com', 'Pied Piper', 'Proposal', 'High', 'Referral', 98000, 'Strong champion in eng.', ARRAY['devtool'], 6, NOW() - INTERVAL '28 days', NOW() - INTERVAL '2 days'),
  ('11111111-1111-4111-8111-111111111108', '90be2c88-ce99-439b-8808-82858aca04f1', 'Slack', 'slack@example.com', 'Vehement', 'Lost', 'Low', 'Cold Outreach', 21000, 'Chose competitor.', ARRAY['lost'], 7, NOW() - INTERVAL '95 days', NOW() - INTERVAL '30 days'),
  ('11111111-1111-4111-8111-111111111109', '90be2c88-ce99-439b-8808-82858aca04f1', 'Vercel', 'vercel@example.com', 'Massive Dynamic', 'Won', 'High', 'Referral', 143000, 'Enterprise annual.', ARRAY['won','infra'], 8, NOW() - INTERVAL '110 days', NOW() - INTERVAL '40 days'),
  ('11111111-1111-4111-8111-111111111110', '90be2c88-ce99-439b-8808-82858aca04f1', 'Airtable', 'airtable@example.com', 'Wayne Ent.', 'Qualified', 'High', 'Event', 67000, 'Met at meetup.', ARRAY['ops'], 9, NOW() - INTERVAL '18 days', NOW() - INTERVAL '1 day'),
  ('11111111-1111-4111-8111-111111111111', '90be2c88-ce99-439b-8808-82858aca04f1', 'Datadog', 'datadog@example.com', 'Stark Industries', 'New', 'Medium', 'Website', 45000, 'Ops lead downloaded whitepaper.', ARRAY['observability'], 10, NOW() - INTERVAL '2 days', NOW()),
  ('11111111-1111-4111-8111-111111111112', '90be2c88-ce99-439b-8808-82858aca04f1', 'Snowflake', 'snowflake@example.com', 'Cyberdyne', 'Proposal', 'High', 'Referral', 152000, 'Data platform evaluation.', ARRAY['data'], 11, NOW() - INTERVAL '48 days', NOW() - INTERVAL '4 days'),
  ('11111111-1111-4111-8111-111111111113', '90be2c88-ce99-439b-8808-82858aca04f1', 'HubSpot', 'hubspot@example.com', 'Tyrell Corp', 'Won', 'Medium', 'Event', 88000, 'Marketing suite deal.', ARRAY['won'], 12, NOW() - INTERVAL '150 days', NOW() - INTERVAL '60 days'),
  ('11111111-1111-4111-8111-111111111114', '90be2c88-ce99-439b-8808-82858aca04f1', 'Asana', 'asana@example.com', 'Aperture Labs', 'Qualified', 'Low', 'Social Media', 30000, 'PM team trial.', ARRAY['productivity'], 13, NOW() - INTERVAL '22 days', NOW() - INTERVAL '3 days'),
  ('11111111-1111-4111-8111-111111111115', '90be2c88-ce99-439b-8808-82858aca04f1', 'Zoom', 'zoom@example.com', 'Oscorp', 'New', 'Medium', 'Cold Outreach', 26000, 'First touch this week.', ARRAY['comms'], 14, NOW() - INTERVAL '6 days', NOW()),
  ('11111111-1111-4111-8111-111111111116', '90be2c88-ce99-439b-8808-82858aca04f1', 'GitLab', 'gitlab@example.com', 'LexCorp', 'Lost', 'Low', 'Website', 18000, 'Budget frozen.', ARRAY['lost'], 15, NOW() - INTERVAL '70 days', NOW() - INTERVAL '20 days')
ON CONFLICT (id) DO NOTHING;

-- Contacts
INSERT INTO public.contacts (id, owner_id, name, email, phone, company, title, tags, notes, favorite, created_at, updated_at)
VALUES
  ('22222222-2222-4222-8222-222222222201', '90be2c88-ce99-439b-8808-82858aca04f1', 'Jordan Lee', 'jordan@acme.com', '+1 555-0101', 'Acme Corp', 'VP Product', ARRAY['champion'], 'Prefers async updates.', true, NOW() - INTERVAL '30 days', NOW()),
  ('22222222-2222-4222-8222-222222222202', '90be2c88-ce99-439b-8808-82858aca04f1', 'Sam Rivera', 'sam@globex.io', '+1 555-0102', 'Globex', 'CTO', ARRAY['decision-maker'], 'Ask about Q3 roadmap.', true, NOW() - INTERVAL '45 days', NOW()),
  ('22222222-2222-4222-8222-222222222203', '90be2c88-ce99-439b-8808-82858aca04f1', 'Casey Kim', 'casey@initech.com', '+1 555-0103', 'Initech', 'Procurement', ARRAY['blocker'], 'Needs security questionnaire.', false, NOW() - INTERVAL '20 days', NOW()),
  ('22222222-2222-4222-8222-222222222204', '90be2c88-ce99-439b-8808-82858aca04f1', 'Riley Chen', 'riley@umbrella.co', '+1 555-0104', 'Umbrella Co', 'Head of Sales Ops', ARRAY['champion'], 'Closed Stripe deal.', true, NOW() - INTERVAL '80 days', NOW()),
  ('22222222-2222-4222-8222-222222222205', '90be2c88-ce99-439b-8808-82858aca04f1', 'Morgan Blake', 'morgan@soylent.com', '+1 555-0105', 'Soylent', 'Marketing Lead', ARRAY['inbound'], 'Active on LinkedIn.', false, NOW() - INTERVAL '10 days', NOW()),
  ('22222222-2222-4222-8222-222222222206', '90be2c88-ce99-439b-8808-82858aca04f1', 'Avery Quinn', 'avery@hooli.com', '+1 555-0106', 'Hooli', 'Design Director', ARRAY['champion'], 'Loves Figma workflows.', true, NOW() - INTERVAL '25 days', NOW()),
  ('22222222-2222-4222-8222-222222222207', '90be2c88-ce99-439b-8808-82858aca04f1', 'Jamie Park', 'jamie@piedpiper.com', '+1 555-0107', 'Pied Piper', 'Eng Manager', ARRAY['technical'], 'Wants SOC2 docs.', false, NOW() - INTERVAL '15 days', NOW()),
  ('22222222-2222-4222-8222-222222222208', '90be2c88-ce99-439b-8808-82858aca04f1', 'Taylor Brooks', 'taylor@wayne.com', '+1 555-0108', 'Wayne Ent.', 'COO', ARRAY['executive'], 'Event follow-up.', true, NOW() - INTERVAL '12 days', NOW())
ON CONFLICT (id) DO NOTHING;

-- Notes
INSERT INTO public.notes (id, owner_id, content, lead_id, contact_id, pinned, created_at, updated_at)
VALUES
  ('33333333-3333-4333-8333-333333333301', '90be2c88-ce99-439b-8808-82858aca04f1', 'Discovery call went well. Budget confirmed for Q4. Next step: send case study.', '11111111-1111-4111-8111-111111111102', NULL, true, NOW() - INTERVAL '5 days', NOW()),
  ('33333333-3333-4333-8333-333333333302', '90be2c88-ce99-439b-8808-82858aca04f1', 'Legal is reviewing MSA. Follow up Friday if no reply.', '11111111-1111-4111-8111-111111111107', NULL, false, NOW() - INTERVAL '2 days', NOW()),
  ('33333333-3333-4333-8333-333333333303', '90be2c88-ce99-439b-8808-82858aca04f1', 'Competitor pricing came up — prepare value comparison one-pager.', '11111111-1111-4111-8111-111111111103', NULL, true, NOW() - INTERVAL '7 days', NOW()),
  ('33333333-3333-4333-8333-333333333304', '90be2c88-ce99-439b-8808-82858aca04f1', 'Introduced to procurement. Need security questionnaire completed.', NULL, '22222222-2222-4222-8222-222222222203', false, NOW() - INTERVAL '3 days', NOW()),
  ('33333333-3333-4333-8333-333333333305', '90be2c88-ce99-439b-8808-82858aca04f1', 'Closed won dinner notes: expand to second business unit next year.', '11111111-1111-4111-8111-111111111104', NULL, false, NOW() - INTERVAL '40 days', NOW()),
  ('33333333-3333-4333-8333-333333333306', '90be2c88-ce99-439b-8808-82858aca04f1', 'LinkedIn inbound — schedule 20-min intro call.', '11111111-1111-4111-8111-111111111105', NULL, false, NOW() - INTERVAL '1 day', NOW())
ON CONFLICT (id) DO NOTHING;

-- Tasks
INSERT INTO public.tasks (id, owner_id, title, description, due_date, status, priority, related_lead_id, related_contact_id, completed_at, created_at, updated_at)
VALUES
  ('44444444-4444-4444-8444-444444444401', '90be2c88-ce99-439b-8808-82858aca04f1', 'Send proposal to Globex', 'Include pricing tiers A/B', NOW() + INTERVAL '2 days', 'In Progress', 'High', '11111111-1111-4111-8111-111111111102', NULL, NULL, NOW() - INTERVAL '3 days', NOW()),
  ('44444444-4444-4444-8444-444444444402', '90be2c88-ce99-439b-8808-82858aca04f1', 'Follow up on MSA with Linear', '', NOW() - INTERVAL '1 day', 'Pending', 'High', '11111111-1111-4111-8111-111111111107', NULL, NULL, NOW() - INTERVAL '5 days', NOW()),
  ('44444444-4444-4444-8444-444444444403', '90be2c88-ce99-439b-8808-82858aca04f1', 'Prepare security questionnaire', 'For Initech procurement', NOW() + INTERVAL '5 days', 'Pending', 'Medium', '11111111-1111-4111-8111-111111111103', NULL, NULL, NOW() - INTERVAL '2 days', NOW()),
  ('44444444-4444-4444-8444-444444444404', '90be2c88-ce99-439b-8808-82858aca04f1', 'Schedule QBR with Umbrella', 'Post-sale expansion', NOW() + INTERVAL '14 days', 'Pending', 'Low', '11111111-1111-4111-8111-111111111104', NULL, NULL, NOW() - INTERVAL '1 day', NOW()),
  ('44444444-4444-4444-8444-444444444405', '90be2c88-ce99-439b-8808-82858aca04f1', 'Demo for Acme design team', '', NOW() + INTERVAL '3 days', 'Pending', 'High', '11111111-1111-4111-8111-111111111101', NULL, NULL, NOW() - INTERVAL '1 day', NOW()),
  ('44444444-4444-4444-8444-444444444406', '90be2c88-ce99-439b-8808-82858aca04f1', 'Send case study PDF', '', NOW() - INTERVAL '3 days', 'Completed', 'Medium', '11111111-1111-4111-8111-111111111109', NULL, NOW() - INTERVAL '2 days', NOW() - INTERVAL '10 days', NOW()),
  ('44444444-4444-4444-8444-444444444407', '90be2c88-ce99-439b-8808-82858aca04f1', 'Book discovery call with Oscorp', '', NOW() + INTERVAL '5 days', 'Pending', 'Low', '11111111-1111-4111-8111-111111111115', NULL, NULL, NOW() - INTERVAL '2 days', NOW()),
  ('44444444-4444-4444-8444-444444444408', '90be2c88-ce99-439b-8808-82858aca04f1', 'Re-engage stalled deal at Soylent', '', NOW() + INTERVAL '14 days', 'Pending', 'Low', '11111111-1111-4111-8111-111111111105', NULL, NULL, NOW() - INTERVAL '4 days', NOW()),
  ('44444444-4444-4444-8444-444444444409', '90be2c88-ce99-439b-8808-82858aca04f1', 'Update pipeline forecast for manager', 'Weekly ritual', NOW(), 'In Progress', 'Medium', NULL, NULL, NULL, NOW() - INTERVAL '1 day', NOW()),
  ('44444444-4444-4444-8444-444444444410', '90be2c88-ce99-439b-8808-82858aca04f1', 'Send security docs to Cyberdyne', '', NOW() - INTERVAL '8 days', 'Completed', 'Medium', '11111111-1111-4111-8111-111111111112', NULL, NOW() - INTERVAL '7 days', NOW() - INTERVAL '12 days', NOW())
ON CONFLICT (id) DO NOTHING;
