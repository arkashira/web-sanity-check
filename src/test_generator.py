import json
from dataclasses import dataclass
from typing import List

@dataclass
class UserFlow:
    steps: List[str]

def generate_tests(user_flows: List[UserFlow], recording_tool: str) -> List[str]:
    """
    Generate tests from recorded user flows.

    Args:
    - user_flows (List[UserFlow]): List of user flows.
    - recording_tool (str): Recording tool used (e.g., Selenium, Cypress).

    Returns:
    - List[str]: List of generated tests.
    """
    tests = []
    for flow in user_flows:
        test = f"def test_{recording_tool}_{flow.steps[0]}():\n"
        test += "    # Test generated from user flow\n"
        test += "    assert True\n"
        tests.append(test)
    return tests

def calculate_coverage(user_flows: List[UserFlow], generated_tests: List[str]) -> float:
    """
    Calculate test coverage.

    Args:
    - user_flows (List[UserFlow]): List of user flows.
    - generated_tests (List[str]): List of generated tests.

    Returns:
    - float: Test coverage percentage.
    """
    covered_flows = 0
    for flow in user_flows:
        for test in generated_tests:
            if flow.steps[0] in test:
                covered_flows += 1
                break
    return (covered_flows / len(user_flows)) * 100
