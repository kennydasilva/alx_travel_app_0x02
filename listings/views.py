from rest_framework import viewsets
from .models import Listing, Booking, Review, Payment
from .serializers import ListingSerializer, BookingSerializer, ReviewSerializer
import uuid
import requests
from django.conf import settings 
from django.http import JsonResponse
from django.views.decorators.csrf import crsf_exempt

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@crsf_exempt
def initiate_payment(request):
    if request.method !="Post":
        return JsonResponse({"error": "Invalid method"}, status=405)
    
    booking_reference = request.Post.get("booking_reference")
    amount = request.Post.get("amount")
    email=request.Post.get("email")

    tx_ref=str(uuid.uuid4())

    payload={
        "amount":amount,
        "currency": "ETB",
        "email": email,
        "tx_ref":tx_ref,
        "return_url": "http://localhost:8000/payment-sucess"

    }

    headers={
        "Authorization": f"Bearer {settingd.CHAPA_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    response = request.post(
        f"{settings.CHAPA_BASE_URL}/transactiom/initialize",
        json=payload,
        headers=headers
    )

    data=response.json()

    if response.status_code ==200:
        Payment.objects.create(
            booking_reference=booking_reference,
            amount=amount,
            transaction_id=tx_ref,
            status="PENDING"
        )
        return JsonResponse({"payment_url": data["data"]["checkout_url"]})
    
    return JsomResponse(data, status=400)