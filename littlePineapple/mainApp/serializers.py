from rest_framework import serializers
from .models import Skillers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skillers
        fields = ('id', 'first_name', 'last_name', 'email', 'special_skill', 'skill_decs', 'tags')

