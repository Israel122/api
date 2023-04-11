import random

from django.shortcuts import render
from rest_framework import generics, status, request
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Payment
from shop.models import Transaction, Category, Product, Cart, CartItem, Order
from shop.serilizers.shop_serializer import TransactionSerializer, CategorySerializer, ProductSerializer, \
    CartSerializer, CartItemSerializer, OrderSerializer


class TransactionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer1 = TransactionSerializer(data=request.data)
    #     serializer2 = ProductSerializer(data=request.data)
    #     if serializer1.is_valid():
    #         if serializer2.is_valid():
    #             requested = serializer2.validated_data['requested_quantity']
    #             available = serializer1.validated_data['available_quantity']
    #             if requested >= available:
    #                 int(requested)-int(available)
    #                 serializer1.save()
    #                 return Response(serializer1.data, status=status.HTTP_200_OK)
    #     return Response({'error: the requested quantity less than available quantity'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateTransactionView(generics.UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class CategoryView2(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def list(self, request, *args, **kwargs):
    #     product = self.request.query_params.get('name')
    #     productadresses = Category.objects.filter(product=product)
    #     Serializer = CategorySerializer(productadresses, many=True)
    #     return Response(Serializer.data, status=status.HTTP_200_OK)


class UpdateCategoryView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductView2(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, category, *args, **kwargs):
        # product = self.request.query_params.get('category')
        productiveness = Product.objects.filter(category=category)
        Serializer = ProductSerializer(productiveness, many=True)
        return Response(Serializer.data, status=status.HTTP_200_OK)


class UpdateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    def post(self, request, *args, **kwargs):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['cartSession'] = random.randint(1, 10000000000000000)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateCartView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemView(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class createCartItemView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    class CartItemView(generics.ListCreateAPIView):
        queryset = CartItem.objects.all()
        serializer_class = CartItemSerializer

        def post(self, request, *args, **kwargs):
            serializer = CartItemSerializer(data=request.data)
            if serializer.is_valid():
                cart = serializer.validated_data['cart']
                cartItems = CartItem.objects.filter(cart=cart)

                product = serializer.validated_data['product']
                is_valid = True
                for cartItem in cartItems:
                    if product == cartItem.product:
                        cartItem.quantity += serializer.validated_data['quantity']
                        cartItem.cost = cartItem.productPrice * cartItem.quantity
                        cartItem.save()
                        is_valid = False
                        return Response({'The quantity have being increase'})

                if is_valid:
                    serializer.validated_data['productPrice'] = product.price
                    quantity = serializer.validated_data['quantity']
                    productPrice = serializer.validated_data['productPrice']
                    serializer.validated_data['cost'] = quantity * productPrice
                    serializer.save()

                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': 'Error creating Cart Item'}, status=status.HTTP_400_BAD_REQUEST)

class UpdateCartItemView(generics.UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class OrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # def post(self, request, *args, **kwargs):
    #     if

    def post(self, request):
        products = Product.objects.all()
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            # cartCreate = Cart(cartSession=random.randint, person=)
            # cartCreate.save()
            carts = serializer.validated_data['cart']
            cartitem = CartItem.objects.filter(cart=carts)
            product_is_valid = False
            cost = 0
            for cart in cartitem:
                if cart.product in products:
                    trans = Product.objects.get(pk=cart.product.pk)
                    if cart.quantity <= trans.quantity:
                        cost += cart.cost
                        trans.\
                            quantity -= cart.quantity
                        product_is_valid = True
                        trans.save()
                    else:
                        return Response({'error': "The Quantity of the Product is not available"})
                        break
                else:
                    cart.delete()

                if product_is_valid == True:
                    # payment = serializer.validated_data['payment']
                    # balance = payment.balance
                    # order_payment = Payment.objects.get(pk=payment.pk)
                    payment = Payment.objects.get(person=carts.person)
                    if cost <= payment.balance:
                        payment.balance - cost
                        payment.save()

                        transaction = Transaction(ref=payment.cardNumber, amount=cost, paymentMethod=payment,
                                                  person=carts.person, status=serializer.validated_data['status'],
                                                  cart=carts)
                        transaction.save()

                    serializer.validated_data['transaction'] = transaction
                    serializer.save()

                    return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': "Order not created"})

class UpdateOrderView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DeleteCart(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class GetCart(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def list(self, request, pk, *args, **kwargs):
        cart = CartItem.objects.filter(cart=pk)
        Serializer = CartItemSerializer(cart, many=True)
        return Response(Serializer.data, status=status.HTTP_200_OK)
