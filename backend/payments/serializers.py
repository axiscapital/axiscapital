
from rest_framework import serializers
from .models import Deposit
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('id', 'amount_usdt', 'status', 'invoice_id', 'created_at')
        read_only_fields = ('status', 'invoice_id', 'created_at')
