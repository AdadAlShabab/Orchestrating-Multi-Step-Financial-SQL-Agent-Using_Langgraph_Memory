# Orchestrating Multi Step Financial SQL Agent Using Langgraph, LangChain, FAISS Memory, and SQLite

## 🧠 Project Overview

This repository demonstrates a production-ready architecture for a **multi-step Financial SQL Agent** using cutting-edge LLM tooling. It leverages a combination of:

- **[LangGraph](https://github.com/langchain-ai/langgraph)**: For orchestrating multi-step agent logic.
- **[LangChain](https://www.langchain.com/)**: For creating SQL agents and handling database toolkits.
- **OpenAI LLMs**: Used via `ChatOpenAI` to interpret user intent and generate SQL queries.
- **FAISS-based Vector Store**: Stores and retrieves semantic memory to provide historical context.
- **SQLite**: A lightweight SQL database backend with sample financial data.

---

## 🔍 What This Agent Can Do
- Accept natural language questions about financial data (e.g., "Show me total expenses in January").
- Retrieve contextual memory from a vector database to enrich SQL generation.
- Use LangGraph to orchestrate query steps.
- Translate the result into a clear and useful output.

---

## 🗂️ Project Structure

```
financial-sql-agent/
├── agents/
│   ├── query_agent.py       # Builds the SQL agent using LangChain + OpenAI + memory
│   └── orchestrator.py      # Orchestrates query handling
│
├── data/
│   ├── init_db.py           # Initializes SQLite with sample financial transactions
│   └── sample_financial_data.db
│
├── memory/
│   └── vector_store.py      # FAISS vector memory using OpenAI embeddings
│
├── prompts/
│   └── financial_prompt.txt # System prompt that guides the agent
│
├── langgraph_app/
│   └── langgraph_flow.py    # LangGraph setup for execution flow
│
├── main.py                 # CLI app entry point
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## 🚀 How to Run This Project

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/financial-sql-agent.git
cd financial-sql-agent
```

### 2. Create a `.env` File
Create a `.env` file in the root folder:
```
OPENAI_API_KEY=your_openai_api_key
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize the SQLite DB
```bash
python data/init_db.py
```
This will create `sample_financial_data.db` with mock transactions.

### 5. Run the App
```bash
python main.py
```
Then enter questions like:
- "What were my grocery expenses in January?"
- "Total salary received in 2024?"

---

## ⚙️ Key Components & Techniques

### ✅ LangGraph (Multi-Step Workflow)
LangGraph allows stateful orchestration between agents. Here it's used to:
- Trigger the query agent
- Manage memory and execution flow

### ✅ LangChain SQL Agent
- Automatically translates user queries into optimized SQL
- Uses `SQLDatabaseToolkit` to explore schema and generate SQL
- Uses `AgentType.ZERO_SHOT_REACT_DESCRIPTION` for efficiency

### ✅ Memory with FAISS Vector Store
- Stores and retrieves past context semantically
- `OpenAIEmbeddings` + FAISS power fast and relevant memory lookup

### ✅ OpenAI Chat Model
- Uses `ChatOpenAI(temperature=0)` for deterministic query generation
- Context is injected into the prompt dynamically

### ✅ SQLite Backend
- Lightweight and easy to explore
- Schema:
```sql
CREATE TABLE transactions (
  id INTEGER PRIMARY KEY,
  date TEXT,
  amount REAL,
  category TEXT,
  account TEXT
);
```

---

## 📌 Future Improvements
- Add multi-table schema support
- Integrate LangSmith for debugging
- Expose via REST API or Streamlit UI
- Add user authentication and persistent memory

---

## 🧑‍💻 Author
Crafted by Adad — Machine Learning Engineer.
  
Need help deploying this project or scaling it with real data? Feel free to ask!
