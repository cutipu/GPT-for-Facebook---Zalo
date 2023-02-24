from zalo.sdk import ZaloSDK
import openai
import json

# Khởi tạo ZaloSDK với thông tin ứng dụng và mã truy cập
app_id = 'your_app_id'
app_secret = 'your_app_secret'
oa_token = 'your_oa_token'
zalo_sdk = ZaloSDK(app_id, app_secret)

# Khởi tạo OpenAI API với mã API key hợp lệ
openai.api_key = "your_api_key"

# Hàm trả về câu trả lời từ GPT Chat
def get_response(input_text):
    response = openai.Completion.create(
      engine="davinci",
      prompt=input_text,
      max_tokens=60,
      n=1,
      stop=None,
      temperature=0.5
    )
    return response.choices[0].text.strip()

# Hàm xử lý tin nhắn đến và trả về tin nhắn trả lời
def process_message(event):
    sender_id = event['sender']['id']
    message_text = event['message']['text']
    response_text = get_response(message_text)
    response = {
        "recipient": {"user_id": sender_id},
        "message": {"text": response_text}
    }
    return json.dumps(response)

# Thiết lập webhook để lắng nghe tin nhắn đến
zalo_sdk.oa.set_webhook('your_webhook_url')

# Xử lý tin nhắn đến và gửi tin nhắn trả lời
@zalo_sdk.oa.on_message
def handle_message(event):
    response = process_message(event)
    zalo_sdk.oa.send_message(response)

# Chạy ứng dụng
if __name__ == '__main__':
    zalo_sdk.run()
