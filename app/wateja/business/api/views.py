from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from business.models import Business, Category
from .serializers import BusinessSerializer, CategorySerializer

# Create your views here.


# Function to handle a GET Request to endpoint "http://wateja/v1/business/"
# Returns an overview of URLs in the endpoint root /wateja/v1/business/
@api_view(['GET'])
def index(request):
    api_list = {
            'Get Business List': '/business-list/',
            'Get Detailed View of a Business': '/business-detail/<str:uuid>/',
            'Create a new Business Object': '/business-create/',
            'Update a Business Object': '/business-update/<str:uuid>/',
            'Delete a Business Object': '/business-delete/<str:uuid>/',

            'Get Category List': '/business-cat-list/',
            'Get Detailed View of a Category': '/business-cat-detail/<str:uuid>/',
            'Create a new Business Category': '/business-cat-create/',
            'Update a Business Category Object': '/business-cat-update/<str:uuid>/',
            'Delete a Business Category Object': '/business-cat-delete/<str:uuid>/',

            }
    return Response(api_list)


# Function to handle a GET Request to endpoint "http://wateja/v1/business/business-list"
# Returns a list of businesses in the app
@api_view(['GET'])
def get_businesses(request):
    try:
        # use select_related on one to many relationship query to reduce number of queries to db
        businesses = Business.objects.select_related('category')
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)

    # Provide a 500 response incase of errors in the above code
    except Exception as e:
        return Response({'error': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Function to handle a GET Request to endpoint "http://wateja/v1/business/business-detail/uuid"
# Returns a detailed view of a particular business with uuid passed.
@api_view(['GET'])
def get_business_detail(request, uuid):
    try:
        # use select_related on one to many relationship query to reduce number of queries to db
        business = Business.objects.select_related('category').get(id=uuid)
        serializer = BusinessSerializer(business, many=False)

        # Add all customers in the business
        return Response(serializer.data)

    # Provide a 500 response incase of errors in the above code
    except Exception as e:
        return Response({'error': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Function to handle a POST Request to endpoint "http://wateja/v1/business/business-create/"
# This will create a business object
# Returns the new item added in the database
@api_view(['POST'])
def add_business(request):
    try:
        serializer = BusinessSerializer(data=request.data)

        # Check if serializers is valid, if valid save the new object
        if serializer.is_valid():
            serializer.save()
        else:
            # Else return the error
            errors = serializer.errors
            return Response(errors,
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.data)
    # Provide a 500 response incase of errors in the above code
    except Exception as e:
        return Response({'error': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Function to handle a POST Request to endpoint "http://wateja/v1/business/business-update/<uuid>"
# This will update a business object
# Returns the new item updated
@api_view(['POST'])
def update_business(request, uuid):
    try:
        business = Business.objects.get(id=uuid)
        serializer = BusinessSerializer(instance=business,
                                        data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
        else:
            errors = serializer.errors
            return Response(errors,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Function to handle a DELETE Request to endpoint "http://wateja/v1/business/business-delete/<uuid>"
# This will delete a business object
# Returns a 200 or 400 status
@api_view(['DELETE'])
def delete_business(request, uuid):
    try:
        business = Business.objects.get(id=uuid)
        business.delete()

        return Response({"message": 'Delete Success'},
                        status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


######################### CATEGOTY API ENDPOINTS #####################

# Function to handle a GET Request to endpoint "http://wateja/v1/business/business-cat-list"
# Returns a list of businesses categories in the app
@api_view(['GET'])
def get_business_categories(request):
    try:
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    # Provide a 500 response incase of errors in the above code
    except Exception as e:
        return Response({'error': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Function to handle a GET Request to endpoint "http://wateja/v1/business/business-cat-detail/uuid"
# Returns a detailed view of a particular category with uuid passed.
@api_view(['GET'])
def get_business_category_detail(request, uuid):
    try:
        category = Category.objects.get(id=uuid)
        serializer = CategorySerializer(category, many=False)

        # Add all business in the category

        businesses = Business.objects.filter(category=category.id).select_related("category")
        businesses_serializer = BusinessSerializer(businesses, many=True)
        return Response({"Category": serializer.data,
                         "Businesses": businesses_serializer.data})

    # Provide a 500 response incase of errors in the above code
    except Exception as e:
        return Response({'error': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Function to handle a POST Request to endpoint "http://wateja/v1/business/business-cat-create/"
# This will create a business category object
# Returns the new item added in the database
@api_view(['POST'])
def add_business_category(request):
    try:
        serializer = CategorySerializer(data=request.data)

        # Check if serializers is valid, if valid save the new object
        if serializer.is_valid():
            serializer.save()
        else:
            # Else return the error
            errors = serializer.errors
            return Response(errors,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.data)
    # Provide a 500 response incase of errors in the above code
    except Exception as e:
        return Response({'error': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Function to handle a POST Request to endpoint "http://wateja/v1/business/business-cat-update/<uuid>"
# This will update a business category object
# Returns the new item updated
@api_view(['POST'])
def update_business_category(request, uuid):
    try:
        category = Category.objects.get(id=uuid)
        serializer = CategorySerializer(instance=category,
                                        data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
        else:
            errors = serializer.errors
            return Response(errors,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Function to handle a DELETE Request to endpoint "http://wateja/v1/business/business-cat-delete/<uuid>"
# This will delete a business category object
# Returns a 200 or 400 status
@api_view(['DELETE'])
def delete_business_category(request, uuid):
    try:
        category = Category.objects.get(id=uuid)
        category.delete()

        return Response({"message": 'Delete Success'},
                        status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
