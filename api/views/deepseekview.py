from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.service.deepseek_service import DeepSeekService
from api.serializer import DeepSeekSerializer

@api_view(['POST'])
def deepseek_chat(request):
    serializer = DeepSeekSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    response = DeepSeekService.get_response(
        serializer.validated_data['prompt'],
        serializer.validated_data.get('model'),
        serializer.validated_data.get('max_tokens')
    )

    if response:
        return Response(response, status=status.HTTP_200_OK)
    else:
        return Response(
            {"error": "Failed to get response from DeepSeek"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )