#noinspection PyUnresolvedReferences
from django.shortcuts import render
# Create your views here.
#noinspection PyUnresolvedReferences
from django.http import HttpResponse
#noinspection PyUnresolvedReferences
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
#noinspection PyUnresolvedReferences
from rest_framework import status
from . models import employees
from . serializers import employeesSerializer,employeeSerializer
#noinspection PyUnresolvedReferences
from rest_framework import status, generics
#noinspection PyUnresolvedReferences
from rest_framework import viewsets
class employeeList(APIView):                    #url for API is: http://127.0.0.1:8000/api/employees/

    def get(self, request):
        employees1=employees.objects.all()
        serializer=employeesSerializer(employees1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class EmployeeViewset(viewsets.ViewSet):            #url fr API is: http://127.0.0.1:8000/api/viewset/
    def list(self,request):
        queryset=employees.objects.all()
        serializer=employeeSerializer(queryset,many=True,context={'request':request})
        return Response(serializer.data)

