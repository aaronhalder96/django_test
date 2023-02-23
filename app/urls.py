from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("companies/", views.CompaniesView.as_view(), name="companies"),
    path("company/<int:company_id>/", views.SingleCompanyView.as_view(), name="single_company"),
    path("employees/", views.EmployeesView.as_view(), name="employees"),
    path("devices/", views.DevicesView.as_view(), name="devices"),
    path("logs/", views.LogsView.as_view(), name="logs"),
    path("assign/device/", views.AssignDeviceView.as_view(), name="assign_device"),
    path("return/device/", views.ReturnDeviceView.as_view(), name="return_device")
]