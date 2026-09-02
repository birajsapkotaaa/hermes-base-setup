# Company Intelligence & Scraping Skill

## Description
Allows the agent to programmatically pull and parse raw text data from company websites, landing pages, and public profile links provided by users to check them against an ICP. The purpose is to act as a Lead Generation & Research Assistant.

## Target ICP Criteria
- **Target Industry:** Real estate and property management companies.
- **Target Size:** 11–200 employees (Accept smaller teams only if they demonstrate high lead/request volume).
- **Target Roles:** Broker Owner, Team Lead, Property Manager, Leasing Manager, Operations Manager, Transaction Coordinator, Office Manager.
- **Relevant Keywords/Workflows:** Property management, real estate brokerage, leasing, tenant requests, maintenance requests, property inquiries, lead follow-up, document collection, showing coordination, transaction coordination, admin support, CRM updates.

## Decision Logic
- **Perfect Fit:** Real estate broker/operator role + defined repeated weekly workflow + high volume + manual admin/follow-up/document-heavy tasks.
- **Dealbreakers (Disqualifiers):**
    - No clear repeated workflow pain (vague "AI curiosity" only).
    - Requesting AI to perform risky autonomous decisions (e.g., approvals, legal decisions, financial transactions, tenant selection, or contract execution) without human review.


## Usage
- Triggered whenever a URL is passed to the input layer.
- Tool Call: `scrape_lead_context(url="<target_url>")`
