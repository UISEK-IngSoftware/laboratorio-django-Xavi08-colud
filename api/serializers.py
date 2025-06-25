from rest_framework import serializers
from pokedex.models import Pokemon
import base64
from django.core.files.base import ContentFile 

class PokemonSerializer(serializers.ModelSerializer):
    picture = serializers.CharField(required=True, allow_blank=False)
    
    class Meta:
        model = Pokemon
        fields = '__all__'
        
    def validate_picture(self, value):
        if value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile(
                    base64.b64decode(imgstr),
                    name=f'tem.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("Imagen no valida")
        return None