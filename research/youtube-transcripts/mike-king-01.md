---
author: "Mike King"
source_type: "YouTube"
date_collected: 2026-04-20
strategic_category: "Technical Architecture"
key_entities: ["Entity Extraction", "Data SEO", "LLM Workflows"]
---
# Transcript Analysis: Mike King

**Source URL:** https://www.youtube.com/watch?v=ukpU-EfRtV4

---

### [00:00]
SEO is deprecated. AI overviews are causing significant traffic losses — Wikipedia data shows clicks dropped sharply after AI overviews rolled out, consistent with studies showing 34.5% CTR reduction. Traditional search is melting down: the one-to-one relationship between rankings and revenue no longer holds. The market has decided the category is called GEO, not AEO or AI SEO.

### [08:15]
AI search is a shift from deterministic to probabilistic rankings. The core pattern is retrieval augmented generation (RAG): queries are encoded into vector representations, vector search identifies candidates, results are reranked, and the response is grounded in retrieved passages. Google uses hybrid retrieval — combining lexical search (BM25/TF-IDF) with semantic vector search — then reranks before generating the response.

### [18:30]
Query fan-out is where content strategy must focus. A single query like "best half marathon training plan" gets broken into dozens of synthetic sub-queries representing explicit and implicit user needs. Each sub-query gets routed to an expected content type — article, checklist, video, buyer guide. The goal is to rank for as many synthetic queries as possible across as many content formats as possible.

### [31:45]
Extractability is the key measure for AI content selection. Content must have high evidence density — verifiable, specific, dated claims that are easy to pull as discrete passages. Use semantic triples (subject-predicate-object sentences), short focused paragraphs, clear headings, and avoid ambiguous language. "As of February 2025, beginners should run no more than 3 miles in week one" outperforms vague best-practice statements.

### [44:00]
Relevance engineering requires an omnimedia content strategy. Visibility must extend beyond the website to video, audio, UGC platforms (Reddit, Quora, LinkedIn), and digital PR. Measurement must evolve beyond traffic and rankings to include passage relevance, entity salience, citation rate, and share of voice across AI channels. Tools like Qoria map synthetic query routing; Relevance Doctor analyzes layout-aware chunking scores.
