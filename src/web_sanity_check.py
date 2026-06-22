import json
from dataclasses import dataclass
from typing import List

@dataclass
class UserFlow:
    steps: List[str]

class WebSanityCheck:
    def __init__(self):
        self.recorded_flows = []

    def record_user_flow(self, flow: UserFlow):
        self.recorded_flows.append(flow)

    def generate_tests(self):
        tests = []
        for flow in self.recorded_flows:
            test = self._generate_test(flow)
            tests.append(test)
        return tests

    def _generate_test(self, flow: UserFlow):
        test = []
        for step in flow.steps:
            test.append(f"assert {step} == '{step}'")
        return "\n".join(test)

    def save_recorded_flows(self, filename: str):
        with open(filename, 'w') as f:
            json.dump([flow.__dict__ for flow in self.recorded_flows], f)

    def load_recorded_flows(self, filename: str):
        with open(filename, 'r') as f:
            flows = json.load(f)
            self.recorded_flows = [UserFlow(**flow) for flow in flows]
