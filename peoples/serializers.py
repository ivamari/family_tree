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


class AncestorSerializer(serializers.ModelSerializer):
    mother = serializers.SerializerMethodField()
    father = serializers.SerializerMethodField()

    class Meta:
        model = People
        fields = ('id',
                  'first_name',
                  'last_name',
                  'mother', 'father')

    def get_mother(self, obj):
        return AncestorSerializer(obj.mother_id).data if obj.mother else None

    def get_father(self, obj):
        return AncestorSerializer(obj.father_id).data if obj.father else None
