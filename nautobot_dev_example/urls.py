"""Django urlpatterns declaration for nautobot_dev_example app."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView
from nautobot.apps.urls import NautobotUIViewSetRouter

from nautobot_dev_example import views

app_name = "nautobot_dev_example"
router = NautobotUIViewSetRouter()

<<<<<<< HEAD
router.register("dev-examples", views.DevExampleUIViewSet)
=======
router.register("devexample", views.DevExampleUIViewSet)
>>>>>>> 36193f9 (Cookie updated by NetworkToCode Cookie Drift Manager Tool)


urlpatterns = [
    path("docs/", RedirectView.as_view(url=static("nautobot_dev_example/docs/index.html")), name="docs"),
]

urlpatterns += router.urls
