import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class GitHubEvent:
    action: str
    issue: Dict[str, str]
    comment: Dict[str, str]

class GitHubApp:
    def __init__(self, token: str):
        self.token = token

    def handle_event(self, event: GitHubEvent):
        if event.action == 'created' and event.comment['body'] == '/wsc test':
            return self.trigger_workflow(event.issue['number'])
        return None

    def trigger_workflow(self, pr_number: int):
        # Simulate triggering a GitHub Action workflow
        return f'Triggered workflow for PR {pr_number}'

    def reply_with_status(self, pr_number: int, status: str):
        # Simulate replying with a status comment
        return f'Replied with status {status} for PR {pr_number}'
