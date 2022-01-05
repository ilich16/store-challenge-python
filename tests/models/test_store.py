import unittest
from datetime import datetime
from typing import Any

from app.models.incident import Incident
from app.models.store import Store


class TestStore(unittest.TestCase):
    def test_incident_status(self):
        # given
        store = Store()
        store.incidents.append(
            Incident(
                description='incident #1',
                is_solved=True,
                created_at=datetime(2021, 12, 27, 20, 50, 10, 0),
                solved_at=datetime(2021, 12, 27, 20, 50, 50, 0),
            )
        )
        store.incidents.append(
            Incident(
                description='incident #2',
                is_solved=False,
                created_at=datetime(2022, 1, 2, 20, 50, 10, 0),
            )
        )
        store.incidents.append(
            Incident(
                description='incident #3',
                is_solved=False,
                created_at=datetime(2021, 12, 28, 20, 50, 10, 0),
            )
        )
        store.incidents.append(
            Incident(
                description='incident #4',
                is_solved=True,
                created_at=datetime(2021, 12, 28, 20, 50, 10, 0),
                solved_at=datetime(2021, 12, 28, 20, 50, 30, 0),
            )
        )
        store.incidents.append(
            Incident(
                description='incident #5',
                is_solved=False,
                created_at=datetime(2022, 1, 2, 20, 50, 10, 0),
            )
        )
        store.incidents.append(
            Incident(
                description='incident #6',
                is_solved=False,
                created_at=datetime(2021, 12, 28, 20, 50, 10, 0),
            )
        )
        start_date: datetime = datetime(2021, 12, 10, 20, 50, 0, 0)
        end_date: datetime = datetime(2022, 1, 3, 23, 50, 25, 0)
        expected_incident_status: dict[str, Any] = {
            'open_cases': 4,
            'closed_cases': 2,
            'average_solution': 30,
        }

        # when
        incident_status: dict[str, Any] = store.incident_status(start_date, end_date)

        # then
        self.assertEqual(incident_status['open_cases'], expected_incident_status['open_cases'])
        self.assertEqual(incident_status['closed_cases'], expected_incident_status['closed_cases'])
        self.assertEqual(incident_status['average_solution'], expected_incident_status['average_solution'])

    def test_get_open_cases_qty(self):
        # given
        store = Store()
        store.incidents.append(
            Incident(
                description='incident #1',
                is_solved=True,
                created_at=datetime(2021, 12, 28, 20, 50, 10, 0),
                solved_at=datetime.now()
            )
        )
        store.incidents.append(
            Incident(
                description='incident #2',
                is_solved=False,
                created_at=datetime(2022, 1, 2, 20, 50, 10, 0),
            )
        )
        store.incidents.append(
            Incident(
                description='incident #3',
                is_solved=False,
                created_at=datetime(2021, 12, 28, 20, 50, 10, 0),
            )
        )
        start_date: datetime = datetime(2021, 12, 30, 20, 50, 0, 0)
        end_date: datetime = datetime(2022, 1, 3, 20, 50, 25, 0)
        expected_open_cases_qty: int = 1

        # when
        open_cases_qty: int = store.get_open_cases_qty(start_date, end_date)

        # then
        self.assertEqual(open_cases_qty, expected_open_cases_qty)

    def test_get_closed_cases_qty(self):
        # given
        store = Store()
        store.incidents.append(
            Incident(
                description='incident #1',
                is_solved=False,
            )
        )
        store.incidents.append(
            Incident(
                description='incident #2',
                is_solved=False
            )
        )
        store.incidents.append(
            Incident(
                description='incident #3',
                is_solved=True,
                created_at=datetime(2021, 12, 28, 20, 50, 10, 0),
                solved_at=datetime.now()
            )
        )
        start_date: datetime = datetime(2021, 12, 28, 20, 50, 0, 0)
        end_date: datetime = datetime(2021, 12, 28, 20, 50, 25, 0)
        expected_open_cases_qty: int = 1

        # when
        closed_cases_qty: int = store.get_closed_cases_qty(start_date, end_date)

        # then
        self.assertEqual(closed_cases_qty, expected_open_cases_qty)

    def test_get_average_solution_time(self):
        # given
        store = Store()
        store.incidents.append(
            Incident(
                description='incident #1',
                is_solved=False,
            )
        )
        store.incidents.append(
            Incident(
                description='incident #2',
                is_solved=True,
                created_at=datetime(2021, 12, 28, 20, 50, 10, 0),
                solved_at=datetime(2021, 12, 28, 20, 50, 25, 0),
            )
        )
        store.incidents.append(
            Incident(
                description='incident #3',
                is_solved=True,
                created_at=datetime(2021, 12, 30, 20, 50, 10, 0),
                solved_at=datetime(2021, 12, 30, 20, 50, 25, 0),
            )
        )
        start_date: datetime = datetime(2021, 12, 27, 20, 50, 10, 0)
        end_date: datetime = datetime(2021, 12, 29, 20, 50, 10, 0)
        expected_average_solution_time: float = 15

        # when
        average_solution_time: float = store.get_average_solution_time(start_date, end_date)

        # then
        self.assertEqual(average_solution_time, expected_average_solution_time)

    def test_get_current_maximum_solution_time(self):
        # given
        store = Store()
        store.incidents.append(
            Incident(
                description='incident #1',
                is_solved=True,
                created_at=datetime(2021, 12, 28, 20, 50, 10, 0),
                solved_at=datetime(2021, 12, 28, 20, 50, 50, 0),
            )
        )
        store.incidents.append(
            Incident(
                description='incident #2',
                is_solved=True,
                created_at=datetime(2022, 1, 2, 20, 50, 10, 0),
                solved_at=datetime(2022, 1, 2, 20, 50, 20, 0),
            )
        )
        store.incidents.append(
            Incident(
                description='incident #3',
                is_solved=True,
                created_at=datetime(2022, 1, 2, 20, 50, 10, 0),
                solved_at=datetime(2022, 1, 2, 20, 50, 25, 0),
            )
        )
        start_date: datetime = datetime(2022, 1, 1, 20, 50, 10, 0)
        end_date: datetime = datetime(2022, 1, 3, 20, 50, 10, 0)
        expected_current_max_sol_time: float = 15

        # when
        current_max_sol_time: float = store.get_current_maximum_solution_time(start_date, end_date)

        # then
        self.assertEqual(current_max_sol_time, expected_current_max_sol_time)


if __name__ == '__main__':
    unittest.main()
