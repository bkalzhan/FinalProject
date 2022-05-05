from django.contrib import admin
from django.urls import path, include
from .views import GymsViewSet, SubscriptionsViewSet, AbonementsViewSet, \
    GymPhotoDetailsApiView, GymPhotoListApiView, transaction_list_post_view, transaction_view, CommentsViewSet, \
    comments_by_gym_detail

urlpatterns = [
    path('gyms/', GymsViewSet.as_view({'get': 'list',
                                         'post': 'create'})),
    path('gyms/<int:pk>/', GymsViewSet.as_view({'get': 'retrieve',
                                                  'delete': 'destroy',
                                                  'put': 'update'})),
    path('gyms/<int:rk>/subscriptions/', SubscriptionsViewSet.as_view({'get': 'subscriptions_by_gym',
                                                                 'post': 'create'})),
    path('gyms/<int:rk>/subscriptions/<int:pk>/', SubscriptionsViewSet.as_view({'get': 'subscription_details_by_gym',
                                                                          'delete': 'destroy',
                                                                          'put': 'update'})),
    path('gymphotos/', GymPhotoListApiView.as_view()),
    path('gymphotos/<int:pk>/', GymPhotoDetailsApiView.as_view()),
    path('gyms/<int:pk>/abonements/', AbonementsViewSet.as_view({'get': 'abonements_by_gym'})),
    path('abonements/', AbonementsViewSet.as_view({'get': 'list',
                                                     'post': 'create'})),
    path('abonements/<int:pk>/', AbonementsViewSet.as_view({'get': 'retrieve',
                                                              'delete': 'destroy',
                                                              'put': 'update'})),
    path('transactions/', transaction_list_post_view),
    path('transactions/<int:pk>/', transaction_view),
    path('comments/', CommentsViewSet.as_view({'get': 'list',
                                               'post': 'create'})),
    path('comments/<int:pk>/', CommentsViewSet.as_view({'get': 'retrieve',
                                                        'delete': 'destroy',
                                                        'put': 'update'})),
    path('gyms/<int:hk>/comments/', CommentsViewSet.as_view({'get': 'comments_by_gym'})),
    path('gyms/<int:hk>/comments/<int:pk>/', comments_by_gym_detail),
]
