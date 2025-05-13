import argparse
import json
from factories import DataProcessorFactory
from processing.reports import PayoutReportGenerator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_files', nargs='+', help='List of csv files')
    parser.add_argument('--report', help='Report name')
    args = parser.parse_args()

    # Создаем компоненты через фабрику
    factory = DataProcessorFactory()
    normalizer = factory.create_column_normalizer()
    reader = factory.create_csv_reader(normalizer)
    report_generator = factory.create_report_generator()
    
    employees = []
    for file in args.csv_files:
        some_employees = reader.read(file)
        employees.extend(some_employees)
    
    reports = report_generator.generate(employees)
    PayoutReportGenerator.save_to_json(reports, args.report)

if __name__ == '__main__':
    main()