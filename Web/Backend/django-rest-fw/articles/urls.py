from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', views.AriticleViewSet, basename='article')

app_name = 'articles'
urlpatterns = [
    # path('', views.AriticleListView.as_view()),
    path('', include(router.urls)),
]