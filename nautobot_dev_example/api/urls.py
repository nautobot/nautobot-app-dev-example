"""Django API urlpatterns declaration for nautobot_dev_example app."""

from nautobot.apps.api import OrderedDefaultRouter

from nautobot_dev_example.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("dev-examples", views.DevExampleViewSet)

app_name = "nautobot_dev_example-api"
urlpatterns = router.urls
