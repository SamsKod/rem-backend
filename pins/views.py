from rest_framework import generics, permissions
from .models import Pin
from .serializers import PinSerializer
from drf_api.permissions import IsOwnerOrReadOnly

    """
    List pins or pin if logged in
    """


class PinList(generics.ListCreateAPIView):
    serializer_class = PinSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Pin.objects.all()

    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)



class PinDetail(generics.RetrieveDestroyAPIView):
    serializer_class = PinSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Pin.objects.all()