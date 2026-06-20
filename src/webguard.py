import concurrent.futures
import time
from dataclasses import dataclass
from typing import List

@dataclass
class TestResult:
    test_name: str
    execution_time: float
    passed: bool

class WebGuard:
    def __init__(self):
        self.test_results = []

    def execute_ui_test(self, test_name: str):
        # Simulate UI test execution time
        execution_time = 2.0
        time.sleep(execution_time)
        return TestResult(test_name, execution_time, True)

    def execute_api_test(self, test_name: str):
        # Simulate API test execution time
        execution_time = 1.0
        time.sleep(execution_time)
        return TestResult(test_name, execution_time, True)

    def execute_tests_in_parallel(self, ui_tests: List[str], api_tests: List[str]):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            ui_futures = {executor.submit(self.execute_ui_test, test): test for test in ui_tests}
            api_futures = {executor.submit(self.execute_api_test, test): test for test in api_tests}

            for future in concurrent.futures.as_completed(list(ui_futures) + list(api_futures)):
                test_name = ui_futures.get(future, api_futures.get(future))
                try:
                    test_result = future.result()
                except Exception as e:
                    print(f"Test {test_name} generated an exception: {e}")
                else:
                    self.test_results.append(test_result)

    def get_test_results(self):
        return self.test_results
