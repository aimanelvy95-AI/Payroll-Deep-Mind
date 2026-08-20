from src.payroll_deep_mind.employee import Employee
from src.payroll_deep_mind.payroll import calculate_gross_pay
from src.payroll_deep_mind.rules import validate_salary


def test_gross_pay():
    employee = Employee(
        employee_id="EMP001",
        name="Test Employee",
        basic_salary=5000,
    )

    assert calculate_gross_pay(employee, 500) == 5500


def test_salary_validation():
    assert validate_salary(5000) is True
    assert validate_salary(-100) is False
