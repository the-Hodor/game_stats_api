from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, ReviewViewset

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Games API",
      default_version='v1',
      description="API для игр и отзывов",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'reviews', ReviewViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]