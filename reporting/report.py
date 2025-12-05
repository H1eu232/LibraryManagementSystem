import datetime

class Report:
    def __init__(self, report_name, generated_date):
        self.report_name = report_name
        self.generated_date = generated_date

    def generate_report(self):
        date_str = self.generated_date.strftime("%Y-%m-%d")
        print(f"--- Generating Report: '{self.report_name}' on {date_str} ---")
        print("Report generation logic would go here...")
        print("--- End of Report ---")