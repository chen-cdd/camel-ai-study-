from camel.societies import RolePlaying
from camel.types import TaskType, ModelType, ModelPlatformType
from camel.models import ModelFactory

import os

# 设置代理
#os.environ["http_proxy"] = "http://127.0.0.1:7897"
#os.environ["https_proxy"] = "http://127.0.0.1:7897"

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="Qwen/Qwen2.5-72B-Instruct",
    url='https://api-inference.modelscope.cn/v1/',
    api_key='94f17f1f-3099-4689-83dd-83f8f3698ee8'
)

task_kwargs = {
    'task_prompt': '制定一个计划去过去并进行改变。',
    'with_task_specify': True,#开启后，将会有一个agent将我们的初始prompt进一步明确化
    'task_specify_agent_kwargs': {'model': model}
}

user_role_kwargs = {
    'user_role_name': '一个雄心勃勃的渴望成为时间旅行者的人',
    'user_agent_kwargs': {'model': model}
}

assistant_role_kwargs = {
    'assistant_role_name': '最优秀的实验物理学家',
    'assistant_agent_kwargs': {'model': model}
}

society = RolePlaying(
    **task_kwargs,             # 任务参数
    **user_role_kwargs,        # 指令发送者的参数
    **assistant_role_kwargs,   # 指令接收者的参数
)

def is_terminated(response):
    """
    当会话应该终止时给出对应信息。
    """
    if response.terminated:
        role = response.msg.role_type.name
        reason = response.info['termination_reasons']
        print(f'AI {role} 因为 {reason} 而终止')

    return response.terminated

def run(society, round_limit: int=10):

    # 获取AI助手到AI用户的初始消息
    input_msg = society.init_chat()

    # 开始互动会话
    for _ in range(round_limit):

        # 获取这一轮的两个响应
        assistant_response, user_response = society.step(input_msg)

        # 检查终止条件
        if is_terminated(assistant_response) or is_terminated(user_response):
            break

        # 获取结果
        print(f'[AI 用户] {user_response.msg.content}.\n')
        # 检查任务是否结束
        if 'CAMEL_TASK_DONE' in user_response.msg.content:
            break
        print(f'[AI 助手] {assistant_response.msg.content}.\n')

        # 获取下一轮的输入消息
        input_msg = assistant_response.msg

    return None

run(society)