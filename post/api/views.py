from rest_framework.response import Response
from rest_framework.views import APIView

from post.api.serializers import PostSerializer
from post.models import Post


class PostAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializers = PostSerializer(qs, many= True)
        return  Response(serializers.data)


