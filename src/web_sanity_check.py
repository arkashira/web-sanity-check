import argparse
import json
import subprocess
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Config:
    url: str
    expected_status_code: int
    headers: Dict[str, str]

def check_website(config: Config) -> bool:
    try:
        response = subprocess.run(
            ["curl", "-o", "/dev/null", "-s", "-w", "%{http_code}", config.url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        status_code = int(response.stdout.strip())
        return status_code == config.expected_status_code
    except subprocess.CalledProcessError:
        return False

def load_config(file_path: str) -> List[Config]:
    with open(file_path, "r") as file:
        configs = json.load(file)
    return [
        Config(
            url=item["url"],
            expected_status_code=item["expected_status_code"],
            headers=item.get("headers", {}),
        )
        for item in configs
    ]

def main():
    parser = argparse.ArgumentParser(description="Web Sanity Check")
    parser.add_argument("--config", required=True, help="Path to the configuration JSON file")
    args = parser.parse_args()
    configs = load_config(args.config)
    results = {config.url: check_website(config) for config in configs}
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
