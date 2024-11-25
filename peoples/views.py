from drf_spectacular.utils import (extend_schema_view, extend_schema,
                                   OpenApiParameter)
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
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
        depth = request.GET.get('depth')
        depth = int(depth) if depth is not None else None

        def get_ancestors(person, depth):
            if not person:
                return None

            data = {
                "id": person.id,
                "first_name": person.first_name,
                "last_name": person.last_name,
            }

            if depth is None or depth > 0:
                next_depth = depth - 1 if depth is not None else None

                mother = person.mother_id
                father = person.father_id

                if mother:
                    data["mother"] = get_ancestors(mother, next_depth)
                if father:
                    data["father"] = get_ancestors(father, next_depth)

            return data

        person = get_object_or_404(self.queryset, pk=person_id)
        ancestors = get_ancestors(person, depth)
        return Response(ancestors)
