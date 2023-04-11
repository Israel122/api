from django.urls import path

from shop.models import Transaction
from shop.views import TransactionView, CategoryView, ProductView, CartView, createCartItemView, OrderView, \
    UpdateTransactionView, UpdateCategoryView, UpdateProductView, UpdateCartView, UpdateCartItemView, UpdateOrderView, \
    CategoryView2, ProductView2, DeleteCart, GetCart, CartItemView

urlpatterns = [
    path('transaction', TransactionView.as_view()),
    path('updatetransaction/<int:pk>', UpdateTransactionView.as_view()),
    path('listcategory', CategoryView.as_view()),
    path('category', CategoryView2.as_view()),
    path('updatecategory/<int:pk>', UpdateCategoryView.as_view()),
    path('product', ProductView.as_view()),
    path('products', ProductView2.as_view()),
    path('deletecart/<int:pk>', DeleteCart.as_view()),
    path('listproduct/<int:category>', ProductView2.as_view()),
    path('updateproduct/<int:pk>', UpdateProductView.as_view()),
    path('cart', CartView.as_view()),
    path('updatecart/<int:pk>', UpdateCartView.as_view()),
    path('cartitem', createCartItemView.as_view()),
    path('listcartitem', CartItemView.as_view()),
    path('updatecartitem/<int:pk>', UpdateCartItemView.as_view()),
    path('order', OrderView.as_view()),
    path('updateorder/<int:pk>', UpdateOrderView.as_view()),
    path('getcart/<int:pk>', GetCart.as_view()),
    # path('createCartItemView', createCartItemView.as_view())
]