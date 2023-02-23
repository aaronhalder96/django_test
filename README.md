# django_test
Django app to track corporate assets

System Requirements: Python Version >= 3.8.0

To clone the repository with HTTPS, use the following command in your desired directory:
git clone https://github.com/aaronhalder96/django_test.git

Before running the app, please install the packages mentioned in the requirements.txt file by using the following command:
pip install -r requirements.txt

Step 1: Migrate the Django ORM
python manage.py makemigrations

Step 2: Migrate the Django ORM
python manage.py migrate

Step 3: Run the server
python manage.py runserver

DOCUMENTATION FOR USING THE API
1. GET http://127.0.0.1:8000/
Returns a list of all companies, employees of those companies, and devices of those companies

2. GET http://127.0.0.1:8000/companies/
Returns a list of all companies

3. POST http://127.0.0.1:8000/companies/
Adds a company to the list of companies
Sample JSON data
{
    "CompanyName": "your_company_name"
}

4. GET http://127.0.0.1:8000/company/<company_id>
Returns all employees and devices of a particular company

5. GET http://127.0.0.1:8000/employees/
Returns a list of all employees

6. POST http://127.0.0.1:8000/employees/
Adds an employee to the list of employees
Sample JSON data
{
    "CompanyId": your_company_id,
    "EmployeeName": "your_employee_name"
}

7. GET http://127.0.0.1:8000/devices/
Returns a list of all devices

8. POST http://127.0.0.1:8000/devices/
Adds a device to the list of devices
Sample JSON data
{
    "CompanyId": your_company_id,
    "DeviceType": "your_device_type" (e.g. Laptop),
    "DeviceName": "your_device_name" (e.g. e.g. IPhone 14 Pro)
}

9. GET http://127.0.0.1:8000/logs/
Returns a list of all logs

10. POST http://127.0.0.1:8000/assign/device/
Assigns a device to an employee of a company
Sample JSON data
{
    "CompanyId": your_company_id, 
    "DeviceId": your_device_id, 
    "EmployeeId": your_employee_id, 
    "CheckoutCondition": "your_device_condition"
}

11. POST http://127.0.0.1:8000/return/device/
Returns a device to the company from the employee
Sample JSON data
{
    "CompanyId": your_company_id, 
    "DeviceId": your_device_id, 
    "EmployeeId": your_employee_id, 
    "ReturnCondition": "your_device_condition"
}