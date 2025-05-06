from langgraph.graph import StateGraph
from agents.orchestrator import Orchestrator

class LangGraphApp:
    def __init__(self):
        self.orchestrator = Orchestrator()
        self.graph = StateGraph()
        self.graph.add_node("handle_query", self.orchestrator.handle_query)
        self.graph.set_entry_point("handle_query")

    def execute(self, user_input):
        return self.graph.run({"input": user_input})
