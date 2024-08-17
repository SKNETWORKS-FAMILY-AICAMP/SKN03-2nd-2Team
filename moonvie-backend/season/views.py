# swagger와 관련 없는 package들은 삭제하였습니다.

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class TestView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        return Response("Swagger 연동 테스트")
