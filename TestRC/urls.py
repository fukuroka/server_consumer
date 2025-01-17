# Первые ссылки
from rest_framework.routers import DefaultRouter
from TestRC import views


router = DefaultRouter()
router.register('home', views.HomePageView, basename='home')
urlpatterns = router.urls