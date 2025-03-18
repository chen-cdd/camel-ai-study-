from camel.messages import BaseMessage

# 创建用户消息
user_msg = BaseMessage.make_user_message(
    role_name="User_1",
    content="Hi, what can you do?"
)

# 创建助手消息
assistant_msg = BaseMessage.make_assistant_message(
    role_name="Assistant_1",
    content="I can help you with various tasks."
)

print("User Message:", user_msg)
print("Assistant Message:", assistant_msg)