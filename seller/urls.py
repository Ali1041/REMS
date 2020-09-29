from django.urls import path
from .views import *
app_name='seller'

urlpatterns=[
    path('passwords-change/',PasswordsChange.as_view(),name='passwords'),
    path('sellercreate/',SellerCreate.as_view(),name='create_property'),
    path('list-property-approved/',SellerListSold.as_view(),name='Approve'),
    path('list-property-pending/',SellerListSold.as_view(),name='pending'),
    path('list-property-not-approved/',SellerListSold.as_view(),name='Reject'),
    path('seller-home/',SellerHome.as_view(),name='seller_home'),
    path('list-sold-property/',SellerListSold.as_view(),name='Sold'),
    path('buyer-home/', BuyerHome.as_view(), name='buyer_home'),
    path('buyer-list-house/',BuyerListPropertiesHouese.as_view(),name='house'),
    path('buyer-list-plot/',BuyerListPropertiesHouese.as_view(),name='plot'),
    path('buyer-list-rent/',BuyerListPropertiesHouese.as_view(),name='rent'),
    path('buyer-list-commercial/',BuyerListPropertiesHouese.as_view(),name='commercial'),
    path('property-detail/<int:pk>/',DetailProperty.as_view(),name='detail'),
    path('buyer-property-detail/<int:pk>/',DetailProperty1.as_view(),name='detail1'),
    path('accepting/',ApprovalView.as_view(),name='redirect'),
    path('mail-sent/',index,name='index')

]