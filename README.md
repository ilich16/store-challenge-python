# store-challenge-python

## Getting started
<hr />

### Prerequisites
You just need [Python](https://www.python.org/downloads/) 3.9+

### Installation
Clone the repo:
```
$ git clone https://github.com/ilich16/store-challenge-python.git
```

## Usage
<hr />

Open your command line application and enter the python interpreter:
```
$ python
```

There are two important classes: `Incident` and `Store`.

### Incident
You can create an `Incident` object importing its class, for example:
```
>>> from datetime import datetime
>>> from app.models.incident import Incident
>>> incident = Incident(description='incident', is_solved=True, created_at=datetime(2021, 12, 28, 20, 50, 10, 0))
```

The properties of an `Incident` object are:
- description: str (required)
- is_solved: bool (optional, default=False)
- created_at: datetime (optional, default=datetime.now())
- solved_at: Optional[datetime] (optional, default=None)

### Store
You can create a `Store` object importing its class, for example:
```
>>> from app.models.store import Store
>>> store = Store()
```

The properties of a `Store` object are:
- incidents: list (initial_value=[])

You need add `Incident` objects manually:
```
>>> store.incidents.append(first_incident)
>>> store.incidents.append(second_incident)
```

Now you can call to `incident_status` function:
```
>>> start_date = datetime(2021, 12, 28, 20, 50, 10)
>>> end_date = datetime(2021, 12, 29, 20, 50, 10)
>>> store.incident_status(start_date, end_date)
```

Note: the arguments of the datetime constructor are: `datetime(year, month, day, hour, minute, second)`

## Tests
<hr />

You can run tests executing the following commands:
```
python -m unittest tests/models/test_incident.py
python -m unittest tests/models/test_store.py
```