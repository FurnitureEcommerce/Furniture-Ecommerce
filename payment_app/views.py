import razorpay
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentCreateSerializer, PaymentVerifySerializer

# Razorpay Test Keys
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

class CreateDummyPaymentAPIView(APIView):
    def post(self, request):
        serializer = PaymentCreateSerializer(data=request.data)
        if serializer.is_valid():
            payment = serializer.save()
            amount_paise = int(payment.amount * 100)

            razorpay_order = client.order.create({
                'amount': amount_paise,
                'currency': 'INR',
                'payment_capture': 1
            })

            payment.razorpay_order_id = razorpay_order['id']
            payment.save()

            return Response({
                'payment_id': payment.id,
                'order_id': razorpay_order['id'],
                'razorpay_key': settings.RAZORPAY_KEY_ID,
                'amount': amount_paise,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyDummyPaymentAPIView(APIView):
    def post(self, request):
        serializer = PaymentVerifySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                # Verify signature
                client.utility.verify_payment_signature({
                    'razorpay_order_id': data['razorpay_order_id'],
                    'razorpay_payment_id': data['razorpay_payment_id'],
                    'razorpay_signature': data['razorpay_signature'],
                })

                # Update payment record
                payment = Payment.objects.get(razorpay_order_id=data['razorpay_order_id'])
                payment.razorpay_payment_id = data['razorpay_payment_id']
                payment.razorpay_signature = data['razorpay_signature']
                payment.paid = True
                payment.save()

                return Response({"message": "Payment verified successfully."})
            except razorpay.errors.SignatureVerificationError:
                return Response({"error": "Signature verification failed."}, status=400)

        return Response(serializer.errors, status=400)
