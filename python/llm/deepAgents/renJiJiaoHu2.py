"""
人机交互2
当用户决定编辑时，用户可以编辑工具参数
"""
import uuid

from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command


@tool
def delete_file(path: str) -> str:
    """
    从文件系统重删除文件
    Args:
        path: 文件路径

    Returns: 响应

    """
    return f"已删除 {path}"

@tool
def read_file(path: str) -> str:
    """
    从文件系统中读取文件
    Args:
        path: 文件路径

    Returns: 响应

    """
    return f"{path} 的内容"

@tool
def send_email(to: str, subject: str, body: str) -> str:
    """
    发送电子邮件
    Args:
        to: 目的地
        subject: 邮件主题
        body: 邮件内容

    Returns: 响应

    """
    return f"已发送邮件至 {to}"


# 创建人机交互检查点
checkpointer = MemorySaver()

# 创建深度代理
model = init_chat_model("glm-4.6:cloud", model_provider="ollama", base_url="http://localhost:11434")
agent = create_deep_agent(
    model=model,
    tools=[delete_file, read_file, send_email],
    # 工具名称映射到中断配置（当使用到工具时是否需要中断，以及中断时允许的操作）
    interrupt_on={
        "delete_file": True, # 默认：批准、编辑、拒绝
        "read_file": False, # 无需中断
        "send_email": {"allowed_decisions": ["approve", "reject", "edit"]} # 批准、拒绝、编辑
    },
    checkpointer=checkpointer
)

# 创建带有thread_id的配置以实现状态持久化（用于中断恢复）
config = {"configurable": {"thread_id": str(uuid.uuid4())}}

# 调用agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "给邮箱1565267514@qq.com发邮件，内容是：123456789, 主题是：lxf测试"}]},
    config=config)

# 检查执行是否被中断
if result.get("__interrupt__"):
    # 提取中断信息
    interrupts = result["__interrupt__"][0].value
    action_requests = interrupts["action_requests"] # 操作请求
    review_configs = interrupts["review_configs"] # 审核配置

    # 创建从工具名称到审核配置的映射
    config_map = {cfg["action_name"]: cfg for cfg in review_configs}

    # 向用户展示待处理的操作
    for action in action_requests:
        review_config = config_map[action["name"]] # 操作工具对应的审核配置
        print(f"工具： {action['name']}") # 工具： send_email
        print(f"参数： {action['args']}") # 参数： {'to': '1565267514@qq.com', 'subject': 'lxf测试', 'body': '123456789'}
        print(f"允许的决策： {review_config['allowed_decisions']}") # 允许的决策： ['approve', 'reject', 'edit']

    # 模拟获取用户决策（注意，每个action_request一个决策，按顺序）
    decisions = []
    for action in action_requests:
        decision = {
            "type": "edit",
            "edited_action": { # 用户编辑邮件
                "name": action["name"], # 必须包含工具名称
                "args": {"to": "1565267514@qq.com", "subject": "这是我的主题", "body": "这是我的内容"} # 用户编辑后的邮件参数
            }
        }
        decisions.append(decision)


    # 使用决策恢复执行
    result = agent.invoke(
        Command(resume={"decisions": decisions}),
        config=config # 必须使用相同的配置
    )


# 处理最终结果
print(result["messages"][-1].content) # 邮件已成功发送至 1565267514@qq.com