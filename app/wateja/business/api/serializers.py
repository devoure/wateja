from rest_framework import serializers
from business.models import Business, Category
from django_countries.serializer_fields import CountryField


# Serializer class to serializer foreign key field in Business model
class BusinessCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


# Serializer class to serialize Category Model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    # country_dict=True, provides a more verbose output
    location = CountryField(country_dict=True)
    category = BusinessCategorySerializer()

    class Meta:
        model = Business
        fields = '__all__'

    # Method called ny SerializerMethodField()
    def get_age(self, obj):
        # Get the age property in the model object
        return obj.age

    # Override the create class to allow saving of nested relationship
    # The default create does not support saving nested relatioship
    def create(self, validated_data):
        try:
            # Get the category field from the validated_data
            category = validated_data.pop('category')
            # Get the name of category passed by user
            category_name = category["name"]

            # Get object from Category model
            category_obj = Category.objects.get(name=category_name)

            # Create the business object by passing the category_obj separately
            new_business = Business.objects.create(category=category_obj,
                                                   **validated_data)

            return new_business
        except Exception as e:
            raise serializers.ValidationError(str(e))
