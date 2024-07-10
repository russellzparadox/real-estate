from rest_framework import serializers
from .models import Case
from land.models import Land, Feature
from land.serializers import LandSerializer
from iranian_cities.models import Shahr, Ostan


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Shahr
        fields = "__all__"


class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ostan
        fields = "__all__"


class CaseSerializer(serializers.ModelSerializer):
    land = LandSerializer()

    class Meta:
        model = Case
        fields = ['id', 'title', 'land', 'content', 'sellPrice', 'rentPrice']
        # optional_fields = ['features']

    def create(self, validated_data):
        print("hello")
        land_data = validated_data.pop('land')
        features_data = land_data.pop('features')
        land = Land.objects.create(**land_data)
        for feature_data in features_data:
            feature, created = Feature.objects.get_or_create(**feature_data)
            land.features.add(feature)
        case = Case.objects.create(land=land, **validated_data)
        return case

    def update(self, instance, validated_data):
        land_data = validated_data.pop('land', None)
        if land_data:
            features_data = land_data.pop('features', None)
            if features_data is not None:
                instance.land.features.clear()
                for feature_data in features_data:
                    feature, created = Feature.objects.get_or_create(**feature_data)
                    instance.land.features.add(feature)
            for attr, value in land_data.items():
                setattr(instance.land, attr, value)
            instance.land.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
