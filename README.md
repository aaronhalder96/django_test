# django_test
Django app to track corporate assets

System Requirements: Python Version >= 3.8.0

To clone the repository with HTTPS, use the following command in your desired directory:<br />
git clone https://github.com/aaronhalder96/django_test.git

Before running the app, please install the packages mentioned in the requirements.txt file by using the following command:<br />
pip install -r requirements.txt

Step 1: Migrate the Django ORM<br />
python manage.py makemigrations

Step 2: Migrate the Django ORM<br />
python manage.py migrate

Step 3: Run the server<br />
python manage.py runserver

DOCUMENTATION FOR USING THE API

1. GET http://127.0.0.1:8000/   <br />
Returns a list of all companies, employees of those companies, and devices of those companies

2. GET http://127.0.0.1:8000/companies/ <br />
Returns a list of all companies

3. POST http://127.0.0.1:8000/companies/    <br />
Adds a company to the list of companies<br />
Sample JSON data<br />
{<br />
    "CompanyName": "your_company_name"<br />
}

4. GET http://127.0.0.1:8000/company/<company_id>   <br />
Returns all employees and devices of a particular company

5. GET http://127.0.0.1:8000/employees/     <br />
Returns a list of all employees

6. POST http://127.0.0.1:8000/employees/        <br />
Adds an employee to the list of employees<br />
Sample JSON data<br />
{<br />
    "CompanyId": your_company_id,<br />
    "EmployeeName": "your_employee_name"<br />
}

7. GET http://127.0.0.1:8000/devices/   <br />
Returns a list of all devices

8. POST http://127.0.0.1:8000/devices/      <br />
Adds a device to the list of devices<br />
Sample JSON data<br />
{<br />
    "CompanyId": your_company_id,<br />
    "DeviceType": "your_device_type" (e.g. Laptop),<br />
    "DeviceName": "your_device_name" (e.g. e.g. IPhone 14 Pro)<br />
}

9. GET http://127.0.0.1:8000/logs/      <br />
Returns a list of all logs

10. POST http://127.0.0.1:8000/assign/device/   <br />
Assigns a device to an employee of a company<br />
Sample JSON data<br />
{<br />
    "CompanyId": your_company_id, <br />
    "DeviceId": your_device_id, <br />
    "EmployeeId": your_employee_id, <br />
    "CheckoutCondition": "your_device_condition"<br />
}

11. POST http://127.0.0.1:8000/return/device/   <br />
Returns a device to the company from the employee<br />
Sample JSON data<br />
{<br />
    "CompanyId": your_company_id, <br />
    "DeviceId": your_device_id, <br />
    "EmployeeId": your_employee_id, <br />
    "ReturnCondition": "your_device_condition"<br />
}