from django.conf.urls import url
from .views import (
    ProfileDetail
)

urlpatterns = [
	url(r'^(?P<username>[\w-]+)/$', ProfileDetail.as_view(),name="detail"),
]
