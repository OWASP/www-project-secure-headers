import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ci"))

from validate_md_links import load_config


class LoadConfigTest(unittest.TestCase):
    def load_timeout(self, timeout):
        with tempfile.TemporaryDirectory() as directory:
            config_path = Path(directory) / "config.json"
            config_path.write_text(json.dumps({"timeout": timeout}), encoding="utf-8")
            config = load_config(config_path)
            self.addCleanup(config["req_session"].close)
            return config["timeout"]

    def test_parses_timeout_in_seconds(self):
        self.assertEqual(60, self.load_timeout("60s"))

    def test_converts_timeout_in_milliseconds_to_seconds(self):
        self.assertEqual(1.5, self.load_timeout("1500ms"))


if __name__ == "__main__":
    unittest.main()
