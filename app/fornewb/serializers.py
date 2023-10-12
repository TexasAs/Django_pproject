from rest_framework.serializers import ModelSerializer

from .models import Fornewb


class FornewbSerializers(ModelSerializer):
    class Meta:
        model = Fornewb
        fields = ['article_title', 'slug', 'content', 'photo', 'is_published', 'cat']