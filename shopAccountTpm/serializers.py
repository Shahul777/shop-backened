from dataclasses import fields
from rest_framework import serializers
from shopAccountTpm.models import AccountExpenses,LabourExpenses,MonthlyEntryTpm

class AccountExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountExpenses
        fields= '__all__'
class LabourExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabourExpenses
        fields = '__all__'

class MonthlyEntryTpmSerializer(serializers.ModelSerializer):
    class Meta:
        model=MonthlyEntryTpm
        fields = '__all__'