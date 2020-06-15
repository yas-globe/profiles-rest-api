from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Call an endpoint and this class > function will handle
class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete',
            'Is similar to a traditional Django View',
            'Gives you the most control over your app logic'
            'Is mapped manually to URLs'
        ]

        # converts list to JSON
        return Response({'message': 'Hello! Here is the list', 'an_apiview': an_apiview})
