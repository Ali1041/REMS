from django.urls import path

from .views import *
app_name='management'

urlpatterns=[
    path('',PropertyHome,name='admin_home'),
    path('list-properties/',PropertyList.as_view(),name='All'),
    path('list-properties-approve-admin/',PropertyList.as_view(),name='Approve'),
    path('list-properties-sold-admin/', PropertyList.as_view(), name='Sold'),
    path('list-properties-reject-admin/', PropertyList.as_view(), name='Reject'),
    path('list-properties-pending-admin/', PropertyList.as_view(), name='Pending'),
    path('list-property-houses-admin/',TypeProperty.as_view(),name='Houses'),
    path('list-property-plot-admin/', TypeProperty.as_view(), name='Plot'),
    path('list-property-Commercial-admin/', TypeProperty.as_view(), name='Commercial'),
    path('admin-approve/<int:pk>/',AdminApprovalProperty.as_view(),name='approve'),
    path('admin-reject/<int:pk>/',AdminApprovalProperty.as_view(),name='reject'),
    path('admin-sold-property/<int:pk>/',AdminApprovalProperty.as_view(),name='sold'),
    path('admin-delete/<int:pk>/',DeleteView.as_view(),name='delete'),
    path('seller-list/',PersonList.as_view(),name='seller'),
    path('buyer-list/',PersonList.as_view(),name='buyer'),
    # path('search/',request1,name='nothing')
]