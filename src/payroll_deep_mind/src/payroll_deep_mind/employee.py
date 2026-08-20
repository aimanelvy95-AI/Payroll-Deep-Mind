from dataclasses import dataclass


@dataclass
class Employee:
    employee_id: str
    name: str
    basic_salary: float
