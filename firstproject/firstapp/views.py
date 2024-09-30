from django.http import JsonResponse
from django.shortcuts import render
from firstapp.models import Employee
from firstapp.serializers import EmployeeSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method =='GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializers(employees, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_details(request, pk):
    try:
        employee = Employee.objects.get(pk = pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializers(employee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmployeeSerializers(employee, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



# Create your views here.
# def employeeView(request):
#     emp = {
#         'id':123,
#         'name':'john',
#         'sal':100000,
#         'post':'developer'
#     }

#     data = Employee.objects.all();

#     response = {'employees': list(data.values('name', 'sal'))}

#     return JsonResponse(response)