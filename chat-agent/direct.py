from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('94f17f1f-3099-4689-83dd-83f8f3698ee8')

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="Qwen/Qwen2.5-72B-Instruct",
    url='https://api-inference.modelscope.cn/v1/',
    api_key=api_key
)

# 创建系统消息，告诉ChatAgent自己的角色定位
system_msg = "You are a helpful assistant that responds to user queries."

# 实例化一个ChatAgent
chat_agent = ChatAgent(model=model, system_message=system_msg,output_language='zh')

# 构造用户消息
user_msg = "Hello! Can you tell me something about CAMEL AI?"

# 将用户消息传给ChatAgent，并获取回复
response = chat_agent.step(user_msg)
print("Assistant Response:", response.msgs[0].content)
