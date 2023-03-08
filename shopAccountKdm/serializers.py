from dataclasses import fields
from rest_framework import serializers
from shopAccountKdm.models import AccountExpenses,LabourExpenses,RateSheet,MonthlyEntryKdm,CombinedEntry

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

class MonthlyEntryKdmSerializer(serializers.ModelSerializer):
    class Meta:
        model=MonthlyEntryKdm
        fields = '__all__'

class CombinedEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model=CombinedEntry
        fields = '__all__'