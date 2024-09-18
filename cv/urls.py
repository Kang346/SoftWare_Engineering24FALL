from . import views
from django.urls import path

app_name = 'cv'
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:cv_id>/", views.detail, name='detail'),
]