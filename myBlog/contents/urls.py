from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^feed/$',
        view=views.Contents.as_view(),
        name='feed',
    ),
] 