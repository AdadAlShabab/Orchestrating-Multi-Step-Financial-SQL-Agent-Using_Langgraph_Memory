from langgraph_app.langgraph_flow import LangGraphApp

if __name__ == '__main__':
    app = LangGraphApp()
    query = input("Enter your financial question: ")
    result = app.execute(query)
    print("Result:\n", result)
