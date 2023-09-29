from .models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields= ('id','name','genre','year','image','director','country')
