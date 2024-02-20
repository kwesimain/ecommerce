from django.conf import settings
from rest_framework import views, status, permissions
from rest_framework.response import Response
import stripe

class CreateChargeView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            charge = stripe.Charge.create(
                amount=int(request.data.get("amount") * 100),  # Amount in cents
                currency="usd",
                source=request.data.get("token"),  # Obtained from Stripe Checkout or Elements
                description="Charge for order",
            )
            return Response({"message": "Charge successful", "data": charge})
        except stripe.error.StripeError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)