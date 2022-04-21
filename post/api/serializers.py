from rest_framework import serializers
from post.models import Post


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['user', 'title', 'content', 'image']
