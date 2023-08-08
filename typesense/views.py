from django.shortcuts import render
from requests import Response
from rest_framework.views import APIView

from .serilaizers import PostSerializer
from .utils import client
from .models import Post


# Create your views here.
class PostSearch(APIView):

    def get(self, request, format=None):
        search = self.request.GET.get('search', None)
        if search is not None:
            search_parameters = {
                'q': search,
                'query_by': 'title,description',
                'include_fields': 'id',
                'per_page': 250,
                'page': 1

            }
            res = client.collections['posts'].documents.search(search_parameters)
            newlist = [x['document']['id'] for x in res['hits']]
            queryset = Post.objects.filter(id__in=newlist).order_by('-id')

            serializer = PostSerializer(queryset, many=True)
            return Response(serializer.data)