from rest_framework import serializers
from land.models import Land, Feature


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name']


class LandSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True)

    class Meta:
        model = Land
        fields = [
            'lat', 'long', 'address', 'province', 'city', 'areaOfBuilding', 'areaOfLand', 'electricityAmper',
            'edari', 'buildingHeight', 'phoneNumber', 'secondaryPhoneNumber', 'ownerName',
            'image', 'features', 'privetNote'
        ]

    def create(self, validated_data):
        features_data = validated_data.pop('features')
        land = Land.objects.create(**validated_data)
        for feature_data in features_data:
            feature, created = Feature.objects.get_or_create(**feature_data)
            land.features.add(feature)
        return land

    def update(self, instance, validated_data):
        features_data = validated_data.pop('features')
        instance.features.clear()
        for feature_data in features_data:
            feature, created = Feature.objects.get_or_create(**feature_data)
            instance.features.add(feature)
        return super().update(instance, validated_data)
