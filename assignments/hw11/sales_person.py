class SalesPerson:
    def __init__(self, employee_id, name):
        self.name = name
        self.employee_id = employee_id
        
    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self):
        return self.name
        self.name = name

    def enter_sale(self, sale):
        self.sale = sale

    def total_sales(self, total_sales):
        return total_sales

    def get_sales(self, sales):
        return sales

    def met_quota(self, quota):
        self.quota = quota
        return quota

    def compare_to(self, other):
        self.other = other
        return other

    def __str__(self):
        pass