from rest_framework import viewsets
from .serializer import FacturaSerializer
from .models import Factura

# Create your views here.

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
