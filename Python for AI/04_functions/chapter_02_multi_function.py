import time

def sales_list():
    time.sleep(1)
    print(f"Sales list is being processed")
def valid_sales_list():
    time.sleep(2)
    print(f"Sales validation is been done")
def dashboard_making():
    time.sleep(2)
    print(f"Dashboard has been made")
def generate_report():
    print(f"Generating report")
    sales_list()
    valid_sales_list()
    dashboard_making()
    print(f"Report is ready")

generate_report()