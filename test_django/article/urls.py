from rest_framework.routers import DefaultRouter
from .views import ArticleView

router = DefaultRouter()
router.register(r'articles', ArticleView, basename='user')

urlpatterns = router.urls
