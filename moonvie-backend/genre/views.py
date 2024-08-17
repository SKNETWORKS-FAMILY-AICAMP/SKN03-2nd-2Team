from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import GetRequestSerializer, GetResponseSerializer


# Create your views here.
class TestView(APIView):
    permission_classes = [permissions.AllowAny]

    # query_serializer는 해당 serializer에서 설정한 내용을 swagger에서 인풋값으로 받을 수 있게 해줌
    @swagger_auto_schema(
        tags=["데이터를 검색합니다."],
        query_serializer=GetRequestSerializer,
        responses={200: GetResponseSerializer},
    )
    def get(self, request):
        return Response("Swagger 연동 테스트")
