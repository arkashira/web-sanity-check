# STORIES.md

## Epic 1 – Core Functionality

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| 1 | **As a QA engineer, I want to add test results to the system, so that I can track test stability over time.** | • `add_test_result(test_name: str, passed: bool, timestamp: datetime)` records the outcome.<br>• Duplicate results for the same test on the same day are ignored.<br>• Results are persisted in an in‑memory store (e.g., a dictionary) for the MVP. |
| 2 | **As a QA engineer, I want to retrieve a list of flaky tests, so that I can prioritize which tests to investigate.** | • `get_flaky_tests(threshold: float = 0.2)` returns test names with a failure rate ≥ threshold.<br>• The list is sorted by failure rate descending.<br>• The method returns an empty list if no tests exceed the threshold. |
| 3 | **As a QA engineer, I want to mark a test as investigated, so that it is excluded from future flaky test lists.** | • `mark_test_as_investigated(test_name: str)` flags the test.<br>• Investigated tests are omitted from `get_flaky_tests` results.<br>• The flag persists across multiple calls during the same session. |

## Epic 2 – Data Persistence

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| 4 | **As a product owner, I want the test results to be persisted to disk, so that data survives restarts.** | • On initialization, the system loads a JSON file (`data.json`) if present.<br>• On each `add_test_result`, the JSON file is updated atomically.<br>• The file format is `{ "tests": { "<test_name>": { "results": [...], "investigated": bool } } }`. |
| 5 | **As a developer, I want a clear API for exporting the current state, so that analytics can be run externally.** | • `export_state() -> dict` returns the full in‑memory data structure.<br>• The exported dict matches the on‑disk JSON schema. |

## Epic 3 – Reporting & Analytics

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| 6 | **As a QA engineer, I want to view a summary report of test stability, so that I can quickly gauge overall test health.** | • `generate_report()` returns a dict: `{ "total_tests": int, "flaky_tests": int, "investigated_tests": int, "average_failure_rate": float }`. |
| 7 | **As a QA engineer, I want to filter flaky tests by a custom time window, so that I can focus on recent instability.** | • `get_flaky_tests(start: datetime, end: datetime, threshold: float)` returns tests with failure rate ≥ threshold within the window.<br>• Tests with no results in the window are excluded. |

## Epic 4 – Integration & Extensibility

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| 8 | **As a CI/CD pipeline maintainer, I want to integrate the tool into a test runner, so that test results are automatically fed into the system.** | • Provide a simple CLI command `web-sanity-check add <test_name> <passed>` that calls `add_test_result`.<br>• The CLI writes results to the same JSON file used by the library. |
| 9 | **As a developer, I want to plug in a custom storage backend, so that the system can use a database in production.** | • Define an abstract `StorageBackend` interface with `load()`, `save(data)`, and `clear()` methods.<br>• The default implementation uses JSON; a stub for SQL can be added later. |
| 10 | **As a product owner, I want to configure the failure‑rate threshold via a config file, so that different projects can use different sensitivity levels.** | • Read `config.yaml` on startup; if missing, default threshold = 0.2.<br>• The config file can also specify the storage path. |

## Epic 5 – Testing & Validation

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| 11 | **As a QA engineer, I want unit tests for the core logic, so that regressions are caught early.** | • At least 90% code coverage for `WebSanityCheck` methods.<br>• Tests cover adding results, calculating failure rates, marking investigated, and persistence. |
| 12 | **As a developer, I want integration tests that simulate a full run, so that the CLI and storage work together.** | • A test script runs the CLI to add results, then calls `generate_report()` and verifies expected output.<br>• The test cleans up the JSON file after completion. |

## MVP Order

1. Core Functionality (stories 1‑3)  
2. Data Persistence (stories 4‑5)  
3. Reporting & Analytics (stories 6‑7)  
4. Integration & Extensibility (stories 8‑10)  
5. Testing & Validation (stories 11‑12)

---
