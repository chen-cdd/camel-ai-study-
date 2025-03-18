from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType
from camel.messages import BaseMessage
from fiction_tools import NovelRecommendationTool
import os

class NovelRecommendationAgent:
    def __init__(self, model=None):
        self.tool = NovelRecommendationTool()
        self.model = model
        self.agent = ChatAgent(model=model, output_language='zh')

    def process_request(self, user_input):
        # 从用户输入提取偏好，例如：'推荐一本科幻小说'
        genre = None
        author = None
        
        if '科幻' in user_input:
            genre = 'Dystopian'
        elif '小说' in user_input:
            genre = 'Fiction'
        
        # 调用小说推荐工具
        recommendation = self.tool.recommend_novel(genre=genre)
        return f"我为你推荐这本小说：'{recommendation['title']}'，类型：{recommendation['genre']}，作者：{recommendation['author']}"

    def chat(self, user_input):
        # 处理用户请求
        result = self.process_request(user_input)
        # 将结果传递给ChatAgent
        response = self.agent.step(result)
        return response.msgs[0].content

# 主程序
if __name__ == "__main__":
    # 创建模型
    model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
        model_type="Qwen/Qwen2.5-72B-Instruct",
        url='https://api-inference.modelscope.cn/v1/',
        api_key='94f17f1f-3099-4689-83dd-83f8f3698ee8'  # 使用您的API密钥
    )
    
    # 创建代理
    agent = NovelRecommendationAgent(model=model)
    
    # 测试
    user_query = "推荐一本科幻小说"
    recommendation = agent.process_request(user_query)
    print(recommendation)

