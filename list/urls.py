#noinspection PyUnresolvedReferences
from django.contrib import admin
from django.urls import path,include
#noinspection PyUnresolvedReferences
from rest_framework.urlpatterns import format_suffix_patterns
#noinspection PyUnresolvedReferences
from .views import employeeList,EmployeeViewset
from list import views
#noinspection PyUnresolvedReferences
from rest_framework import routers
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register('list',EmployeeViewset,basename='list')

urlpatterns = [
path('viewset/', include(router.urls)),
    path('employees/',views.employeeList.as_view()),
   # path('generic/employees/',views.EmployeeListt.as_view(),name='employees-detail'),
]