from rest_framework import serializers


class LinkSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=1000)