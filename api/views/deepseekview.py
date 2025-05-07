import os

import requests
from dotenv import load_dotenv
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

load_dotenv()


@api_view(['POST'])
@permission_classes([AllowAny])
def deepseek_chat(request):

    # lấy promt từ request
    promt = request.data.get("message")

    # kiểm tra xem promt có tồn tại không
    if not promt:
        return Response(
            {"error": "Thiếu promt đầu vào"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # lấy API key từ .env
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    if not openrouter_api_key:
        return Response(
            {"error": "Thiếu API Key"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    # tạo headers cho OpenRouter
    headers = {
        "Authorization": f"Bearer {openrouter_api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",  # sau này sẽ thay bằng domain của frontend
        "X-Title": "Django DeepSeek App",
    }

    # gửi request
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json={
                "model": "deepseek/deepseek-chat-v3-0324:free",
                "messages": [{"role": "user", "content": promt}]
            }
        )
        response.raise_for_status()  # kiểm tra lỗi HTTP
        return Response(response.json(), status=status.HTTP_200_OK)

    except requests.exceptions.RequestException as e:
        return Response(
            {"error": f"Lỗi khi gọi DeepSeek API: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )