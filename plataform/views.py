from rest_framework import viewsets
from .models import Member
from .serializers import (
    MemberSerializer,
)


class MemberView(viewsets.ModelViewSet):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
