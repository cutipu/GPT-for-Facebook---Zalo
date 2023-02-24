import facebook
import openai

# Khai báo thông tin đăng nhập Facebook API
access_token = 'YOUR_ACCESS_TOKEN'
group_id = 'YOUR_GROUP_ID'

# Khai báo thông tin đăng nhập OpenAI API
openai.api_key = "YOUR_OPENAI_API_KEY"

# Kết nối đến group chat Facebook
graph = facebook.GraphAPI(access_token)
messages = graph.get_connections(group_id, 'messages')

# Lấy tin nhắn mới nhất từ group chat
message = messages['data'][0]['message']

# Tạo câu trả lời bằng chat GPT từ tin nhắn
response = openai.Completion.create(
    engine="davinci",
    prompt=message,
    max_tokens=60,
    n=1,
    stop=None,
    temperature=0.5,
)

# Phản hồi lại tin nhắn với câu trả lời của chat GPT
graph.put_object(group_id, 'messages', message=response['choices'][0]['text'])
