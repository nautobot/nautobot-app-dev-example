"""Django API urlpatterns declaration for my_plugin plugin."""

from nautobot.core.api import OrderedDefaultRouter

from my_plugin.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("devexample", views.DevExampleViewSet)


app_name = "my_plugin-api"
urlpatterns = router.urls
