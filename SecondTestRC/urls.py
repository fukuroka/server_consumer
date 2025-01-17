# Вторые ссылки
from rest_framework.routers import DefaultRouter
from SecondTestRC import views


router = DefaultRouter()
router.register('second_home', views.SecondHomePageView, basename='second_home')
urlpatterns = router.urls