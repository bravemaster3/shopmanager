from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, VenteViewSet, ApprovisionnementViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename="Liste articles")
router.register('ventes', VenteViewSet, basename="Liste ventes")
router.register('Approvisionnements', ApprovisionnementViewSet, basename="Liste approvisionnements")
urlpatterns = router.urls