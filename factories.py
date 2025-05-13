from processing.normalizers import RateColumnNormalizer, ColumnNormalizer
from processing.readers import EmployeeCSVReader, CSVReader
from processing.reports import PayoutReportGenerator, ReportGenerator

class DataProcessorFactory:
    """Фабрика для создания компонентов обработки данных"""
    @staticmethod
    def create_column_normalizer() -> ColumnNormalizer:
        return RateColumnNormalizer()
    
    @staticmethod
    def create_csv_reader(normalizer: ColumnNormalizer) -> CSVReader:
        return EmployeeCSVReader(normalizer)
    
    @staticmethod
    def create_report_generator() -> ReportGenerator:
        return PayoutReportGenerator()