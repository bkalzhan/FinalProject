from rest_framework import serializers
from .models import Gym, Subscription, Abon, Transaction, GymPhoto, Comment


class GymPhotoSerializer(serializers.ModelSerializer):
    gym_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = GymPhoto
        fields = '__all__'


class BaseGymSerializer(serializers.ModelSerializer):
    gym_photos = GymPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Gym
        fields = '__all__'
        abstract = True


class GymSerializerShort(BaseGymSerializer):
    class Meta:
        model = Gym
        fields = ['id', 'name']


class GymSerializer(BaseGymSerializer):
    class Meta:
        model = Gym
        fields = '__all__'


class BaseSubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ['id', 'gym', 'cost']
        abstract = True


class SubscriptionSerializer(BaseSubscriptionSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class SubscriptionSerializerShort(BaseSubscriptionSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'type', 'cost']


class AbonementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abon
        fields = '__all__'


class AbonementSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Abon
        fields = ['id', 'subscription', 'gym', 'purchase_date', 'expired_date']


class TransactionSerializer(serializers.ModelSerializer):
    abonement_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'


class BaseCommentSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(write_only=True)
    gym_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        abstract = True


class CommentSerializer(BaseCommentSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

