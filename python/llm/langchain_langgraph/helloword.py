from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage, SystemMessage

model = ChatDeepSeek(model="deepseek-chat", api_key="sk-d31136f3bc6549669a98e9be69c8ef9a")

messages = [
    SystemMessage(content="翻译以下英文为中文"),
    HumanMessage(content="hi!"),
]

result = model.invoke(messages)

print(result) # content='嗨！' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 2, 'prompt_tokens': 10, 'total_tokens': 12, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 0}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 10}, 'model_name': 'deepseek-chat', 'system_fingerprint': 'fp_3a5770e1b4_prod0225', 'finish_reason': 'stop', 'logprobs': None} id='run-baef98a0-f417-49ce-9059-8b4dcf9f50b8-0' usage_metadata={'input_tokens': 10, 'output_tokens': 2, 'total_tokens': 12, 'input_token_details': {'cache_read': 0}, 'output_token_details': {}}
