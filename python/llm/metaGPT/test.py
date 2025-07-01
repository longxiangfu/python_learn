import re
import subprocess

from metagpt.actions import Action, UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
import asyncio

from metagpt.context import Context


class SimpleWriteCode(Action):
    PROMPT_TEMPLATE: str = """
    Write a python function that can {instruction}.
    Return ```python your_code_here ``` with NO other texts,
    your code:
    """
    name: str = "SimpleWriteCode"

    async def run(self, instruction: str):
        prompt = self.PROMPT_TEMPLATE.format(instruction=instruction)

        logger.info(prompt)

        rsp = await self._aask(prompt)

        code_text = self.parse_code(rsp)

        return code_text

    @staticmethod
    def parse_code(rsp):
        pattern = r"```python(.*)```"
        match = re.search(pattern, rsp, re.DOTALL)
        code_text = match.group(1) if match else rsp
        return code_text


class SimpleWriteTest(Action):
    PROMPT_TEMPLATE: str = """
    Context: {context}
    Write {k} unit tests using pytest for the given function, assuming you have imported it.
    Return ```python your_code_here ``` with NO other texts,
    your code:
    """

    name: str = "SimpleWriteTest"

    async def run(self, context: str, k: int = 3):
        prompt = self.PROMPT_TEMPLATE.format(context=context, k=k)

        logger.info(prompt)

        rsp = await self._aask(prompt)

        code_text = self.parse_code(rsp)

        return code_text

    @staticmethod
    def parse_code(rsp):
        pattern = r"```python(.*)```"
        match = re.search(pattern, rsp, re.DOTALL)
        code_text = match.group(1) if match else rsp
        return code_text

class SimpleWriteReview(Action):
    PROMPT_TEMPLATE: str = """
    Context: {context}
    Review the test cases and provide one critical comments:
    """

    name: str = "SimpleWriteReview"

    async def run(self, context: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context)

        logger.info(prompt)

        rsp = await self._aask(prompt)

        return rsp


class SimpleCoder(Role):
    name: str = "Alice"
    profile: str = "SimpleCoder"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._watch([UserRequirement])
        self.set_actions([SimpleWriteCode])

class SimpleTester(Role):
    name: str = "Bob"
    profile: str = "SimpleTester"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleWriteTest])
        self._watch([SimpleWriteCode])
        # self._watch([SimpleWriteCode, SimpleWriteReview])  # feel free to try this too

    async def _act(self) -> Message:
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        todo = self.rc.todo

        # context = self.get_memories(k=1)[0].content # use the most recent memory as context
        context = self.get_memories()  # use all memories as context

        code_text = await todo.run(context, k=5)  # specify arguments
        msg = Message(content=code_text, role=self.profile, cause_by=type(todo))

        return msg

class SimpleReviewer(Role):
    name: str = "Charlie"
    profile: str = "SimpleReviewer"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleWriteReview])
        self._watch([SimpleWriteTest])


import asyncio
import typer
from metagpt.logs import logger
from metagpt.team import Team
app = typer.Typer()

async def main(
        idea: str = typer.Argument(..., help="write a function that calculates the product of a list"),
        investment: float = typer.Option(default=3.0, help="Dollar amount to invest in the AI company."),
        n_round: int = typer.Option(default=5, help="Number of rounds for the simulation."),
):
    logger.info(idea)

    # 创建一个团队
    team = Team()
    # 团队里添加三个角色
    team.hire(
        [
            SimpleCoder(),
            SimpleTester(),
            SimpleReviewer(),
        ]
    )

    team.invest(investment=3.0)
    team.run_project(idea)
    await team.run(n_round=5)

asyncio.run(main(idea="写一个python函数用来计算一个list中数字的和"))