#      from django.test import TestCase
#
# # Create your tests here.
#      def post(self, request):
#          products = Product.objects.all()
#          serializer = OrderSerializer(data=request.data)
#          if serializer.is_valid():
#              product = serializer.validated_data['product']
#              if serializer.validated_data['product'] in products:
#                  quantity = serializer.validated_data['quantity']
#                  trans = Product.objects.get(pk=product.pk)
#                  if quantity <= trans.available_quantity:
#                      trans.available_quantity = trans.available_quantity - quantity
#                      trans.save()
#
#                      price = serializer.validated_data['price']
#                      payment = serializer.validated_data['payment']
#                      balance = payment.balance
#                      order_payment = Payment.objects.get(pk=payment.pk)
#                      if price <= balance:
#                          order_payment.balance = order_payment.balance - price
#                          order_payment.save()
#                          serializer.save()
#
#                          status = serializer.validated_data['status']
#                          cart = serializer.validated_data['cart']
#                          transaction = Transaction(ref=order_payment.cardNumber, amount=price * quantity,
#                                                    person=cart.person, status=status, cart=cart, )
#                          return Response(serializer.data)
