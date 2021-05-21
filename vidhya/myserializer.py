from rest_framework.serializers import ModelSerializer
from vidhya.models import Vidhya
class EmpToJson(ModelSerializer):
    class Meta:
        model=Vidhya
        fields='__all__'