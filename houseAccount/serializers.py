from dataclasses import fields
from rest_framework import serializers
from houseAccount.models import AccountExpenses,RateSheet

class AccountExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountExpenses
        fields= '__all__'

class RateSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model=RateSheet
        fields = '__all__'