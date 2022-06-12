import imp

from attr import fields
from .models import *
from rest_framework import Serializers

class DonnaUser(Serializers.ModelSerializers):
    class META:
        model = DonnaUsers
        fields = '__all__'

