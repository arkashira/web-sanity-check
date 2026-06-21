import pytest
from src.web_sanity_check import generate_gitlab_ci_yaml, WebSanityCheckConfig

def test_generate_gitlab_ci_yaml_default_test_directory():
    config = WebSanityCheckConfig(test_directory="tests")
    yaml = generate_gitlab_ci_yaml(config)
    assert "web-sanity-check" in yaml
    assert "tests" in yaml

def test_generate_gitlab_ci_yaml_custom_test_directory():
    config = WebSanityCheckConfig(test_directory="custom-tests")
    yaml = generate_gitlab_ci_yaml(config)
    assert "web-sanity-check" in yaml
    assert "custom-tests" in yaml

def test_main_with_default_test_directory(capsys):
    import sys
    sys.argv = ["web_sanity_check.py"]
    from src.web_sanity_check import main
    main()
    captured = capsys.readouterr()
    assert "web-sanity-check" in captured.out
    assert "tests" in captured.out

def test_main_with_custom_test_directory(capsys):
    import sys
    sys.argv = ["web_sanity_check.py", "--test-directory", "custom-tests"]
    from src.web_sanity_check import main
    main()
    captured = capsys.readouterr()
    assert "web-sanity-check" in captured.out
    assert "custom-tests" in captured.out
