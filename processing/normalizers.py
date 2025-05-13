from abc import ABC, abstractmethod
from typing import Set

class ColumnNormalizer(ABC):
    """Абстрактный класс для нормализации названий столбцов"""
    @abstractmethod
    def normalize(self, column_name: str) -> str:
        pass

class RateColumnNormalizer(ColumnNormalizer):
    """Нормализация столбцов с оплатой"""
    def __init__(self):
        self.payment_columns: Set[str] = {'rate', 'hourly_rate', 'salary'}
    
    def normalize(self, column_name: str) -> str:
        return 'rate' if column_name.strip().lower() in self.payment_columns else column_name