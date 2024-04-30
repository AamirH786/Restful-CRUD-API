from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import EmployeeSerializer
from .models import Employee

# Create your views here.

# Get And Post Method Defined Here
@api_view(['GET', 'POST'])
def GetEmployeeDetails(request):
    if request.method == 'GET':
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Unsupported request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

#GET, PUT, PATCH, AND DELETE Method Is Here By Spesific Id
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def GetEditDel(request, id=None):
    #Trying To Get Data By Id If Id Not Matches Simply It Will Show Show Bad Request
    try:
        emp = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #For GET Method Function 
    if request.method == 'GET':
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #For PUT Method To Update Data
    if request.method == 'PUT':
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #For PATCH Method To Update Data
    if request.method == 'PATCH':
        serializer = EmployeeSerializer(emp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #For DELETE Method To Update Data
    if request.method == 'DELETE':
       emp.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)