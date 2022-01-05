from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from app.models.incident import Incident


@dataclass
class Store:
    incidents: list[Incident] = field(init=False, default_factory=list)

    def incident_status(self, start_date: datetime, end_date: datetime) -> dict[str, Any]:
        """
        Get the status of the store between the dates given

        Parameters
        ----------
        start_date : datetime
            the start date to search in the list of incidents

        end_date : datetime
            the end date to search in the list of incidents

        Returns
        -------
        dict
            the status of the store
        """
        return {
            'open_cases': self.get_open_cases_qty(start_date, end_date),
            'closed_cases': self.get_closed_cases_qty(start_date, end_date),
            'average_solution': self.get_average_solution_time(start_date, end_date),
            'maximum_solution': self.get_current_maximum_solution_time(start_date, end_date)
        }

    def get_open_cases_qty(self, start_date: datetime, end_date: datetime) -> int:
        """
        Get the quantity of the open cases in the store between the dates given

        Parameters
        ----------
        start_date : datetime
            the start date to search in the list of incidents

        end_date : datetime
            the end date to search in the list of incidents

        Returns
        -------
        int
            the quantity
        """
        open_cases_qty: int = 0
        for incident in self.incidents:
            if start_date < incident.created_at < end_date:
                if not incident.is_solved:
                    open_cases_qty += 1

        return open_cases_qty

    def get_closed_cases_qty(self, start_date: datetime, end_date: datetime) -> int:
        """
        Get the quantity of the closed cases in the store between the dates given

        Parameters
        ----------
        start_date : datetime
            the start date to search in the list of incidents

        end_date : datetime
            the end date to search in the list of incidents

        Returns
        -------
        float
            the quantity
        """
        closed_cases_qty: int = 0
        for incident in self.incidents:
            if incident.is_solved and start_date < incident.created_at < end_date:
                closed_cases_qty += 1

        return closed_cases_qty

    def get_average_solution_time(self, start_date: datetime, end_date: datetime) -> float:
        """
        Get the average solution time between the dates given

        Parameters
        ----------
        start_date : datetime
            the start date to search in the list of incidents

        end_date : datetime
            the end date to search in the list of incidents

        Returns
        -------
        float
            the average in seconds
        """
        solution_time: int = 0
        incident_qty: int = 0
        for incident in self.incidents:
            if incident.is_solved and start_date < incident.created_at < end_date:
                solution_time += int(incident.get_solution_time())
                incident_qty += 1

        if incident_qty == 0:
            return 0

        return solution_time / incident_qty

    def get_current_maximum_solution_time(self, start_date: datetime, end_date: datetime) -> int:
        """
        Get the current maximum solution time between the dates given

        Parameters
        ----------
        start_date : datetime
            the start date to search in the list of incidents

        end_date : datetime
            the end date to search in the list of incidents

        Returns
        -------
        float
            the maximum in seconds
        """
        max_solution_time: int = 0
        for incident in self.incidents:
            if start_date < incident.created_at < end_date:
                current_solution_time = int(incident.get_solution_time())
                if current_solution_time > max_solution_time:
                    max_solution_time = current_solution_time

        return max_solution_time
