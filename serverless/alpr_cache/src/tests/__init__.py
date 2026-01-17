import unittest
import json


class AlprCacheTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("test_overpass_data.json") as f:
            cls.overpass_test_data_raw = f.read()

    def setUp(self):
        # On every test setup, overpass_test_data is reset just in case it's contents where mutated.
        self.overpass_test_data = json.loads(self.overpass_test_data_raw)

