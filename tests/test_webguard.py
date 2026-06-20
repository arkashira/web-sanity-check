import pytest
from webguard import WebGuard, TestResult

@pytest.fixture
def webguard():
    return WebGuard()

def test_execute_ui_test(webguard):
    test_name = "ui_test_1"
    test_result = webguard.execute_ui_test(test_name)
    assert test_result.test_name == test_name
    assert test_result.execution_time >= 2.0
    assert test_result.passed

def test_execute_api_test(webguard):
    test_name = "api_test_1"
    test_result = webguard.execute_api_test(test_name)
    assert test_result.test_name == test_name
    assert test_result.execution_time >= 1.0
    assert test_result.passed

def test_execute_tests_in_parallel(webguard):
    ui_tests = ["ui_test_1", "ui_test_2"]
    api_tests = ["api_test_1", "api_test_2"]
    webguard.execute_tests_in_parallel(ui_tests, api_tests)
    test_results = webguard.get_test_results()
    assert len(test_results) == 4
    for test_result in test_results:
        assert test_result.passed

def test_execute_tests_in_parallel_empty_lists(webguard):
    ui_tests = []
    api_tests = []
    webguard.execute_tests_in_parallel(ui_tests, api_tests)
    test_results = webguard.get_test_results()
    assert len(test_results) == 0
