from rest_framework import serializers
from .models import Shift


class ShiftSerializer(serializers.ModelSerializer):

    id = serializers.CharField()
    volunteer = serializers.StringRelatedField()

    class Meta:
        model = Shift
        fields = ('id', 'volunteer', 'start_time', 'end_time', )