from drf_spectacular.utils import (extend_schema_view, extend_schema,
                                   OpenApiParameter)
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from peoples.models import People
from peoples.serializers import PeopleSerializer, AncestorSerializer


@extend_schema_view(
    retrieve=extend_schema(summary='Деталка человека',
                           tags=['Люди']),
    list=extend_schema(summary='Список людей', tags=['Люди']),
    create=extend_schema(summary='Добавить человека',
                         tags=['Люди']),
    update=extend_schema(summary='Изменить параметры',
                                 tags=['Люди']),
)
class PeopleView(GenericViewSet, mixins.RetrieveModelMixin,
                 mixins.ListModelMixin, mixins.CreateModelMixin,
                 mixins.UpdateModelMixin):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    http_method_names = ('get', 'post', 'put', )
    lookup_url_kwarg = 'person_id'


@extend_schema_view(
    retrieve=extend_schema(
        summary='Родословная',
        tags=['Родословная'],
        parameters=[
            OpenApiParameter(
                name='depth',
                description='Количество поколений для получения родословной',
                required=False,
                type=int,
                location=OpenApiParameter.QUERY,
            )
        ],
    )
)
class AncestorView(GenericViewSet, mixins.RetrieveModelMixin):
    queryset = People.objects.all()
    serializer_class = AncestorSerializer

    def retrieve(self, request, *args, **kwargs):
        person_id = kwargs.get('person_id')
        depth = int(request.GET.get('depth', 0))

        def get_ancestors(person, depth):
            if depth == 0 or not person:
                return None

            data = {
                "id": person.id,
                "first_name": person.first_name,
                "last_name": person.last_name,
            }

            if depth > 1:
                data["mother"] = get_ancestors(person.mother_id, depth - 1)
                data["father"] = get_ancestors(person.father_id, depth - 1)
            else:
                data["mother"] = {
                    "id": person.mother_id.id,
                    "first_name": person.mother_id.first_name,
                    "last_name": person.mother_id.last_name,
                } if person.mother_id else None
                data["father"] = {
                    "id": person.father_id.id,
                    "first_name": person.father_id.first_name,
                    "last_name": person.father_id.last_name,
                } if person.father_id else None

            return data

        person = get_object_or_404(self.queryset, pk=person_id)
        ancestors = get_ancestors(person, depth)
        return Response(ancestors)
