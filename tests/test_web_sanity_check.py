from src.web_sanity_check import WebSanityCheck
from src.github_app import GitHubEvent
import pytest

@pytest.fixture
def event():
    return GitHubEvent(
        action='created',
        issue={'number': '123'},
        comment={'body': '/wsc test'}
    )

def test_handle_comment(event):
    wsc = WebSanityCheck('token')
    result = wsc.handle_comment(event)
    assert result == 'Replied with status pass for PR 123'

def test_handle_comment_invalid_comment():
    event = GitHubEvent(
        action='created',
        issue={'number': '123'},
        comment={'body': 'invalid comment'}
    )
    wsc = WebSanityCheck('token')
    result = wsc.handle_comment(event)
    assert result is None
