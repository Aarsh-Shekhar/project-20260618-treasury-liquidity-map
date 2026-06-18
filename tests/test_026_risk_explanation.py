import unittest

from treasury_liquidity_map.models import Record
from treasury_liquidity_map.scoring import score_record


class DepthCheck26(unittest.TestCase):
    def test_026_risk_explanation(self):
        record = Record(id="cashflow-026", exposure=52087, signal=0.760, urgency=2)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
