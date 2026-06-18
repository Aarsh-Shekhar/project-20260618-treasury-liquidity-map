import unittest

from treasury_liquidity_map.models import Record
from treasury_liquidity_map.scoring import score_record


class DepthCheck44(unittest.TestCase):
    def test_044_scenario_analysis(self):
        record = Record(id="cashflow-044", exposure=77587, signal=0.379, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
