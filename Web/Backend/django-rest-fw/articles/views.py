from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleListSerializer

class AriticleListView(ListAPIView):
    '''
    하나의 기능을 명시적으로 하고 싶을 때 사용
    '''
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    # permission_classes = []  # 조건에 따른 분기 / 로그인, 같은 계정 등등..


class AriticleViewSet(ModelViewSet):
    '''
    기본경로/                           : list(GET), create(POST) 
    기본경로/lookup_field(기본값 : pk)   : retrieve(GET), update(PUT), destroy(DELETE)
    '''
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    lookup_field = 'pk'  # 하나만 조회 할때 키값
    # permission_classes = []

