from dotenv import load_dotenv
from langchain.agents import AgentType
from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import PythonREPLTool

# import os
# import openai

load_dotenv()  # Load environment variables from .env file
# api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = api_key
model = "gpt-3.5-turbo"
# model = "gpt-4-0613"


def main():
    print("start")
    python_agent_executor = create_python_agent(
        llm=ChatOpenAI(temperature=0, model=model),
        tool=PythonREPLTool(),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    python_agent_executor.run(
        "generate and save in the 'out'-directory within the current working directory 5 QRcodes that point to www.eastwards.jp"
    )


if __name__ == "__main__":
    main()
