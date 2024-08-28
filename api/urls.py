from django.urls import path
from .views import ReceiptList, ReceiptDetail
urlpatterns = [
    path('receipts/process/', ReceiptList.as_view()),
    path('receipts/<uuid:id>/points/', ReceiptDetail.as_view())
]