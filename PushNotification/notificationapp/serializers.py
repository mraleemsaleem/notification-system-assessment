from rest_framework import serializers
from .models import *


#Serialziers of API
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model   = Category
        fields  = ['id','category_name']


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model   = ChannelType
        fields  = ['id','channel_name']



class LogSerializer(serializers.ModelSerializer):
    category    = serializers.PrimaryKeyRelatedField(source='category.category_name' ,queryset=Category.objects.all(), many=False)
    channel     = serializers.PrimaryKeyRelatedField(source='channell.channel_name' ,queryset=ChannelType.objects.all(), many=False)
    user        = serializers.PrimaryKeyRelatedField(source='user.username' ,queryset=ChannelType.objects.all())
    class Meta:
        model = LogHistory
        fields = ['id', 'user', 'category', 'channel', 'message', 'send_data']

    def to_representation(self, instance):
        representation = super(LogSerializer, self).to_representation(instance)
        representation['send_data'] = instance.send_data.strftime('%b %d, %Y %H:%M:%S')
        return representation