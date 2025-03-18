# 📊 Market Intelligence with CrewAI

This project utilizes **CrewAI**, **Ollama (Llama 3.1)**, and **Streamlit** to analyze market trends and generate AI-driven strategies based on real-time data from **Alpha Vantage**.

---

## 📂 Project Structure

The following structure outlines the organization of files within the **PUBLISH_GENERATIVE** project.  
Each file and directory serves a specific function for the correct execution of the market analysis system.

```
PUBLISH_GENERATIVE/        # Root directory of the project
│-- app/                   # Core application folder
│   │-- __pycache__/       # Compiled Python files
│   │-- __init__.py        # Marks the directory as a Python package
│   │-- agents.py          # Defines AI agents in CrewAI
│   │-- main.py            # Main script to run the application
│   │-- tasks.py           # Defines tasks assigned to the agents
│   │-- utils.py           # Utility functions for the project
│-- data/                  # Folder for storing data files
│-- venv/                  # Virtual environment (should be added to .gitignore)
│-- .env                   # Environment variables file (API keys, configurations)
│-- .gitignore             # File to exclude unnecessary elements in Git
│-- structure.md           # Document explaining the project structure
│-- README.md              # Main documentation file
│-- requirements.txt       # Dependencies required for the project
```

---

## 🚀 Features

✅ **Real-time market trend analysis** with **Alpha Vantage** data.  
✅ **AI-based marketing strategy generation**.  
✅ **Financial feasibility assessment** of business strategies.  
✅ **Implemented using AI agents** with **CrewAI**.  
✅ **Interactive interface with Streamlit**.

---

## 🔑 Alpha Vantage API Key Setup

To use real-time market data, you need to configure your **API Key** from **Alpha Vantage**.

### 1️⃣ Obtain Your API Key
- Go to [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and register for a free API Key.

### 2️⃣ Configure the Token in a `.env` File
- In the root directory of the project (`Publish_Generative`), **create a file named `.env`**.
- **Open `.env` in a text editor** and add the following line:

  ```plaintext
  ALPHA_VANTAGE_API_KEY=YOUR_API_KEY_HERE
  ```

---

## 📥 Installation and Execution

Follow these steps to set up and run the project:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/surribasg/Publish_Generative.git
cd Publish_Generative
```

### 2️⃣ Install Ollama and Llama 3.1
Ollama is required to run Llama 3.1 locally.

- **For macOS and Linux, run:**
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```
- **For Windows, download and install from:**
  [https://ollama.com/download](https://ollama.com/download)

- **Download the Llama 3.1 model:**
  ```bash
  ollama pull llama3
  ```

- **Run Ollama Serve (to use it as a local API):**
  ```bash
  ollama serve
  ```

### 3️⃣ Install Dependencies in a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux  
venv\Scripts\activate  # Windows  
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

---

## 📊 How It Works

This system uses **CrewAI** to automate stock market analysis through specialized AI agents:

1. **Market Analyst:** Identifies market trends and stock patterns.
2. **Marketing Strategist:** Develops a marketing strategy based on detected trends.
3. **Financial Consultant:** Evaluates the economic feasibility of the proposed strategies.

Each agent works independently, leveraging AI to generate insights and business recommendations.

---

## 📝 Contribution & Improvements

This project is open for improvement! You can:
- Optimize agent prompts
- Add new data sources
- Integrate additional financial analysis techniques

If you have ideas for making the system more efficient, feel free to collaborate!

🔗 **GitHub Repository:** [https://github.com/surribasg/Publish_Generative](https://github.com/surribasg/Publish_Generative)
