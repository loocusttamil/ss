from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Relay
from .serializers import RelaySerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RelayStatusView(APIView):
    def get(self, request):
        relays = Relay.objects.all()
        serializer = RelaySerializer(relays, many=True)
        return Response(serializer.data)

    def post(self, request):
        relay_id = request.data.get("relay_id")
        status_value = request.data.get("status")
        relay, _ = Relay.objects.get_or_create(relay_id=relay_id)
        relay.status = status_value
        relay.save()
        return Response({"message": "Relay status updated"}, status=status.HTTP_200_OK)

@api_view(["POST"])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({"token": str(refresh.access_token)})
    return Response({"error": "Invalid credentials"}, status=401)
