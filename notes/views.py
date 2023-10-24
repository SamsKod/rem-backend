from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Note
from .serializers import NoteSerializer


class NotesList(generics.ListCreateAPIView):
   
    queryset = Note.objects.annotate(
        comments_count=Count('comment', distinct=True),
        pins_count=Count('pins', distinct=True),
    ).order_by('-created_at')
    serializer_class = NoteSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'pins__owner__profile',
        'owner__profile',
    ]
    
    ordering_fields = [
        'comments_count',
        'pins_count',
        'pins__created_at'
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
   
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Note.objects.annotate(
        comments_count=Count('comment', distinct=True),
        pins_count=Count('pins', distinct=True),
    ).order_by('-created_at')
    serializer_class = NoteSerializer