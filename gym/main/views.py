import logging

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets, status
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic import DetailView
from datetime import datetime, timedelta
from .models import Gym, Subscription, Abon, Transaction, GymPhoto, Comment
from .serializers import GymSerializer, GymSerializerShort, GymPhotoSerializer, \
    TransactionSerializer, CommentSerializer, SubscriptionSerializerShort, AbonementSerializer, \
    SubscriptionSerializer, AbonementSerializerShort


# Create your views here.

logger = logging.getLogger(__name__)


class GymsViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list':
            return GymSerializerShort
        elif self.action == 'retrieve':
            return GymSerializer
        elif self.action == 'create':
            return GymSerializer
        elif self.action == 'update':
            return GymSerializerShort
        elif self.action == 'destroy':
            return GymSerializer


class SubscriptionsViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SubscriptionSerializerShort

    def get_serializer_class(self):
        if self.action == 'create':
            return SubscriptionSerializer
        elif self.action == 'update':
            return SubscriptionSerializer
        elif self.action == 'destroy':
            return SubscriptionSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def subscriptions_by_gym(self, request, rk):
        queryset = Subscription.objects.filter(gym=rk)
        serializer = SubscriptionSerializerShort(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def subscription_details_by_gym(self, request, pk, rk):
        queryset = Subscription.objects.subscription_details_by_gym(rk, pk)
        serializer = SubscriptionSerializer(queryset, many=True)
        return Response(serializer.data)


class AbonementsViewSet(viewsets.ModelViewSet):
    queryset = Abon.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AbonementSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return AbonementSerializerShort
        elif self.action == 'retrieve':
            return AbonementSerializer
        elif self.action == 'create':
            return AbonementSerializer
        elif self.action == 'update':
            return AbonementSerializer
        elif self.action == 'destroy':
            return AbonementSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def abonements_by_gym(self, request, pk):
        queryset = Abon.objects.abonements_by_gym(pk)
        serializer = AbonementSerializer(queryset, many=True)
        return Response(serializer.data)


class GymPhotoListApiView(generics.ListCreateAPIView):
    serializer_class = GymPhotoSerializer
    permission_classes = (AllowAny,)
    parser_classes = [FormParser, JSONParser, MultiPartParser]

    def get_queryset(self):
        queryset = GymPhoto.objects.all()
        return queryset


class GymPhotoDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GymPhotoSerializer
    permission_classes = (AllowAny,)
    queryset = GymPhoto.objects.all()
    parser_classes = [FormParser, JSONParser, MultiPartParser]


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def transaction_list_post_view(request):
    if request.method == 'GET':
        transaction_list = Transaction.objects.all()
        serializer = TransactionSerializer(transaction_list, many=True)
        logger.debug(f'Transaction created ID: {serializer.instance}')
        logger.info(f'Transaction created ID:  {serializer.instance}')
        logger.warning(f'Transaction created ID:  {serializer.instance}')
        logger.error(f'Transaction created ID:  {serializer.instance}')
        logger.critical(f'Transaction created ID:  {serializer.instance}')
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'Transaction created ID: {serializer.instance}')
            logger.info(f'Transaction created ID:  {serializer.instance}')
            logger.warning(f'Transaction created ID:  {serializer.instance}')
            logger.error(f'Transaction created ID:  {serializer.instance}')
            logger.critical(f'Transaction created ID:  {serializer.instance}')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def transaction_view(request, pk):
    try:
        transaction = Transaction.objects.get(id=pk)
    except Transaction.DoesNotExist as e:
        return Response({'error': str(e)})
    if request.method == 'GET':
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TransactionSerializer(instance=transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})
    if request.method == 'DELETE':
        transaction.delete()
        return Response({'deleted': True})


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TransactionSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return TransactionSerializer
        elif self.action == 'retrieve':
            return TransactionSerializer
        elif self.action == 'create':
            return TransactionSerializer
        elif self.action == 'update':
            return TransactionSerializer
        elif self.action == 'destroy':
            return TransactionSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentSerializer
        elif self.action == 'retrieve':
            return CommentSerializer
        elif self.action == 'create':
            return CommentSerializer
        elif self.action == 'update':
            return CommentSerializer
        elif self.action == 'destroy':
            return CommentSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def comments_by_gym(self, request, hk):
        queryset = Comment.objects.filter(gym=hk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comments_by_gym_detail(request, pk, hk):
    queryset = Comment.objects.comment_detail_by_gym(hk, pk)
    serializer = CommentSerializer(queryset, many=True)
    return Response(serializer.data)
