from django.urls import path, include
from rest_framework.routers import DefaultRouter

from peoples.views import PeopleView

router_people = DefaultRouter()

router_people.register(r'', PeopleView, 'people')

urlpatterns = [
    path('people/', include(router_people.urls)),
]
