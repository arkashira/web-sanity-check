from github_app import GitHubApp, GitHubEvent

class WebSanityCheck:
    def __init__(self, token: str):
        self.app = GitHubApp(token)

    def handle_comment(self, event: GitHubEvent):
        result = self.app.handle_event(event)
        if result:
            pr_number = event.issue['number']
            status = 'pass' if result.startswith('Triggered') else 'fail'
            return self.app.reply_with_status(pr_number, status)
        return None
