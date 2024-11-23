from django.urls import path, include
from rest_framework.routers import DefaultRouter

from peoples.views import PeopleView, AncestorView

router_v1 = DefaultRouter()

router_v1.register(r'', PeopleView, 'hotels')
router_v1.register(r'people', AncestorView, basename='people')

urlpatterns = [
    path('hotels/', include(router_v1.urls)),
]
