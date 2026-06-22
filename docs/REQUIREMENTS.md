# REQUIREMENTS.md

## Project Overview
`web-sanity-check` is a lightweight utility that aggregates test execution results, identifies flaky tests, and tracks investigation status. It is intended to be used as a library within CI pipelines or as a standalone CLI tool for developers and QA engineers.

---

## Functional Requirements

| ID | Description | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| **FR‑1** | **Instantiate the checker** | Must | `WebSanityCheck()` returns a valid instance with an empty internal state. |
| **FR‑2** | **Add test results** | Must | `add_test_result(test_name: str, passed: bool, timestamp: datetime)` stores the result. Duplicate entries for the same test at the same timestamp are ignored. |
| **FR‑3** | **Retrieve flaky tests** | Must | `get_flaky_tests(threshold: float = 0.5)` returns a list of test names whose failure rate exceeds the threshold. Failure rate = failures / total runs. |
| **FR‑4** | **Mark test as investigated** | Must | `mark_test_as_investigated(test_name: str)` flags the test; subsequent calls to `get_flaky_tests` exclude flagged tests unless explicitly requested. |
| **FR‑5** | **Persist state** | Should | Provide optional `save_to_file(path: str)` and `load_from_file(path: str)` to serialize/deserialize the internal state using JSON. |
| **FR‑6** | **CLI integration** | Should | A command‑line interface (`web-sanity-check`) that accepts sub‑commands: `add`, `list`, `investigate`, `save`, `load`. |
| **FR‑7** | **Logging** | Should | Emit INFO logs for key actions (adding result, marking investigated, loading/saving). |
| **FR‑8** | **Unit tests** | Should | All public methods must have corresponding unit tests covering edge cases (no data, all passed, all failed). |

---

## Non‑Functional Requirements

| ID | Requirement | Details |
|----|-------------|---------|
| **NFR‑1** | **Performance** | Adding a result and retrieving flaky tests must operate in O(1) amortized time per operation. |
| **NFR‑2** | **Memory Footprint** | Internal state should not exceed 10 MB for 100 k test results. |
| **NFR‑3** | **Security** | No external network calls; all data is local. |
| **NFR‑4** | **Reliability** | State persistence must be atomic; partial writes should not corrupt the file. |
| **NFR‑5** | **Usability** | CLI should provide helpful help messages and clear error output. |
| **NFR‑6** | **Extensibility** | Design should allow future integration with CI systems (e.g., GitHub Actions, Jenkins). |
| **NFR‑7** | **Compliance** | Use only permissively licensed dependencies (MIT, Apache‑2.0). |

---

## Constraints

1. **Python Version** – Must run on Python 3.10+.
2. **Dependencies** – Only standard library modules are allowed; external packages are prohibited unless they are part of the standard library or bundled in the repo.
3. **File Format** – State persistence must use JSON; binary formats are disallowed.
4. **Testing** – All tests must pass under `pytest` with `--maxfail=1`.

---

## Assumptions

- Test names are unique identifiers; no two distinct tests share the same name.
- Timestamps are timezone‑aware `datetime` objects; chronological order is preserved by insertion time.
- The threshold for flakiness defaults to 0.5 (i.e., >50% failures) but can be overridden by the caller.
- Investigated tests are permanently excluded from flaky lists unless explicitly re‑enabled by the user.

---

## Deliverables

1. `web_sanity_check.py` – Core implementation.
2. `cli.py` – Command‑line interface.
3. `tests/` – Comprehensive unit tests.
4. `requirements.txt` – Empty or minimal (standard library only).
5. `README.md` – Updated with usage examples.

---

## Acceptance Checklist

- [ ] All functional requirements implemented and documented.
- [ ] Non‑functional requirements met (benchmarks, memory usage).
- [ ] Unit tests cover >90% code coverage.
- [ ] CLI works as described with `--help`.
- [ ] State persistence is atomic and recoverable.
- [ ] No external dependencies beyond the standard library.

---
