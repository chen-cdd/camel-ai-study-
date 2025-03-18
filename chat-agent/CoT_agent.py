from camel.agents import TaskSpecifyAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, TaskType
import os
from dotenv import load_dotenv

load_dotenv()
api_key = '94f17f1f-3099-4689-83dd-83f8f3698ee8' 

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="Qwen/Qwen2.5-72B-Instruct",
    url='https://api-inference.modelscope.cn/v1/',
    api_key=api_key
)
task_specify_agent = TaskSpecifyAgent(
    model=model, task_type=TaskType.AI_SOCIETY,output_language='中文'
)
specified_task_prompt = task_specify_agent.run(
    task_prompt="Improving stage presence and performance skills",
    meta_dict=dict(
        assistant_role="Musician", user_role="Student", word_limit=100
    ),
)
print(f"Specified task prompt:\n{specified_task_prompt}\n")