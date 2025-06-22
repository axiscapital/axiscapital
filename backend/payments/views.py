
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.conf import settings
from .models import Deposit
from .serializers import DepositSerializer
from .utils import create_binance_order
class CreateDepositView(generics.CreateAPIView):
    serializer_class = DepositSerializer
    permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        amount = request.data.get('amount_usdt')
        deposit = Deposit.objects.create(user=request.user, amount_usdt=amount)
        try:
            result = create_binance_order(
                amount,
                settings.BINANCE_API_KEY,
                settings.BINANCE_API_SECRET,
                settings.BINANCE_CERT_SN
            )
            deposit.invoice_id = result['data']['prepayId']
            deposit.save()
            return Response({'checkoutUrl': result['data']['checkoutUrl']}, status=status.HTTP_201_CREATED)
        except Exception as e:
            deposit.status = Deposit.FAILED
            deposit.save()
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
