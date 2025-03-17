from rest_framework.serializers import ModelSerializer
from subscription.models import Subscribe


class SubscribeSerializer(ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['email', 'is_active']
        read_only_fields = ['is_active']