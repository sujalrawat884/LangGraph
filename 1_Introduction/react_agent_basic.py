from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv                                                                                
from langchain_community.tools import tool
from langchain.agents import initialize_agent
from langchain_community.tools import TavilySearchResults

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

search_tool = TavilySearchResults(search_depth="basic")
tools = [search_tool]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="zero-shot-react-description",
    verbose=True,
)

agent.invoke("Tell me about the mock drill in India.")
