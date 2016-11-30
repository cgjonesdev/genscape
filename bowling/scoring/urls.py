from django.conf.urls import url, include
from scoring import views
from rest_framework.routers import DefaultRouter

# # Create a router and register our viewsets with it.
router = DefaultRouter(schema_title='Bowling Scoring API')
router.register(r'players', views.PlayerViewSet)

urlpatterns = [
    url(r'^players/(?P<pk>[0-9]+)/bowl/$', views.PlayerBowl.as_view()),
    url(r'^', include(router.urls))]
