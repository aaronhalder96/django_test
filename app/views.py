from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from datetime import datetime

class HomeView(APIView):
    """
    GET: List all info of companies, employees of those companies, and devices of those companies
    """
    def get(self, request, format=None):
        companies = Companies.objects.all()
        employees = Employees.objects.all()
        devices = Devices.objects.all()
        output = []
        for company in companies:
            output.append({'id': company.id, 'name': company.CompanyName, 
                            'employees': [employee.EmployeeName for employee in employees.filter(CompanyId=company.id)],
                            'devices': [device.DeviceName for device in devices.filter(CompanyId=company.id)]})
        return Response(output)

class CompaniesView(APIView):
    """
    GET: List all companies
    POST: Add a company
    """
    def get(self, request, format=None):
        companies = Companies.objects.all()
        serializer = CompaniesSerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompaniesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleCompanyView(APIView):
    """
    GET: List all info of a single company, including its employees and devices
    """
    def get(self, request, company_id=None):
        if company_id is None:
            return Response({'message': 'Company ID is needed to view the details.'}, status=status.HTTP_400_BAD_REQUEST)
        company = Companies.objects.filter(id=company_id).first()
        if company is None:
            return Response({'message': 'Company cannpot be found or does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        employees = Employees.objects.filter(CompanyId=company_id)
        devices = Devices.objects.filter(CompanyId=company_id)
        output = {'company_name': company.CompanyName, 
                    'employees': [employee.EmployeeName for employee in employees],
                    'devices': [device.DeviceName for device in devices]}
        return Response(output)

class EmployeesView(APIView):
    """
    GET: List all employees
    POST: Add an employee
    """
    def get(self, request, format=None):
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DevicesView(APIView):
    """
    GET: List all devices
    POST: Add a device
    """
    def get(self, request, format=None):
        devices = Devices.objects.all()
        serializer = DevicesSerializer(devices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DevicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogsView(APIView):
    """
    GET: List all logs
    POST: Add a log
    """
    def get(self, request, format=None):
        logs = Logs.objects.all()
        serializer = LogsSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LogsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignDeviceView(APIView):
    """
    POST: Assign device to employee
    """
    def post(self, request, format=None):
        serializer = LogsSerializer(data=request.data)
        if serializer.is_valid():
            device_id = serializer.validated_data['DeviceId'].id
            employee_id = serializer.validated_data['EmployeeId'].id
            company_id = serializer.validated_data['CompanyId'].id
            device = Devices.objects.filter(id=device_id, State='Unassigned', CompanyId=company_id).first()
            if device is None:
                return Response({'message': 'Device cannot be found or is not available.'}, status=status.HTTP_400_BAD_REQUEST)
            employee = Employees.objects.filter(id=employee_id, CompanyId=company_id).first()
            if employee is None:
                return Response({'message': 'Employee cannot be found or does not belong to this company.'}, status=status.HTTP_400_BAD_REQUEST)
            device.State = 'Assigned'
            device.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReturnDeviceView(APIView):
    """
    POST: Return device from employee
    """
    def post(self, request, format=None):
        request_data = request.data
        device_id = request_data.get('DeviceId', None)
        employee_id = request_data.get('EmployeeId', None)
        company_id = request_data.get('CompanyId', None)
        return_condition = request_data.get('ReturnCondition', None)
        if device_id is None or employee_id is None or company_id is None or return_condition is None:
            return Response({'message': 'Invalid JSON data.'}, status=status.HTTP_400_BAD_REQUEST)
        device = Devices.objects.filter(id=device_id, State='Assigned', CompanyId=company_id).first()
        if device is None:
            return Response({'message': 'Device cannot be found or is not assigned to any employee.'}, status=status.HTTP_400_BAD_REQUEST)
        employee = Employees.objects.filter(id=employee_id, CompanyId=company_id).first()
        if employee is None:
            return Response({'message': 'Employee cannot be found or does not belong to this company.'}, status=status.HTTP_400_BAD_REQUEST)
        log = Logs.objects.filter(DeviceId=device_id, EmployeeId=employee_id, CompanyId=company_id).last()
        if log is None:
            return Response({'message': 'Device log cannot be found or does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        device.State = 'Unassigned'
        device.save()
        log.ReturnCondition = return_condition
        log.ReturnTime = datetime.utcnow()
        log.save()
        serializer = LogsSerializer(log)
        return Response(serializer.data, status=status.HTTP_201_CREATED)