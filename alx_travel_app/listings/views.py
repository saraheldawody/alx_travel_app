from rest_framework import generics
from .models import Listing
from .serializers import ListingSerializer

class ListingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer