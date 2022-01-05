from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional


@dataclass
class Incident:
    description: str
    is_solved: bool = False
    created_at: datetime = datetime.now()
    solved_at: Optional[datetime] = None

    def get_solution_time(self) -> float:
        """
        Get the time from when the incident was created until it was resolved

        Returns
        -------
        float
            the time in seconds
        """
        if self.solved_at is not None and self.is_solved:
            duration: timedelta = self.solved_at - self.created_at
            return duration.total_seconds()

        duration: timedelta = datetime.now() - self.created_at
        return duration.total_seconds()
