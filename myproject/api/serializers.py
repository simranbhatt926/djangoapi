from api.models import Company,Employee
from rest_framework import serializers
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        # queryset = Employee.objects.all()
        fields="__all__"
        
