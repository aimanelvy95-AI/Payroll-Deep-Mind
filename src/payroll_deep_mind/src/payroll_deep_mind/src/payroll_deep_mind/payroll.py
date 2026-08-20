from .employee import Employee


def calculate_gross_pay(employee: Employee, allowance: float = 0.0) -> float:
    return employee.basic_salary + allowance
