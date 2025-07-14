from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from currency_tools import convert_currency, list_supported_currencies

llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash-latest",
    google_api_key="AIzaSyAI5zSce0uDo3pX64xdMG0KiojRf3CckzQ"
)

tools = [convert_currency, list_supported_currencies]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,  # ✅ Fix here
    verbose=True
)
