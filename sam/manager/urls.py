from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "manager"
urlpatterns = [
    path("", views.EntityListView.as_view(), name="index"),
    path("entity/<int:pk>/", views.EntityDetailView.as_view(), name="entity"),
    path(
        "entity/project/<int:pk>/",
        views.ProjectView.as_view(),
        name="project",
    ),
    path("action/<str:action>/<int:doc_id>/", views.ActionView.as_view(), name="perform-action"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
