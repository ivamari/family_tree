from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from peoples.models import People
from peoples.serializers import PeopleSerializer


class PeopleView(GenericViewSet, mixins.RetrieveModelMixin,
                 mixins.ListModelMixin, mixins.CreateModelMixin,
                 mixins.UpdateModelMixin):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    http_method_names = ('get', 'post', 'put',)
    lookup_url_kwarg = 'person_id'
