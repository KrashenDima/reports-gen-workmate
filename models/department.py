from dataclasses import dataclass
from typing import List
from models.employee import Employee

@dataclass
class DepartmentReport:
    """Класс для хранения отчета по отделу"""
    name: str
    employees: List[Employee]
    total_hours: int = 0
    total_payout: int = 0

    def __post_init__(self):
        """Автоматически рассчитывает общие показатели при создании"""
        self.total_hours = sum(emp.hours_worked for emp in self.employees)
        self.total_payout = sum(emp.payout for emp in self.employees)