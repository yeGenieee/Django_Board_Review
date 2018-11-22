from django.urls import path, re_path
from .views import PostLV, PostDV, PostAV, PostYAV, PostMAV, PostDAV, PostTAV

urlpatterns = [

    # ex) /blog/
    path('', PostLV.as_view(), name='index'),

    # ex) /blog/post/
    path('post/', PostLV.as_view(), name='post_list'),

    # ex) /blog/post/django-example/
    path('post/<slug:slug>/', PostDV.as_view(), name='post_detail'),

    # ex) /blog/archive/
    path('archive/', PostAV.as_view(), name='post_archive'),

    # ex) /blog/2012/
    re_path(r'^(?P<year>\d{4})/', PostYAV.as_view(), name='post_year_archive'),

    # ex) /blog/2012/nov/
    re_path(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archivce'),

    # ex) /blog/2012/nov/10/
    re_path(r'^(?P<year>\d{4})/(?P<month>[a-z]{3}/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    # ex) /blog/today/
    path('today/', PostTAV.as_view(), name='post_today_archive'),
]