from schema.config import Config, Secret
import unittest
from pathlib import Path
from pydantic_yaml import YamlModel

DATA_DIR = Path(__file__).parent / "data"


class BaseYamlTest(unittest.TestCase):
    def setUp(self):
        self.expected: YamlModel = None
        self.path: Path = None

    def test_load(self):
        obj = type(self.expected).parse_file(self.path)
        self.assertEqual(self.expected, obj)

    def test_dump(self):
        with open(self.path) as f:
            self.assertEqual(f.read(), self.expected.yaml())


class TestConfig(BaseYamlTest):
    def setUp(self):
        self.expected = Config(port=5000)
        self.path = DATA_DIR / "config.yaml"


class TestSecret(BaseYamlTest):
    def setUp(self):
        self.expected = Secret(openai_api_key="test_key")
        self.path = DATA_DIR / "secret.yaml"
