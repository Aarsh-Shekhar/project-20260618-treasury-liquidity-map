import unittest

from treasury_liquidity_map.models import Record
from treasury_liquidity_map.scoring import score_record


class DepthCheck35(unittest.TestCase):
    def test_035_backlog_triage(self):
        record = Record(id="cashflow-035", exposure=9543, signal=0.255, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
