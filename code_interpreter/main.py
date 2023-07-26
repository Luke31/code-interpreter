from dotenv import load_dotenv
from langchain.agents import AgentType, create_csv_agent
from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import PythonREPLTool

# import os
# import openai

load_dotenv()  # Load environment variables from .env file
# api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = api_key
model = "gpt-3.5-turbo"
csv_path = "in/episode_info.csv"
# model = "gpt-4"


def main():
    print("start")
    python_agent_executor = create_python_agent(
        llm=ChatOpenAI(temperature=0, model=model),
        tool=PythonREPLTool(),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # python_agent_executor.run(
    #     "generate and save in the 'out'-directory within the current working directory 5 QRcodes that point to www.eastwards.jp"
    # )

    csv_agent = create_csv_agent(
        llm=ChatOpenAI(
            temperature=0,
            model=model,
        ),
        path=csv_path,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
    csv_agent.run("in file episode_info, which writer wrote the most episodes? how many episodes did they write?")


if __name__ == "__main__":
    main()
