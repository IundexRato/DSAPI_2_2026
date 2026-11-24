from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PecaViewSet

router = DefaultRouter()
router.register(r'pecas', PecaViewSet, basename='peca')

urlpatterns = [
    path('', include(router.urls)),
]