from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format= None):
        """request a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application login',
            'is mapped manually to URLS'
        ]

        return Response({'message': 'Hello', 'an_apiview' : an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer


    def list(self, request):
        """Return a hello message"""
        an_viewset = [
            'Uses HTTP methods as function (get, post, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application login',
            'is mapped manually to URLS'
        ]

        return Response({'message':'Hellow World', 'viewset': an_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            serializer.errors
            status = status.HTTP_400_BAD_REQUEST


    def  retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})


    def  update(self, request, pk=None):
        """Handle updating an object by its ID"""
        return Response({'http_method': 'UPDATE'})
