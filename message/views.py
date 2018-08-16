from .models import Message
from .serializers import MessageSerializer
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView
)

# Create your views here.

class MessageListAPIView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageCreateAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
