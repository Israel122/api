from django.contrib.auth.hashers import make_password
from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from account.models import Person, Address, Payment
from account.serilizers.account_serializer import PersonSerializer, AddressSerializer, PaymentSerializer


# Create your views here.
class CreateUser(APIView):

    def post(self, request, format=None):
        print(request.data)
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.validated_data['is_active'] = True
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'error': 'ERROR creating user'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, format=None):
        username = [user.username for user in Person.objects.all()]
        return Response({'username': username}, status=status.HTTP_200_OK)


class AddressView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    # def list(self, request, *args, **kwargs):
    #     serializers = AddressSerializer(Address.objects.all(), many=True)
    #     return Response(serializers.data, status=status.HTTP_200_OK)


class UpdateAddressView(generics.UpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class Paymentview(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class UpdatePaymentview(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    # def put(self, request, *args, **kwargs):
    #     return self.update(self, *args, **kwargs)


class GetAddressview(generics.RetrieveDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressViewUser(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def list(self, request, user, *args, **kwargs):
        user = self.request.query_params.get('user')

        userAddressess = Address.objects.filter(person=user)
        Serializer = AddressSerializer(userAddressess, many=True)
        return Response(Serializer.data, status=status.HTTP_200_OK)

# balance = serializer.validated_data["balance"]
# if balance >= serializer.validated_data['cost']:
#     var = balance - serializer.validated_data['cost']
