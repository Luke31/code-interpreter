from dotenv import load_dotenv
from langchain.agents import AgentType, create_csv_agent, initialize_agent
from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import PythonREPLTool, Tool

load_dotenv()  # Load environment variables from .env file
csv_path = "in/episode_info.csv"
model_python_agent_executor = "gpt-3.5-turbo"
model_csv_agent = "gpt-3.5-turbo"
model_grand_agent = "gpt-4"

def main():
    print(f"start")
    python_agent_executor = create_python_agent(
        llm=ChatOpenAI(temperature=0, model=model_python_agent_executor),
        tool=PythonREPLTool(),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    csv_agent = create_csv_agent(
        llm=ChatOpenAI(
            temperature=0,
            model=model_csv_agent,
        ),
        path=csv_path,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )

    grand_agent = initialize_agent(
        tools=[
            Tool(
                name="PythonAgent",
                func=python_agent_executor.run,
                description="""useful when you need to transform natural language and write from it python and execute the python code, 
    returning the results of the code execution,
    DO NOT SEND PYTHON CODE TO THIS TOOL""",
            ),
            Tool(
                name="CSVAgent",
                func=csv_agent.run,
                description="""useful when you need to answer question over episode_info.csv file,
                                               takes an input the entire question and returns the answer after running pandas calculations""",
            ),
        ],
        llm=ChatOpenAI(temperature=0, model=model_grand_agent),
        agent_type=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
    )
    # cmd = "generate and save in the directory called out within the current working directory 5 QRcodes that point to www.eastwards.jp"
    cmd = "in file episode_info.csv in directory called in, which writer wrote the most episodes? how many episodes did they write?"
    grand_agent.run(cmd)


if __name__ == "__main__":
    main()
