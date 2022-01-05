import unittest
from datetime import datetime

from app.models.incident import Incident


class TestIncident(unittest.TestCase):
    def test_get_solution_time(self):
        # given
        incident = Incident(
            description='incident',
            is_solved=True,
            created_at=datetime(2021, 12, 28, 20, 50, 10, 0),
            solved_at=datetime(2021, 12, 28, 20, 50, 30, 0)
        )
        duration_expected: float = 20

        # when
        solution_time = incident.get_solution_time()

        # then
        self.assertEqual(duration_expected, solution_time)


if __name__ == '__main__':
    unittest.main()
