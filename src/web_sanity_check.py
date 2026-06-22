from dataclasses import dataclass
from typing import List

@dataclass
class TestResult:
    test_name: str
    failure_rate: float
    source_file: str
    line_number: int
    investigated: bool = False

class WebSanityCheck:
    def __init__(self):
        self.test_results = []

    def add_test_result(self, test_name: str, failure_rate: float, source_file: str, line_number: int):
        self.test_results.append(TestResult(test_name, failure_rate, source_file, line_number))

    def get_flaky_tests(self):
        return [test for test in self.test_results if test.failure_rate > 30 and not test.investigated]

    def mark_test_as_investigated(self, test_name: str):
        for test in self.test_results:
            if test.test_name == test_name:
                test.investigated = True
                break
