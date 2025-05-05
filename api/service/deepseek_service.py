import requests
from django.conf import settings


class DeepSeekService:
    API_URL = "https://api.deepseek.com/v1/chat/completions"  # Kiểm tra lại endpoint chính xác

    @classmethod
    def get_response(cls, prompt, model="deepseek-chat", max_tokens=2048):
        headers = {
            "Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens
        }

        try:
            response = requests.post(cls.API_URL, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            # Xử lý lỗi phù hợp với ứng dụng của bạn
            print(f"Error calling DeepSeek API: {e}")
            return None