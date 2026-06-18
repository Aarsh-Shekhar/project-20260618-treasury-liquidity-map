import unittest

from treasury_liquidity_map.models import Record
from treasury_liquidity_map.scoring import score_record


class DepthCheck32(unittest.TestCase):
    def test_032_operator_handoff(self):
        record = Record(id="cashflow-032", exposure=89019, signal=0.532, urgency=2)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
