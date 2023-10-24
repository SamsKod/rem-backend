from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
   
    queryset = Profile.objects.annotate(
        notes_count=Count('owner__note', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    ordering_fields = [
        'notes_count',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
   
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        notes_count=Count('owner__note', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer    