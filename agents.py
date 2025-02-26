import json
from langchain_groq import ChatGroq
from langchain_core.tools import Tool
from langchain.agents import AgentType, initialize_agent
from langchain_community.utilities import GoogleSerperAPIWrapper

# ✅ Manually pass API keys


SERPER_API_KEY="your_serper_api_key"
GROQ_API_KEY="your_groq_api_key"


class SummarizerAgent:
    """Breaks down a topic into structured subtopics using Groq LLM"""

    def __init__(self, model="mixtral-8x7b-32768"):
        self.llm = ChatGroq(model_name=model, api_key=GROQ_API_KEY)

    def summarize(self, topic: str) -> dict:
        """Breaks the topic into subtopics with explanations."""
        prompt = f"""
        Break down the following topic into structured subtopics, each with a short explanation.
        Format the response as JSON with 'subtopics' as the key.

        Topic: {topic}

        Example JSON Output:
        {{
            "subtopics": {{
                "Definition": "What this topic is about...",
                "Key Principles": "Important concepts within the topic...",
                "Applications": "Where this topic is used...",
                "Challenges": "Difficulties and limitations..."
            }}
        }}

        Respond ONLY with valid JSON. Do NOT include any other text.
        """
        response = self.llm.invoke(prompt)

        # ✅ Ensure valid JSON response
        try:
            result = json.loads(response.content)
            return result.get("subtopics", {"error": "Unexpected response format"})
        except json.JSONDecodeError:
            return {"error": "Could not parse response"}

class FlashcardAgent:
    """Converts key concepts into flashcards using Groq LLM"""

    def __init__(self, model="mixtral-8x7b-32768"):
        self.llm = ChatGroq(model_name=model, api_key=GROQ_API_KEY)

    def generate_flashcards(self, key_concepts: list) -> dict:
        """Creates flashcards based on extracted key concepts."""
        if not key_concepts:
            return {"error": "No key concepts provided."}

        prompt = f"""
        Convert these key concepts into a dictionary of flashcards.
        Each key should be a question, and the value should be an answer.

        Key Concepts: {key_concepts}

        Example JSON Output:
        {{
            "What is Concept 1?": "Definition of Concept 1",
            "How does Concept 2 work?": "Explanation of Concept 2"
        }}

        Respond ONLY with valid JSON. Do NOT include any other text.
        """
        response = self.llm.invoke(prompt)

        # ✅ Ensure valid JSON response
        try:
            return json.loads(response.content)
        except json.JSONDecodeError:
            return {"error": "Failed to parse flashcard response."}

class WebSearchAgent:
    """Uses GoogleSerperAPIWrapper for intelligent web search"""

    def __init__(self):
        self.search_tool = GoogleSerperAPIWrapper(serper_api_key=SERPER_API_KEY)

    def search_resources(self, topic: str) -> list:
        """Finds study resources using Serper API."""
        return self.search_tool.run(topic)


class WebSearchAgent:
    """Agent 3: Uses GoogleSerperAPIWrapper for intelligent web search"""

    def __init__(self):
        self.search_tool = GoogleSerperAPIWrapper(serper_api_key=SERPER_API_KEY)  # ✅ Pass API key directly

        # ✅ Use a standard conversational agent instead of Self-Ask
        self.agent = initialize_agent(
            tools=[
                Tool(
                    name="Web Search",
                    func=self.search_tool.run,
                    description="Finds web resources using GoogleSerper API."
                )
            ],
            llm=ChatGroq(model_name="mixtral-8x7b-32768", api_key=GROQ_API_KEY),
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # ✅ More stable than Self-Ask
            verbose=True,
            handle_parsing_errors=True  # ✅ Enables retry on parsing failures
        )

    def search_resources(self, topic: str) -> list:
        """Finds study resources using the conversational agent."""
        try:
            search_results = self.agent.run(topic)
            return [{"title": search_results, "url": "N/A"}] if search_results else []
        except Exception as e:
            print(f"❌ Error in search agent: {e}")
            return [{"title": "Error fetching results", "url": "N/A"}]