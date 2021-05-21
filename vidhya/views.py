from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
#from rest_framework.viewsets import GenericViewSet
#from rest_framework.mixins import DestroyModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin
from vidhya.models import Vidhya
from vidhya.myserializer import EmpToJson
# Create your views here.
class MyOwnMixin(ModelViewSet):
    #model=Vidhya
    #fields='__all__'
    queryset = Vidhya.objects.all()
    serializer_class = EmpToJson


def login(req):
    return render(request=req, template_name='login.html')