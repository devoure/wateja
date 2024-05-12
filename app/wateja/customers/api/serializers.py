from rest_framework import serializers
from customers.models import Customer
from business.models import Business
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ["name", "id"]


class CustomerSerializer(serializers.ModelSerializer):
    # country_dict=True, provides a more verbose output
    nationality = CountryField(country_dict=True)
    business = BusinessSerializer()
    phone = PhoneNumberField()

    class Meta:
        model = Customer
        fields = '__all__'
    # Override the create class to allow saving of nested relationship
    # The default create does not support saving nested relatioship

    def create(self, validated_data):
        try:
            # Get the business field from the validated_data
            business = validated_data.pop('business')
            # Get the name of business passed by user
            business_name = business["name"]

            # Get object from Business model
            business_obj = Business.objects.get(name=business_name)

            # Create the customer object by passing the business_obj separately
            new_customer = Customer.objects.create(business=business_obj,
                                                   **validated_data)

            return new_customer
        except Exception as e:
            raise serializers.ValidationError(str(e))
