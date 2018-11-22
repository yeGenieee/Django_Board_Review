from django.urls import path

from .views import BookmarkLV, BookmarkDV

urlpatterns = [
    # Class Based Views

    # ex) /bookmark/
    path('', BookmarkLV.as_view(), name='index'),

    # ex) /bookmark/5/
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
]