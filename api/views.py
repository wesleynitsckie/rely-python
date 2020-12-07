from django.http import HttpResponse, JsonResponse
from base.models import Transaction
from .serializers import TransactionSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def transaction_list(request):
    if request.method == 'GET':
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        blob = {
                "first_name": data["first_name"],
                "last_name" : data["last_name"],
                "income": data["income"],
                "dob": data["dob"],
            }
        res = {
            'transaction_blob' : json.dumps(blob)
        }
        serializer = TransactionSerializer(data=res)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def confirm_sanction(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        transaction = Transaction.objects.get(id=data["id"])
        if data['confirm'] == True:
            status = Transaction.Status.DENIED
        else:
            status = Transaction.Status.PEPCHECK
        transaction.status = status
        transaction.save()
        serializer = TransactionSerializer(transaction)
        return JsonResponse(serializer.data, safe = False)
    else:
        return JsonResponse({'msg': 'Method not Allowed'}, status=400)

@csrf_exempt
def check_status(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        transaction = Transaction.objects.get(id=data["id"])
        serializer = TransactionSerializer(transaction)
        return JsonResponse(serializer.data, safe = False)
    else:
        return JsonResponse({'msg': 'Method not Allowed'}, status=400)

@csrf_exempt
def confirm_pep(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        transaction = Transaction.objects.get(id=data["id"])
        transaction.confirm_on_pep_list = data['confirm']
        transaction.status = Transaction.Status.ASSESSMENT
        transaction.save()
        serializer = TransactionSerializer(transaction)
        return JsonResponse(serializer.data, safe = False)
    else:
        return JsonResponse({'msg': 'Method not Allowed'}, status=400)