# import langgraph
# from langgraph.graph import StateGraph
# from agents import SummarizerAgent, FlashcardAgent, WebSearchAgent

# class TutorBotGraph:
#     """Defines a stateless multi-agent workflow using LangGraph"""

#     def __init__(self):
#         self.summarizer = SummarizerAgent()
#         self.flashcard_gen = FlashcardAgent()
#         self.web_search = WebSearchAgent()

#         # ✅ Define a stateless graph
#         self.graph = StateGraph(dict)

#         # ✅ Define nodes (each function returns new data only)
#         self.graph.add_node("summarizer", self.run_summarizer)
#         self.graph.add_node("process_results", self.process_results)  # ✅ Merges all outputs

#         # ✅ Define edges (pass all required inputs)
#         self.graph.add_edge("summarizer", "process_results")

#         # ✅ Set entry point
#         self.graph.set_entry_point("summarizer")

#         # ✅ Compile the graph
#         self.executor = self.graph.compile()

#     # ✅ Step 1: Summarizer extracts subtopics
#     def run_summarizer(self, inputs: dict):
#         """Summarizer Agent extracts structured subtopics."""
#         topic = inputs["topic"]
#         subtopics = self.summarizer.summarize(topic)
#         return {"topic": topic, "subtopics": subtopics}  # ✅ Ensures topic is always included

#     # ✅ Step 2: Generate flashcards and fetch web search results
#     def process_results(self, inputs: dict):
#         """Generates flashcards and fetches web resources in one step to avoid update conflicts."""
#         topic = inputs["topic"]
#         subtopics = inputs["subtopics"]

#         # ✅ Generate flashcards
#         subtopic_names = list(subtopics.keys()) if subtopics else []
#         flashcards = self.flashcard_gen.generate_flashcards(subtopic_names)

#         # ✅ Fetch web search results
#         resources = self.web_search.search_resources(topic)

#         return {
#             "subtopics": subtopics,
#             "flashcards": flashcards,
#             "resources": resources
#         }  # ✅ Returns everything at once to prevent multiple updates per step

#     def run(self, topic: str):
#         """Executes the LangGraph multi-agent workflow (Fully Stateless)."""
#         initial_inputs = {"topic": topic}  # ✅ Explicitly passing topic, no state tracking
#         return self.executor.invoke(initial_inputs)  # ✅ Ensures execution is stateless



import langgraph
from langgraph.graph import StateGraph
from agents import SummarizerAgent, FlashcardAgent, WebSearchAgent

class TutorBotGraph:
    """Defines a stateless multi-agent workflow using LangGraph with Human-in-the-Loop (HITL)"""

    def __init__(self):
        self.summarizer = SummarizerAgent()
        self.flashcard_gen = FlashcardAgent()
        self.web_search = WebSearchAgent()

        # ✅ Define a stateless graph
        self.graph = StateGraph(dict)

        # ✅ Define nodes (each function returns new data only)
        self.graph.add_node("summarizer", self.run_summarizer)
        self.graph.add_node("human_review", self.human_review)  # ✅ HITL Step
        self.graph.add_node("process_results", self.process_results)

        # ✅ Define edges (pass data explicitly)
        self.graph.add_edge("summarizer", "human_review")  # AI → Human Review
        self.graph.add_edge("human_review", "process_results")  # Human Review → Final Processing

        # ✅ Set entry point
        self.graph.set_entry_point("summarizer")

        # ✅ Compile the graph
        self.executor = self.graph.compile()

    # ✅ Step 1: Summarizer extracts subtopics
    def run_summarizer(self, inputs: dict):
        """Summarizer Agent extracts structured subtopics."""
        topic = inputs["topic"]
        subtopics = self.summarizer.summarize(topic)
        return {"topic": topic, "subtopics": subtopics}  # ✅ Ensures topic is always included

    # ✅ Step 2: Human-in-the-Loop Review
    def human_review(self, inputs: dict):
        """Human reviews and optionally modifies AI-generated subtopics."""
        topic = inputs["topic"]
        subtopics = inputs["subtopics"]

        # 🔹 Present subtopics for review
        print("\n👀 Review AI-generated subtopics:")
        for subtopic, explanation in subtopics.items():
            print(f"- {subtopic}: {explanation}")

        # 🔹 Allow manual changes
        user_input = input("\nDo you want to modify subtopics? (yes/no): ").strip().lower()
        if user_input == "yes":
            edited_subtopics = {}
            print("\n✍️ Enter revised subtopics (leave blank to keep unchanged):")
            for subtopic, explanation in subtopics.items():
                new_text = input(f"{subtopic} ({explanation}): ").strip()
                edited_subtopics[subtopic] = new_text if new_text else explanation
            subtopics = edited_subtopics

        return {"topic": topic, "subtopics": subtopics}  # ✅ Pass reviewed subtopics forward

    # ✅ Step 3: Generate flashcards & fetch web search results
    def process_results(self, inputs: dict):
        """Generates flashcards and fetches web resources in one step to avoid update conflicts."""
        topic = inputs["topic"]
        subtopics = inputs["subtopics"]

        # ✅ Generate flashcards
        subtopic_names = list(subtopics.keys()) if subtopics else []
        flashcards = self.flashcard_gen.generate_flashcards(subtopic_names)

        # ✅ Fetch web search results
        resources = self.web_search.search_resources(topic)

        return {
            "subtopics": subtopics,
            "flashcards": flashcards,
            "resources": resources
        }  # ✅ Returns everything at once to prevent multiple updates per step

    def run(self, topic: str):
        """Executes the LangGraph multi-agent workflow (Fully Stateless + HITL)."""
        initial_inputs = {"topic": topic}  # ✅ Explicitly passing topic, no state tracking
        return self.executor.invoke(initial_inputs)  # ✅ Ensures execution is stateless
