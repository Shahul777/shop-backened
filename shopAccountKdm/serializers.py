from dataclasses import fields
from rest_framework import serializers
from shopAccountKdm.models import AccountExpenses,LabourExpenses,RateSheet

class AccountExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountExpenses
        fields= '__all__'
class LabourExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabourExpenses
        fields = '__all__'

class RateSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model=RateSheet
        fields = '__all__'