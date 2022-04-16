from sales_person import SalesPerson

class SalesForce:
    def __init__(self):
        self.individual_sales()

    def add_data(self, file_name):
        self.file_name = file_name

    def quota_report(self, quota):
        self.quota = quota

    def top_seller(self):
        self.get_sale_frequencies()

    def individual_sales(self, employee_id):
        self.employee_id = employee_id

    def get_sale_frequencies(self):
        self.quota = quota

