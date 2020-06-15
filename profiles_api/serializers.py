from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    """Serializes a name field for testing our API View, Accepts name input"""
    # takes care to validate data type
    name = serializers.CharField(max_length=10)