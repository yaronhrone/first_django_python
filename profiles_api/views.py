from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiVeiw(APIView):
    """Test API View"""

    def get(self,requst,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional Django View',
            'gives you the most control over your application logic',
            'is mapped manually to URLs',
        ]
        return Response({'message' : 'Hello!', 'an_apiview': an_apiview})