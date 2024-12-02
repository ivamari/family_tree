from django.urls import path, include
from rest_framework.routers import DefaultRouter

from peoples.views import PeopleView, AncestorView

router_people = DefaultRouter()

router_people.register(r'', PeopleView, 'people')

urlpatterns = [
    path('people/', include(router_people.urls)),
    path('people/<int:person_id>/ancestors/',
         AncestorView.as_view({'get': 'retrieve'})),
]
