import os
from langchain.tools import SerperSearch
from langchain_core.tools import Tool

# ✅ Read API key from environment variables
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

if not SERPER_API_KEY:
    raise ValueError("❌ Serper API key is missing! Set SERPER_API_KEY in environment variables.")

# ✅ Create a Serper-based web search tool
search_tool = Tool(
    name="Google Web Search (Serper)",
    func=SerperSearch(api_key=SERPER_API_KEY).run,
    description="Finds web resources using Google Search via Serper API."
)
