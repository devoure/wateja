from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from customers.models import Customer
from customers.api.serializers import CustomerSerializer

# Create your views here.


# Function to handle a GET Request to endpoint "http://wateja/v1/customers/"
# Returns an overview of URLs in the endpoint root /wateja/v1/customers/
@api_view(['GET'])
def index(request):
    api_list = {
            'Get Customers List': '/customers-list/',
            'Get Detailed View of a Customer': '/customer-detail/<str:uuid>/',
            'Create a new Customer Object': '/customer-create/',
            'Update a Customer Object': '/customer-update/<str:uuid>/',
            'Delete a Customer Object': '/customer-delete/<str:uuid>/',
            }
    return Response(api_list)


# Function to handle a GET Request to endpoint "http://wateja/v1/customers/customers-list"
# Returns a list of customers in the app
@api_view(['GET'])
def get_customers(request):
    try:
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    # Provide a 500 response incase of errors in the above code
    except Exception as e:
        return Response({'error': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Function to handle a GET Request to endpoint "http://wateja/v1/customers/customer-detail/uuid"
# Returns a detailed view of a particular customer with uuid passed.
@api_view(['GET'])
def get_customer_detail(request, uuid):
    try:
        customer = Customer.objects.get(id=uuid)
        serializer = CustomerSerializer(customer, many=False)

        return Response(serializer.data)

    # Provide a 500 response incase of errors in the above code
    except Exception as e:
        return Response({'error': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Function to handle a POST Request to endpoint "http://wateja/v1/customers/customer-create/"
# This will create a customer object
# Returns the new item added in the database
@api_view(['POST'])
def add_customer(request):
    try:
        serializer = CustomerSerializer(data=request.data)

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


# Function to handle a POST Request to endpoint "http://wateja/v1/customers/customer-update/<uuid>"
# This will update a customer object
# Returns the new item updated
@api_view(['POST'])
def update_customer(request, uuid):
    try:
        customer = Customer.objects.get(id=uuid)
        serializer = CustomerSerializer(instance=customer,
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


# Function to handle a DELETE Request to endpoint "http://wateja/v1/customers/customer-delete/<uuid>"
# This will delete a customer object
# Returns a 200 or 400 status
@api_view(['DELETE'])
def delete_customer(request, uuid):
    try:
        customer = Customer.objects.get(id=uuid)
        customer.delete()

        return Response({"message": 'Delete Success'},
                        status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
