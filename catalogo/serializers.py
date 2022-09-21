#Creamos clases para poder utilizar los serializadores en las vistas

from rest_framework import serializers
from .models import Coche

#Serializador del modelo Coche
class CocheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coche
        fields = '__all__'


