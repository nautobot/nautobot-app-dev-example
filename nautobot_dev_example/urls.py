"""Django urlpatterns declaration for nautobot_dev_example plugin."""

from django.urls import path
from nautobot.extras.views import ObjectChangeLogView

from nautobot_dev_example import models
from nautobot_dev_example.views import devexample

urlpatterns = [
    # DevExample URLs
    path("devexample/", devexample.DevExampleListView.as_view(), name="devexample_list"),
    # Order is important for these URLs to work (add/delete/edit) to be before any that require uuid/slug
    path("devexample/add/", devexample.DevExampleCreateView.as_view(), name="devexample_add"),
    path("devexample/delete/", devexample.DevExampleBulkDeleteView.as_view(), name="devexample_bulk_delete"),
    path("devexample/edit/", devexample.DevExampleBulkEditView.as_view(), name="devexample_bulk_edit"),
    path("devexample/<slug:slug>/", devexample.DevExampleView.as_view(), name="devexample"),
    path("devexample/<slug:slug>/delete/", devexample.DevExampleDeleteView.as_view(), name="devexample_delete"),
    path("devexample/<slug:slug>/edit/", devexample.DevExampleEditView.as_view(), name="devexample_edit"),
    path(
        "devexample/<slug:slug>/changelog/",
        ObjectChangeLogView.as_view(),
        name="devexample_changelog",
        kwargs={"model": models.DevExample},
    ),
]
