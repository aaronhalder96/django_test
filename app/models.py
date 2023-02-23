from django.db import models

# Create your models here.
class Companies(models.Model):
    CompanyName = models.CharField(max_length=100, null=False)

class Employees(models.Model):
    CompanyId = models.ForeignKey(Companies, on_delete=models.CASCADE)
    EmployeeName = models.CharField(max_length=100, null=False)

class Devices(models.Model):
    CompanyId = models.ForeignKey(Companies, on_delete=models.CASCADE)
    DeviceType = models.CharField(max_length=100)
    DeviceName = models.CharField(max_length=100)
    State = models.CharField(max_length=100, default='Unassigned')

class Logs(models.Model):
    CompanyId = models.ForeignKey(Companies, on_delete=models.CASCADE)
    DeviceId = models.ForeignKey(Devices, on_delete=models.CASCADE)
    EmployeeId = models.ForeignKey(Employees, on_delete=models.CASCADE)
    CheckoutTime = models.DateTimeField(auto_now_add=True)
    CheckoutCondition = models.CharField(max_length=100, null=False)
    ReturnTime = models.DateTimeField(null=True)
    ReturnCondition = models.CharField(max_length=100, null=True)
