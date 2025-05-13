from dataclasses import dataclass

@dataclass
class Employee:
    """Класс для хранения данных о сотруднике"""
    name: str
    department: str
    hours_worked: int
    rate: int
    payout: int