from rest_framework import serializers
from base.models import Transaction
import uuid

""" 
The Transaction Serializer
Prepares the interaction between the Transaction Model 
and the REST API
"""
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'status', 'transaction_blob']

    def update(self, instance, validated_data):
        instance.save()
        return instance

