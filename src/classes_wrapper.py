from dataclasses import dataclass


@dataclass(order=True)
class Jobs:
    position: str
    company_fix: str
    city: str
    salary: str
    intrest: int
    acept: int

@dataclass()
class configs_class:
    headers: []
    conf_animation: []
    url: 4
    main_logger: []
    console_logger: []
    json_file: []