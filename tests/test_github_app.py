from src.github_app import GitHubApp, GitHubEvent
import pytest

@pytest.fixture
def event():
    return GitHubEvent(
        action='created',
        issue={'number': '123'},
        comment={'body': '/wsc test'}
    )

def test_handle_event(event):
    app = GitHubApp('token')
    result = app.handle_event(event)
    assert result == 'Triggered workflow for PR 123'

def test_handle_event_invalid_comment():
    event = GitHubEvent(
        action='created',
        issue={'number': '123'},
        comment={'body': 'invalid comment'}
    )
    app = GitHubApp('token')
    result = app.handle_event(event)
    assert result is None

def test_trigger_workflow():
    app = GitHubApp('token')
    result = app.trigger_workflow(123)
    assert result == 'Triggered workflow for PR 123'

def test_reply_with_status():
    app = GitHubApp('token')
    result = app.reply_with_status(123, 'pass')
    assert result == 'Replied with status pass for PR 123'
