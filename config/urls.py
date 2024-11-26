from typing import List

from django.contrib import admin
from django.urls import URLResolver, path

from apps.messenger.views import MessageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MessageView.as_view())
]
