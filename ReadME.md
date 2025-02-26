# **📚 TutorBot - AI-Powered Learning Assistant**  

Welcome to **TutorBot**, an AI-powered learning assistant built with **LangGraph**, **Flask**, and **Groq LLMs**.  
TutorBot generates **structured learning materials, flashcards, and web resources** based on user input, with **Human-in-the-Loop (HITL) review** for enhanced learning!  

🚀 **Features:**  
✔️ **Multi-Agent System** using LangGraph  
✔️ **AI-Generated Learning Summaries**  
✔️ **Auto-Generated Flashcards** for better retention  
✔️ **Web Search Integration** using Serper API  
✔️ **Human Review Step** for refining AI results  
✔️ **Flask-Based UI** with a modern animated design  

---

## **📂 Project Structure**  
```
/FunAgents
│── /templates         # HTML files for Flask UI
│   │── index.html     # Home page with topic input
│   │── review.html    # Human review step
│   │── results.html   # Displays final learning materials
│── app.py             # Flask app
│── graphs.py          # LangGraph multi-agent workflow
│── agents.py          # AI agents (Summarizer, Flashcards, WebSearch)
│── main.py            # CLI version (Optional)
│── requirements.txt   # Python dependencies
│── README.md          # Project documentation (this file)
```

---

## **💻 Installation & Setup**  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/yourusername/TutorBot.git
cd TutorBot
```

### **2️⃣ Set Up a Virtual Environment (Recommended)**
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up API Keys**  
Create a `.env` file in the project root and add:  
```
SERPER_API_KEY=your_serper_api_key
GROQ_API_KEY=your_groq_api_key
```
Or set them manually in `app.py` and `agents.py`.

---

## **🚀 Running the Application**
### **🔹 Option 1: Run the Flask Web App**
```bash
python app.py
```
Then visit **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** in your browser.

### **🔹 Option 2: Run the CLI Version (Optional)**
```bash
python main.py
```

---

## **🛠️ How It Works**
1️⃣ **User enters a topic** on the homepage.  
2️⃣ **AI generates subtopics & learning materials** (via Groq LLM).  
3️⃣ **User reviews & edits subtopics** (HITL step).  
4️⃣ **Flashcards & web resources are generated.**  
5️⃣ **Final results are displayed with study materials.**  

---

## **🖥️ Screenshots**
### **📌 Home Page**
![Home Page](<img width="1224" alt="Screenshot 2025-02-26 at 10 30 49 AM" src="https://github.com/user-attachments/assets/4d2a3df5-8e4b-470f-83e1-b20e9af1170a" />
)  

### **📌 Human Review Step**
![Review Step](<img width="1219" alt="image" src="https://github.com/user-attachments/assets/ac737e15-a815-4272-a113-cd02c408d3f4" />
)  

### **📌 Final Results**
![Results Page](![Capture-2025-02-26-103130](https://github.com/user-attachments/assets/a156115a-c29e-4b1c-af31-a6744d5b51a6)
)
![Results](https://github.com/user-attachments/assets/5e5587ed-e8c7-4d10-bbe3-ee3ecdf8f331)


---

## **🔑 Technologies Used**
| **Technology** | **Purpose** |
|--------------|-------------|
| **LangChain** | Multi-agent workflow with LangGraph |
| **Flask** | Web UI for interactive learning |
| **Groq LLM (Mixtral-8x7B)** | AI-powered summarization & flashcard generation |
| **Serper API** | Web search integration |
| **HTML & CSS** | Fancy gradient animations for UI |

---

## **🎯 Future Improvements**
✅ **User Authentication** (Save study history)  
✅ **Downloadable PDFs of Learning Material**  
✅ **More AI Agents** (Quiz Generator, Code Explainer)  
✅ **Speech-to-Text Input for Topics**  

---

## **🤝 Contributing**
Want to contribute? 🎉 Fork the repo & submit a PR!  
```bash
git clone https://github.com/yourusername/TutorBot.git
cd TutorBot
git checkout -b feature-branch
```

---

## **📜 License**
MIT License © 2025 [Your Name](https://github.com/yourusername)

---

### **🚀 Ready to Learn Smarter? Start TutorBot Now!**  
```bash
python app.py
```
📚🔥
