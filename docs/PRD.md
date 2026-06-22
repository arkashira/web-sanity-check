# Product Requirements Document (PRD)  
**Project:** Web Sanity Check  
**Repository:** `web-sanity-check`  
**Owner:** Axentx – Product & Engineering Lead  
**Date:** 2026‑06‑22  

---

## 1. Problem Statement  

In large web applications, automated UI and integration tests frequently become flaky due to race conditions, timing issues, or external dependencies. Flaky tests:

- **Consume CI resources** (re‑runs, longer pipelines).  
- **Reduce developer confidence** (false positives/negatives).  
- **Mask real failures** and delay releases.  

Current tooling in the company only logs test failures; it does **not** provide a systematic way to:

1. Detect and rank flaky tests over time.  
2. Prioritize which tests need stabilization effort.  
3. Track investigation status so that the same flaky test isn’t repeatedly re‑investigated.  

Without a focused approach, teams waste time chasing transient failures and miss critical bugs.

---

## 2. Target Users  

| Persona | Role | Pain Points | How Web Sanity Check Helps |
|---------|------|-------------|---------------------------|
| **QA Engineers** | Test Lead | Overwhelmed by flaky test noise; needs quick insights into which tests are most unstable. | Provides a ranked list of flaky tests with historical stability metrics. |
| **DevOps / CI Engineers** | Pipeline Owner | CI pipeline stalls due to repeated test failures; wants to reduce unnecessary re‑runs. | Allows marking tests as “investigated” so they can be temporarily excluded or flagged for re‑run only when needed. |
| **Product Managers** | Release Owner | Needs confidence that releases are stable; wants visibility into test reliability. | Offers a simple API to surface flaky test counts and trends in release dashboards. |
| **Developers** | Feature Owner | Wants to know which tests are flaky before committing code that may affect them. | Exposes a lightweight CLI/SDK that can be integrated into pre‑commit hooks. |

---

## 3. Goals & Success Metrics  

| Goal | Success Metric | Target |
|------|----------------|--------|
| **Detect flaky tests accurately** | Precision & Recall of flaky test detection (≥ 90 %) | 90 %+ |
| **Prioritize stabilization effort** | Mean time to fix (MTTF) for top‑ranked flaky tests | Reduce by 30 % vs baseline |
| **Reduce CI waste** | Percentage of CI time spent on re‑runs due to flakiness | Decrease by 25 % |
| **Improve developer confidence** | User satisfaction score (survey) | ≥ 4.5/5 |
| **Enable easy integration** | Number of integrations (CI, IDE, Slack) | ≥ 3 by Q3 2026 |

---

## 4. Key Features (Prioritized)

| # | Feature | Description | Priority | Notes |
|---|---------|-------------|----------|-------|
| 1 | **Flaky Test Detection Engine** | Analyzes test run history, flags tests that fail intermittently (failure rate > threshold, e.g., 10 % over last 30 runs). | Must-Have | Uses `add_test_result` to ingest results. |
| 2 | **Ranking & Prioritization** | Scores flaky tests by volatility, impact (e.g., critical path), and frequency. Exposes `get_flaky_tests` with sorting options. | Must-Have | Output includes confidence score and suggested action. |
| 3 | **Investigation Tracking** | Allows marking a test as investigated (`mark_test_as_investigated`). Stores investigation metadata (investigator, timestamp, notes). | Must-Have | Prevents duplicate work. |
| 4 | **CLI & SDK** | Simple command‑line tool to run detection on a local test run, and a Python SDK for CI integration. | Nice-to-Have | Should be zero‑dependency for CI environments. |
| 5 | **Dashboard API** | REST endpoint to expose flaky test metrics for dashboards (e.g., Grafana, PowerBI). | Nice-to-Have | JSON schema defined. |
| 6 | **Notification Hook** | Optional Slack/Teams webhook to alert teams when a test’s volatility crosses a threshold. | Nice-to-Have | Configurable per project. |
| 7 | **Data Persistence Layer** | Store results in a lightweight SQLite DB (or optional PostgreSQL). | Must-Have | Schema: `test_name`, `run_id`, `status`, `timestamp`, `investigated_at`, `investigator`. |
| 8 | **Configuration** | YAML/JSON config for thresholds, notification settings, and integration tokens. | Must-Have | Defaults provided. |
| 9 | **Extensibility** | Plugin system to support custom test frameworks (e.g., Cypress, Playwright). | Nice-to-Have | Abstract `TestResultParser`. |

---

## 5. Scope

### In‑Scope

- Core detection, ranking, and investigation tracking logic.  
- CLI and Python SDK for CI integration.  
- SQLite persistence with optional PostgreSQL support.  
- Basic REST API for metrics.  
- Unit & integration tests covering core logic.  
- Documentation (README, API reference, usage guide).  

### Out‑of‑Scope

- Full‑blown UI dashboard (handled by external monitoring tools).  
- Advanced machine‑learning models for flakiness prediction.  
- Integration with proprietary test frameworks not in the public domain.  
- Real‑time streaming analytics (Kafka, etc.).  

---

## 6. Acceptance Criteria  

1. **Detection** – Given a series of test results, `get_flaky_tests` returns all tests that meet the flakiness threshold with ≥ 90 % precision.  
2. **Ranking** – The returned list is sorted by volatility score; top‑3 tests are the most unstable.  
3. **Investigation** – After calling `mark_test_as_investigated`, the test no longer appears in the top‑ranked list until it re‑enters the threshold.  
4. **CLI** – Running `web-sanity-check run` on a local test output file prints a table of flaky tests.  
5. **SDK** – CI pipeline can call `add_test_result` for each test and retrieve the flaky list via `get_flaky_tests`.  
6. **Persistence** – All data survives process restarts; running the tool twice with the same data yields identical results.  
7. **Documentation** – README includes installation, configuration, CLI usage, and SDK examples.  

---

## 7. Technical Constraints & Decisions  

- **Language**: Python 3.11 (consistent with existing Axentx tooling).  
- **Dependencies**: `pandas` for data manipulation, `fastapi` for REST API, `uvicorn` for dev server.  
- **Testing**: `pytest` + `pytest-mock`.  
- **CI**: GitHub Actions – lint, test, and build Docker image.  
- **Packaging**: `setuptools` + `wheel`; publish to internal PyPI.  

---

## 8. Roadmap (High‑Level)

| Milestone | Deliverable | Target Date |
|-----------|-------------|-------------|
| MVP | Core detection, ranking, CLI, SDK, persistence | 2026‑07‑15 |
| Feature Set 1 | Investigation tracking, basic API | 2026‑08‑01 |
| Feature Set 2 | Notification hook, optional PostgreSQL | 2026‑09‑01 |
| Feature Set 3 | Dashboard API, plugin system | 2026‑10‑15 |

---

## 9. Risks & Mitigations  

| Risk | Impact | Mitigation |
|------|--------|------------|
| **False positives** in flakiness detection | Low confidence, wasted effort | Tune thresholds; allow user overrides |
| **Data volume** in large projects | Performance degradation | Use incremental updates; index DB |
| **Integration friction** with diverse test frameworks | Low adoption | Provide clear SDK examples; support common frameworks first |
| **Security** of stored test results | Data leakage | Encrypt DB at rest; restrict access via API keys |

---

## 10. Stakeholder Sign‑Off  

| Stakeholder | Role | Signature |
|-------------|------|-----------|
| Alex | Product Manager | ☐ |
| Maya | Lead QA Engineer | ☐ |
| Ravi | DevOps Lead | ☐ |
| Lina | Engineering Lead | ☐ |

---
