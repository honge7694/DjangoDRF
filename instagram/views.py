from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def dispatch(self, request, *args, **kwargs): # request와 response 사이의 중개자 역할, HTTP 메서드 파악한다.
    #     print("request.body : ", request.body) # print 비추, logger 추천
    #     print("request.POST : ", request.POST)
        
    #     return super().dispatch(request, *args, **kwargs)





