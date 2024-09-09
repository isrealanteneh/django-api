from rest_framework import serializers
from .models import Orga_Structure


class Orga_srializer(serializers.ModelSerializer):
    class Meta:
        model = Orga_Structure
        fields = "__all__"