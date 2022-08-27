from django.urls import path

from . import views

app_name = 'manager'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("entity/<int:entity_id>/", views.entityDetail, name="entity"),
    path("entity/<int:entity_id>/project/<int:project_id>/", views.projectDetail, name="project")
]