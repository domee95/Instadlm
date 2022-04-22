from rest_framework.routers import SimpleRouter

from followers.views import FollowingViewSet, FollowViewSet

router = SimpleRouter()
router.register('following', FollowingViewSet, basename='following')
router.register('follow', FollowViewSet,)
# no se pone basename xq el FollowingSet tiene queryset y automaticamnete el routert lo da con relationship
urlpatterns = router.urls