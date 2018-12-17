from rest_framework import serializers
from .models import Member


#member serializer
class MemberSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Member
        fields = '__all__'
