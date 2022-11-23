from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status


@api_view()
def error_page(request):
    return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

class SubmitForm(APIView):

    def post(self, request):
        category = self.request.data.get('category')
        message = self.request.data.get("message")

        new_users = User.objects.filter(category__id=category)
        for user in new_users:
            multiple_chn = user.channell.all()
            for chn in multiple_chn:
                loghistory = LogHistory(user=user, category=user.category, channell=chn, message=message)
                loghistory.save()
        return Response({"category": category, "message": message})


class GetLogs(APIView):

    def get(self, request, id=None, format=None):
        if id is not None:
            log_data = LogHistory.objects.get(id=id)
            serializer = LogSerializer(log_data)
            return Response(serializer.data)
        log_data = LogHistory.objects.all().order_by('-send_data')
        serializer = LogSerializer(log_data, many=True)
        return Response(serializer.data)