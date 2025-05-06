from agents.query_agent import QueryAgent

class Orchestrator:
    def __init__(self):
        self.agent = QueryAgent()

    def handle_query(self, user_input):
        return self.agent.run_query(user_input)
