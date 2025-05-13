import json

from abc import ABC, abstractmethod
from typing import List, Set
from dataclasses import dataclass, asdict
from models.employee import Employee
from models.department import DepartmentReport

class ReportGenerator(ABC):
    """Абстрактный класс для генерации отчетов"""
    @abstractmethod
    def generate(self, employees: List[Employee]) -> List[DepartmentReport]:
        pass

class PayoutReportGenerator(ReportGenerator):
    """Генератор отчетов о выплатах"""
    def generate(self, employees: List[Employee]) -> List[DepartmentReport]:
        departments = self._get_unique_departments(employees)
        reports = []
        
        for dept in departments:
            dept_employees = [emp for emp in employees if emp.department == dept]
            reports.append(DepartmentReport(
                name=dept,
                employees=dept_employees
            ))
        
        return reports
    
    def _get_unique_departments(self, employees: List[Employee]) -> Set[str]:
        return {emp.department for emp in employees}
    
    @staticmethod
    def save_to_json(reports: List[DepartmentReport], filename: str) -> None:
        report_data = {
            'departments': [asdict(report) for report in reports]
        }
        # Сохраняем в файл с красивым форматированием
        with open(f"{filename}.json", 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=4, ensure_ascii=False)