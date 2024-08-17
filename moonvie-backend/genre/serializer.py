from rest_framework import serializers


# query param
class GetRequestSerializer(serializers.Serializer):
    offset = serializers.IntegerField(help_text="기준점 번호", default=0)
    limit = serializers.IntegerField(help_text="출력할 row 갯수", default=10)
    trial_stage = serializers.CharField(help_text="trial_stage param", required=False)


class GetResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()
