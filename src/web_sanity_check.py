import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class WebSanityCheckConfig:
    test_directory: str

def generate_gitlab_ci_yaml(config: WebSanityCheckConfig) -> str:
    yaml_template = """
stages:
  - test

web-sanity-check:
  stage: test
  image: docker:latest
  script:
    - docker pull web-sanity-check
    - docker run -t web-sanity-check wsc run {test_directory}
  allow_failure: false
"""
    return yaml_template.format(test_directory=config.test_directory)

def main():
    parser = ArgumentParser(description="Generate .gitlab-ci.yml snippet for web-sanity-check")
    parser.add_argument("--test-directory", help="Custom test directory", default="tests")
    args = parser.parse_args()
    config = WebSanityCheckConfig(test_directory=args.test_directory)
    print(generate_gitlab_ci_yaml(config))

if __name__ == "__main__":
    main()
