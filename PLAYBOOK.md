# 100hires AI-Powered SEO Playbook
## Programmatic Content Production for B2B SaaS ATS Platforms

---

> **How to use this document:** This playbook is designed to be read all the way through once, then returned to by section as needed. The logic is consistent throughout — every recommendation carries its operating condition with it. You can open any section and follow the reasoning without losing the thread.

---

## The Context: Operational Baseline & Constraints

**This playbook is not a universal SEO guide. It is an architectural blueprint for a specific business at a specific stage.**

**The Target Buyer — The "Frankenstein-Stack" Operator:**
We are not targeting HR generalists searching for "best ATS software." We are targeting the tech-savvy HR Director or startup founder who has already validated their problem — they are currently managing hiring across ChatGPT, Zapier, Calendly, and a legacy ATS, and the maintenance cost of that stack is becoming their actual job. They are not searching for "more AI." They are searching for consolidation. They are searching for integration fixes. They are searching for escape.

This matters for every decision in this playbook. The buyer we are building for has already done the hard work of proving the problem is real. That changes what we build, where we build it, and why it converts.

**When this playbook applies:**
- The domain has sufficient baseline authority to support deep programmatic page indexation
- Engineering or technical marketing resources exist to support API extraction or template automation
- The team can support a human-in-the-loop review workflow before publishing at scale

**When this playbook is a reference document, not a mandate:**
- Domain Rating is too low to index deep programmatic pages
- No developer bandwidth exists for API integration
- Publishing infrastructure is not yet in place

If you do not meet the operational prerequisites above, enter at Lane B of the Execution SOP and use this document as a planning reference until capacity exists.

---

## Execution SOP: The Programmatic SEO Decision Tree

**The origin of these workflows:** These operational lanes were engineered by observing the inherent friction between the selected sources — specifically the divide between technical scalability (King, Nath), manual semantic theory (Gübür), and conversion urgency (Schwartz, DiNardi). Rather than treating their conflicting advice as absolute rules, the bottlenecks their strategies were addressing were isolated to create workflows based on actual operational capacity.

**The meta-assumption visible throughout this document:** All three lanes converge at the same bottleneck regardless of entry point. The lane you enter is determined by your resources. The convergence point — E-E-A-T verification and crawl management — is non-negotiable regardless of lane. This is not a rigid system. Pivots between lanes are expected and accounted for.

---

### LANE A: The Engineering-Led Start
*Use this lane if: You have developer bandwidth and access to structured HR or hiring data via APIs.*

**Node A1: API Entity Extraction**
Extract structured entity data — average salaries, required skills, compliance requirements, regional labor law references — for specific job titles from market APIs.
*(source: Mike King, [AI Search Manual Presentation](https://www.youtube.com/watch?v=ukpU-EfRtV4), April 2026)*

*Weakness embedded here: This node assumes the API data is clean and complete. In practice, labor market APIs vary significantly in data quality by region and role type. Validate a sample before scaling.*

- **IF** the returned data is complete and structured → Move to Node A2
- **IF** the data is messy or thin → PIVOT to Lane B, Node B1 to manually map semantic gaps before proceeding

**Node A2: Programmatic Template Structuring**
Feed clean API data into rigid JSON or Markdown templates. Titles are not AI-generated — use deterministic templates like "Customer Success Manager Job Description — SaaS Industry, Remote." AI fills the structured variables. The template controls the architecture.
*(source: Preetam Nath, [Programmatic SEO Course](https://preetamnath.com), 2026)*
*(source: Jake Ward, [Programmatic SEO 2.0](https://www.linkedin.com/in/jakeaward/), March 2026)*

→ Route to the Convergence Hub

---

### LANE B: The Marketing-Led Start
*Use this lane if: You have existing content or manual research capacity but no developer resources yet.*

**Node B1: Semantic Mapping & Entity Association**
Before writing anything, map the topical authority network for a single micro-niche — for example, "Healthcare Recruiting" or "Remote Engineering Hiring." Identify the specific entities and attributes a search engine expects to see: role types, required certifications, salary bands, compliance requirements, tools.
*(source: Koray Tuğberk GÜBÜR, [Holistic SEO & Topical Authority](https://www.youtube.com/watch?v=PCNnLSCjSMc), 2026)*

*Weakness embedded here: This is the slowest lane. Manual semantic mapping is thorough but creates an operational bottleneck at editorial capacity. Do not attempt to cover more than one micro-niche at a time before validating indexation.*

- **IF** a complete topical map exists for the cluster → Move to Node B2
- **IF** the map is incomplete → Continue mapping. Do not generate content yet. Thin content in a YMYL category compounds technical debt faster than it generates traffic.
- **Pivot opportunity:** If engineering resources open up mid-process → PIVOT to Lane A, Node A1 to automate template population from the completed semantic map

**Node B2: Manual Template Structuring**
Build page templates by hand based on the completed semantic map. Every entity identified in B1 should have a corresponding field in the template.

→ Route to the Convergence Hub

---

### LANE C: The Sales-Led Start
*Use this lane if: You need pipeline immediately and cannot wait for topical authority to compound.*

**Node C1: BOFU Intent Mapping**
Map strictly Bottom-of-Funnel search queries — not "what is an ATS" but "ATS for nurse staffing agencies," "Workable alternatives for startups under 50 employees," "how to automate interview scheduling without Calendly."
*(source: Gaetano DiNardi, [Does AI Traffic Convert Better Than Google?](https://substack.com/@gaetanodinardi), November 2025)*

*Weakness embedded here: This lane produces the fastest pipeline but the narrowest topical footprint. It does not build domain authority over time. Treat Lane C as a bridge, not a destination.*

- **IF** internal product data exists to prove superiority for this query → Move to Node C2
- **IF** no product differentiation data exists for this query → PIVOT to Lane B, Node B1 to build broader relevance first

**Node C2: Product-Led Asset Creation**
Build the landing page around product utility, not informational text. Anonymized hiring data, interactive templates, workflow comparisons. The page should do something, not just say something.
*(source: Eli Schwartz, [AEO is Not SEO 2.0](https://elischw.substack.com), April 2026)*

→ Route to the Convergence Hub

---

### THE CONVERGENCE HUB: Publishing & Protection
*All content from all lanes passes through here before going live. This is non-negotiable regardless of entry point.*

**Node D1: E-E-A-T Injection**
Apply human-in-the-loop review. For every page: inject real author citations, link to verified compliance sources and labor laws, ensure YMYL safety standards are met. Ask: does this page feel like a verified resource or a database dump?
*(source: Lily Ray, [25 Years of SEO History, Brighton SEO](https://www.youtube.com/watch?v=nw-dllribgQ), 2025)*

- **IF** the page reads like a database dump → Return to the originating lane for enrichment
- **IF** the page reads as a verified resource → Move to Node D2

**Node D2: Automated Crawl Management**
Deploy pages and immediately activate server log monitoring. Check for canonicalization issues, crawl waste, and low-value pagination trapping Googlebot. Schedule a 90-day audit of all programmatic clusters to verify API data accuracy and refresh stale salary or compliance information.
*(source: Aleyda Solis, [Crawling Mondays — SEO Automation](https://www.youtube.com/watch?v=fxa8DAo8hgg), 2021)*

- **IF** Googlebot is trapped in low-value loops → Adjust robots.txt and internal linking parameters immediately
- **IF** crawl architecture is clean → Pipeline is stable. Scale generation.

---

## Section: Where Experts Disagree

### Conflict 1: Content Velocity vs. Algorithmic Risk

**What Preetam Nath recommends:** Build massive programmatic matrices at high velocity. Capture long-tail intent through volume and rapid iteration.
*(source: Preetam Nath, [Programmatic SEO Course](https://preetamnath.com), 2026)*

**What Lily Ray recommends:** Implement strict human-in-the-loop review and robust E-E-A-T signals before publishing at scale. Unchecked programmatic velocity in YMYL categories triggers core update penalties.
*(source: Lily Ray, [Brighton SEO Keynote](https://www.youtube.com/watch?v=nw-dllribgQ), 2025)*

**Which side I take and why:** A hybrid approach weighted heavily toward Ray. Nath's matrix logic designs the architecture. Ray's verification protocols gate the publishing velocity. For an ATS platform operating in hiring and salary data — both YMYL categories — unverified programmatic pages create technical debt faster than they create traffic. The convergence hub in this playbook is the direct structural response to this conflict.

**The context of the disagreement:** Nath is optimizing for aggressive early-stage growth on domains where a penalty is survivable. Ray is advising brands where a manual action would damage the core lead generation engine. The disagreement is not about SEO — it is about risk tolerance relative to business stage.

---

### Conflict 2: Keyword Modifiers vs. Product-Led Utility

**What Jake Ward recommends:** Target repeatable keyword modifiers — "vs," "alternatives," "templates" — using LLMs to generate derivative pages at scale capturing existing search volume.
*(source: Jake Ward, [Programmatic SEO 2.0](https://www.linkedin.com/in/jakeaward/), March 2026)*

**What Eli Schwartz recommends:** Stop chasing keywords entirely. Build SEO into the product's utility. Surface internal data as interactive tools that an AI Overview cannot summarize or replace.
*(source: Eli Schwartz, [AEO is Not SEO 2.0](https://elischw.substack.com), April 2026)*

**Which side I take and why:** Schwartz, for this specific use case and stage. Top-of-funnel keyword pages are being cannibalized by AI Overviews at an accelerating rate. An ATS competing on blog posts is competing on a surface that is structurally shrinking. Surfacing anonymized hiring data as interactive tools creates a defensible moat that keyword volume cannot replicate. Ward's approach becomes relevant again at scale, for competitive comparison pages built on real product data — not as the primary strategy.

**Pivot Point:** When domain authority baseline is established and Lane A is producing indexed, ranking pages, Ward's keyword modifier matrix becomes a viable extension of the programmatic architecture — not the foundation.

**The context of the disagreement:** Ward's frameworks were built for affiliate marketing and traffic arbitrage where volume is the metric. Schwartz is advising mature SaaS companies where the product itself is the SEO engine. They are not contradicting each other — they are speaking to different business models entirely.

---

### Conflict 3: Semantic Theory vs. API Data Extraction

**What Koray Tuğberk GÜBÜR recommends:** Manually define and map exhaustive topical authority semantic networks before generating any content. Entity-attribute relationships must be explicitly planned to avoid thin content classification.
*(source: Koray Tuğberk GÜBÜR, [Holistic SEO Presentation](https://www.youtube.com/watch?v=PCNnLSCjSMc), 2026)*

**What Mike King recommends:** Use LLMs to extract structured entity data directly from live APIs and inject that data into templates. The API extraction fulfills the semantic requirements automatically without manual mapping.
*(source: Mike King, [AI Search Manual](https://www.youtube.com/watch?v=ukpU-EfRtV4), April 2026)*

**Which side I take and why:** King's method for Lane A. For a database-heavy SaaS with API access, manual semantic mapping creates an operational bottleneck that engineering velocity can eliminate. The API data, when structured correctly, satisfies the entity-attribute relationships Koray identifies as necessary — it just does it programmatically rather than editorially. Koray's manual approach is preserved in Lane B for teams without that engineering access.

**The context of the disagreement:** Koray's framework was built for content-heavy publishers with large editorial teams. King is speaking to technical SEOs with developer resources. This is an operational capacity disagreement, not a strategic one.

---

## Section: What I Rejected and Why

### Rejected: High-Volume TOFU Informational Glossaries

**The idea:** Use AI to generate hundreds of definition pages — "What is an ATS," "How to conduct a structured interview," "What is a hiring funnel."

**Why I rejected it:** Google's AI Overviews answer these queries immediately with zero-click results. For a platform where the conversion metric is software signups, capturing readers who need a definition provides no pipeline value. Every engineering and content resource allocated to TOFU glossaries is a resource not allocated to the BOFU intent that actually drives ARR. This rejection applies at every operational stage — there is no stage at which building TOFU glossaries is the right move for an ATS in 2026.

---

### Rejected: Fully Autonomous Zero-Human Publishing Pipelines

**The idea:** Connect an API directly to an LLM, auto-generate pages, publish to the live domain at maximum velocity with no human review step.

**Why I rejected it:** HR, salary, and hiring compliance data are YMYL categories. A single Google core update classifying the domain as a programmatic spam farm does not set the pipeline back — it ends it. The convergence hub in this playbook exists specifically because this rejection is non-negotiable. Scale is only valuable if the domain retains its ability to rank. This rejection also applies at every stage — the human-in-the-loop review is the cost of operating in a YMYL category, not an optional efficiency upgrade.

---

## Section: My Original Ideas

### The "Shadow Tech-Stack" Deconstruction Hubs

**The idea:** None of the experts in this playbook addressed targeting workflow exhaustion as the primary conversion trigger. The conventional SEO approach targets product category keywords — "best ATS software," "ATS for startups." My original idea is to target the Shadow Tech Stacks our ideal buyer is currently maintaining instead.

We build a programmatic matrix of BOFU landing pages targeting specific integration queries: "How to connect Workable with ChatGPT and Calendly," "Zapier workflows for automated resume screening," "How to filter AI-generated job applications from your inbox." These are not comparison pages. They are workflow deconstruction pages that intercept the buyer at the exact moment of operational frustration.

**Who we are reaching:** The tech-savvy HR Director or startup founder who has already validated that their hiring problem is real and worth solving. They are not searching for a product category. They are searching for a fix to a specific broken step in a workflow they built themselves.

**Why it could work:**

1. **It avoids TOFU cannibalization** — AI Overviews can summarize "what is an ATS" but cannot provide nuanced, product-specific tutorials on connecting three disparate APIs with different rate limits and authentication methods. This traffic is structurally protected from AI summarization.

2. **It respects algorithmic risk** — Instead of thousands of thin "City + Job Title" pages, we are building a smaller, highly structured matrix of workflow solutions. Lower volume, higher specificity, easier to pass E-E-A-T verification at the convergence hub.

3. **It maximizes conversion logic** — The Frankenstein-Stack buyer is not evaluating products. They are evaluating escape routes. When they land on a page that names their exact workflow and shows them the hidden maintenance cost of maintaining it — API rate limits, broken Zaps, context switching between five tabs — 100hires presents as consolidation, not competition.

4. **It creates compounding word-of-mouth without a formal affiliate program** — This buyer has already invested significant time and cognitive effort validating that their problem is worth solving. When 100hires eliminates that stack, their prior investment makes them psychologically committed to the solution succeeding. They evangelize in the same subreddits and Slack communities where they were previously searching for integration fixes. They recommend 100hires because recommending it validates the decision they made. That is referral behavior without referral infrastructure — and it compounds because the communities they evangelize in are the same communities where the next Frankenstein-Stack buyer is currently searching.

---

## Section: Weaknesses of This Playbook

The weaknesses below are not surprises. They are visible throughout this document in the embedded operating conditions of every node and every conflict resolution. This section names them explicitly.

**1. Domain Authority Dependency**
This entire pipeline assumes sufficient baseline domain strength to index deep programmatic pages. The decision tree has no backlink acquisition strategy. If 100hires currently operates at low DR, the pages will be crawled and ignored. This playbook requires a parallel link acquisition effort that is outside its scope.

**2. The Conversion Assumption**
The playbook assumes that the Frankenstein-Stack buyer will convert on a programmatic landing page without high-touch sales intervention. In mid-market B2B, procurement often involves multiple stakeholders and a sales cycle. If the pages generate qualified traffic but no pipeline movement, the CAC model breaks. This assumption should be tested with a small batch before scaling.

**3. Platform Risk**
The entire architecture depends on Google's continued willingness to index and rank database-driven programmatic content. A mid-year core update targeting AI-assisted content clusters could devalue the templates regardless of E-E-A-T compliance. There is no hedge against this inside the playbook — it is a structural risk of the strategy.

**4. The Freshness Problem**
Job market data, salary benchmarks, and compliance requirements change. Programmatic pages built on stale API data become liabilities over time. The 90-day audit built into Node D2 is the structural response to this risk, but it requires consistent execution to be effective.

---

## Section: Who I Would NOT Recommend Following at This Stage

### Koray Tuğberk GÜBÜR — Premature at Early Operational Stage

Koray's framework is the most theoretically complete approach in this research set. His topical authority methodology is correct. The semantic entity-attribute mapping he describes is exactly what Google's retrieval systems are looking for.

The reason I would not recommend following his methodology at the early operational stage this playbook addresses is purely one of capacity. His framework assumes a large editorial team capable of manually mapping exhaustive semantic networks before publishing a single page. It assumes the time and resources to do that mapping properly across every micro-niche in the target domain.

At the stage this playbook is designed for, that capacity does not exist. Following Koray's framework without that capacity does not produce a slower version of his results — it produces a stalled pipeline, because the prerequisite work never gets completed before the business needs content live.

**When to return to his work:** Once the domain has established baseline topical authority in two or three micro-niches via Lane A or Lane C, Koray's semantic mapping framework becomes the right tool for deepening that authority systematically. His methodology is Stage B work. This playbook is Stage A.

The conflict between his approach and Mike King's API extraction method is resolved in this document not by declaring one wrong, but by assigning each to the operational stage where it creates leverage rather than friction.

---

*Sources are cited inline throughout this document. All research files are available in the `/research/` directory of this repository.*
