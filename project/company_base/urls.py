from django.urls import path
from . import views

app_name = 'company_base'

urlpatterns = [
    path('', views.EmployeesList.as_view(), name ='index'),
    path('department/<int:id>', views.EmployeesList.as_view(), name ='department'),
    path('working/<int:number>', views.EmployeesList.as_view(), name ='is_working'),
    path('employee/<int:pk>', views.EmployeeDetail.as_view(), name ='employee'),
    path('alpha', views.EmployeesAlphaList.as_view(), name ='alpha'),
    path('alpha/<str:group>', views.EmployeesAlphaList.as_view(), name ='groups'),
]