import json
import unittest
from pathlib import Path

ROOTS_DIR = Path("data/roots")

class TestMorphologyFiles(unittest.TestCase):
    def test_all_json_valid(self):
        for file in ROOTS_DIR.glob("*.json"):
            with self.subTest(file=file.name):
                with open(file, encoding="utf-8") as f:
                    data = json.load(f)
                self.assertIn("phonology", data, f"Missing 'phonology' in {file.name}")
                self.assertIn("metadata", data, f"Missing 'metadata' in {file.name}")

    def test_phonology_structure(self):
        for file in ROOTS_DIR.glob("*.json"):
            with open(file, encoding="utf-8") as f:
                data = json.load(f)
            phon = data.get("phonology", {})
            self.assertIsInstance(phon.get("ipa", []), list)
            self.assertIn(phon.get("stress", ""), ["מלרע", "מלעיל", "לא ידוע"])

if __name__ == "__main__":
    unittest.main()