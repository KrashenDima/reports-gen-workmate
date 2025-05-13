from abc import ABC, abstractmethod
from typing import List, Dict
from models.employee import Employee
from processing.normalizers import ColumnNormalizer

class CSVReader(ABC):
    """Абстрактный класс для чтения CSV файлов"""
    def __init__(self, normalizer: ColumnNormalizer):
        self.normalizer = normalizer
    
    @abstractmethod
    def read(self, file_path: str) -> List[Employee]:
        pass

class EmployeeCSVReader(CSVReader):
    """Конкретная реализация чтения CSV файлов с данными сотрудников"""
    def read(self, file_path: str) -> List[Employee]:
        employees = []
        try:
            with open(file_path, encoding='utf-8') as file:
                lines = [line.strip() for line in file if line.strip()]

                if not lines:
                    return employees

                column_names = [self.normalizer.normalize(col) for col in lines[0].split(',')]
                
                for line in lines[1:]:
                    values = line.split(',')
                    if len(values) != len(column_names):
                        print(f"Warning: Row has {len(values)} values but expected {len(column_names)}")
                        continue
                    
                    row = dict(zip(column_names, values))
                    try:
                        hours_worked = int(row.get('hours_worked', 0))
                        rate = int(row.get('rate', 0))
                        employee = Employee(
                            name=row.get('name', ''),
                            department=row.get('department', ''),
                            hours_worked=hours_worked,
                            rate=rate,
                            payout=hours_worked*rate
                        )
                        employees.append(employee)
                    except (ValueError, KeyError) as e:
                        print(f"Error processing row: {row}. Error: {e}")

        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
        except Exception as e:
            print(f"Error processing file {file_path}: {str(e)}")
        
        return employees
