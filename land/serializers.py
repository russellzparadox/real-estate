from rest_framework import serializers
from land.models import Land, Feature, Status, TypeOfPropertyUse


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TypeOfPropertyUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfPropertyUse
        fields = '__all__'


class LandSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True)

    class Meta:
        model = Land
        fields = [
            'lat', 'long', 'address', 'province', 'city', 'areaOfBuilding', 'areaOfLand', 'electricityAmper',
            'edari', 'buildingHeight', 'phoneNumber', 'secondaryPhoneNumber', 'ownerName',
            'image', 'features', 'privetNote', 'status', 'typeOfPropertyUse'
        ]

    def create(self, validated_data):
        features_data = validated_data.pop('features')
        status_data = validated_data.pop('status')
        type_of_property_use_data = validated_data.pop('typeOfPropertyUse')
        status = Status.objects.get(name=status_data)
        type_of_property_use = TypeOfPropertyUse.objects.get(name=type_of_property_use_data)
        land = Land.objects.create(typeOfPropertyUse=type_of_property_use, status=status, **validated_data)
        for feature_data in features_data:
            feature, created = Feature.objects.get_or_create(**feature_data)
            land.features.add(feature)
        return land

    def update(self, instance, validated_data):
        features_data = validated_data.pop('features')
        status_data = validated_data.pop('status')
        type_of_property_use_data = validated_data.pop('typeOfPropertyUse')
        status = Status.objects.get(name=status_data)
        type_of_property_use = TypeOfPropertyUse.objects.get(name=type_of_property_use_data)
        instance.status = status
        instance.typeOfPropertyUse = type_of_property_use
        instance.features.clear()
        for feature_data in features_data:
            feature, created = Feature.objects.get_or_create(**feature_data)
            instance.features.add(feature)
        return super().update(instance, validated_data)
