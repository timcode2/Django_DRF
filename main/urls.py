from main.apps import MainConfig
from rest_framework.routers import DefaultRouter

from main.views import CourseViewSet

app_name = MainConfig.name


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [

] + router.urls
