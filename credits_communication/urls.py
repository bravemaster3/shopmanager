from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, VenteViewSet, ApprovisionnementViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename="Liste articles cc")
router.register('ventes', VenteViewSet, basename="Liste ventes cc")
router.register('Approvisionnements', ApprovisionnementViewSet, basename="Liste approvisionnements cc")
urlpatterns = router.urls