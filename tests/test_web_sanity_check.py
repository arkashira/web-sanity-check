import pytest
from src.web_sanity_check import run_web_sanity_check, TestResult

def test_run_web_sanity_check_pass():
    result = run_web_sanity_check("path/to/suite", "https://example.com", "api-key")
    assert result.passed
    assert result.summary_link == "https://example.com/test-summary"

def test_run_web_sanity_check_fail_invalid_url():
    result = run_web_sanity_check("path/to/suite", "invalid-url", "api-key")
    assert not result.passed
    assert result.summary_link == "invalid-url/test-summary"

def test_run_web_sanity_check_fail_empty_url():
    result = run_web_sanity_check("path/to/suite", "", "api-key")
    assert not result.passed
    assert result.summary_link == "/test-summary"

def test_main_pass():
    import sys
    import io
    import argparse
    from src.web_sanity_check import main

    # Mock argparse
    class MockArgparse:
        def __init__(self, suite_path, target_url, api_key):
            self.suite_path = suite_path
            self.target_url = target_url
            self.api_key = api_key

    # Mock sys.argv
    sys.argv = ["web_sanity_check", "--suite_path", "path/to/suite", "--target_url", "https://example.com", "--api_key", "api-key"]

    # Capture stdout
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput

    # Run main
    main()

    # Restore sys.stdout
    sys.stdout = sys.__stdout__

    # Check output
    assert "Test passed. Summary: https://example.com/test-summary" in capturedOutput.getvalue()

def test_main_fail():
    import sys
    import io
    import argparse
    from src.web_sanity_check import main

    # Mock argparse
    class MockArgparse:
        def __init__(self, suite_path, target_url, api_key):
            self.suite_path = suite_path
            self.target_url = target_url
            self.api_key = api_key

    # Mock sys.argv
    sys.argv = ["web_sanity_check", "--suite_path", "path/to/suite", "--target_url", "invalid-url", "--api_key", "api-key"]

    # Capture stdout
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput

    # Run main
    main()

    # Restore sys.stdout
    sys.stdout = sys.__stdout__

    # Check output
    assert "Test failed. Summary: invalid-url/test-summary" in capturedOutput.getvalue()
