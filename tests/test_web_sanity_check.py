import json
import subprocess
from unittest.mock import patch
from web_sanity_check import Config, check_website, load_config

def test_load_config():
    config_data = [
        {"url": "http://example.com", "expected_status_code": 200},
        {"url": "http://example.org", "expected_status_code": 404},
    ]
    with patch("builtins.open", create=True) as mock_open:
        mock_open.return_value.__enter__.return_value.read.return_value = json.dumps(config_data)
        configs = load_config("dummy.json")
    assert len(configs) == 2
    assert configs[0].url == "http://example.com"
    assert configs[0].expected_status_code == 200
    assert configs[1].url == "http://example.org"
    assert configs[1].expected_status_code == 404

def test_check_website_success():
    config = Config(url="http://example.com", expected_status_code=200, headers={})
    with patch("subprocess.run") as mock_run:
        mock_run.return_value.stdout = "200"
        result = check_website(config)
    assert result is True

def test_check_website_failure():
    config = Config(url="http://example.com", expected_status_code=200, headers={})
    with patch("subprocess.run") as mock_run:
        mock_run.side_effect = subprocess.CalledProcessError(returncode=1, cmd=["curl"])
        result = check_website(config)
    assert result is False
