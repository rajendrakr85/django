from rest_framework import serializers
from firstapp.models import Employee

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'sal']