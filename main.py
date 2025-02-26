# from graphs import TutorBotGraph

# if __name__ == "__main__":
#     topic = "History of tea"  # Example topic

#     tutor_bot = TutorBotGraph()
#     results = tutor_bot.run(topic)  # 🚀 Runs the multi-agent workflow

#     # ✅ Extract outputs from process_results step
#     subtopics = results.get("subtopics", {})
#     flashcards = results.get("flashcards", {})
#     resources = results.get("resources", [])

#     # ✅ Print the extracted subtopics
#     print("\n🔹 Breakdown of Topic:")
#     if subtopics:
#         for subtopic, explanation in subtopics.items():
#             print(f"- {subtopic}: {explanation}")
#     else:
#         print("No subtopics extracted.")

#     # ✅ Print the generated flashcards
#     print("\n📝 Flashcards:")
#     if flashcards:
#         for question, answer in flashcards.items():
#             print(f"Q: {question}\nA: {answer}\n")
#     else:
#         print("No flashcards generated.")

#     # ✅ Print the fetched web resources
#     print("\n🔍 Web Resources (via Serper API):")
#     if resources:
#         for res in resources:
#             print(f"- {res['title']}: {res['url']}")
#     else:
#         print("No resources found.")


from graphs import TutorBotGraph

if __name__ == "__main__":
    topic = "History of silk"  # Example topic

    tutor_bot = TutorBotGraph()
    results = tutor_bot.run(topic)  # 🚀 Runs the multi-agent workflow

    # ✅ Extract outputs from process_results step
    subtopics = results.get("subtopics", {})
    flashcards = results.get("flashcards", {})
    resources = results.get("resources", [])

    # ✅ Print the extracted subtopics
    print("\n🔹 Final Breakdown of Topic (After Human Review):")
    if subtopics:
        for subtopic, explanation in subtopics.items():
            print(f"- {subtopic}: {explanation}")
    else:
        print("No subtopics extracted.")

    # ✅ Print the generated flashcards
    print("\n📝 Flashcards:")
    if flashcards:
        for question, answer in flashcards.items():
            print(f"Q: {question}\nA: {answer}\n")
    else:
        print("No flashcards generated.")

    # ✅ Print the fetched web resources
    print("\n🔍 Web Resources (via Serper API):")
    if resources:
        for res in resources:
            print(f"- {res['title']}: {res['url']}")
    else:
        print("No resources found.")

