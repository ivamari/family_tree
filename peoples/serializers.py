from rest_framework import serializers

from peoples.models import People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = (
            'id',
            'first_name',
            'last_name',
            'mother_id',
            'father_id',
        )
