from dataclasses import dataclass


@dataclass(order=True)
class Jobs:
    position : str
    company_fix : str
    city : str
    salary : str
    intrest : int
    acept : int