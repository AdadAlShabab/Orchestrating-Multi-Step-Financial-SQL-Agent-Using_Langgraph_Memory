from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.sql_database import SQLDatabase
from langchain.chat_models import ChatOpenAI

from memory.vector_store import VectorMemory

llm = ChatOpenAI(temperature=0)

class QueryAgent:
    def __init__(self):
        self.db = SQLDatabase.from_uri("sqlite:///data/sample_financial_data.db")
        self.memory = VectorMemory()
        self.agent = create_sql_agent(
            llm=llm,
            toolkit=SQLDatabaseToolkit(db=self.db, llm=llm),
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
        )

    def run_query(self, user_input):
        context = self.memory.retrieve(user_input)
        return self.agent.run(f"User query: {user_input}\nMemory context: {context}")
