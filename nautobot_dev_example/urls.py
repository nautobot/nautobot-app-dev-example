"""Django urlpatterns declaration for nautobot_dev_example app."""

from nautobot.apps.urls import NautobotUIViewSetRouter

from nautobot_dev_example import views

router = NautobotUIViewSetRouter()
router.register("devexample", views.DevExampleUIViewSet)

urlpatterns = router.urls
