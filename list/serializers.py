from rest_framework import serializers
from . models import employees
#noinspection PyUnresolvedReferences
from rest_framework.serializers import HyperlinkedIdentityField,HyperlinkedModelSerializer
class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model=employees
        fields=('firstname','emp_id')

class employeeSerializer(serializers.ModelSerializer):
    firstname = serializers.HyperlinkedRelatedField(many=True,view_name='employees-detail',read_only=True)
    # specify model and fields
    class Meta:
        model = employees
        fields = ('id','firstname','Email','phone_number','Designation','company_name')
        depth=2