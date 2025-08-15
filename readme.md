📄 AI Resume Analyzer using Google Gemini API

An AI-powered resume analyzer that helps job seekers improve their resumes with instant, role-specific feedback.
This tool reads resumes in PDF or TXT format, extracts text, and uses Google Gemini AI to provide actionable insights.

🚀 Features

📂 Upload PDF or TXT resumes

🤖 Analyze content with Google Gemini API

🎯 Role-specific improvement suggestions

📊 Feedback on clarity, skills, formatting, experience

🖥 Built with Streamlit for a simple, interactive interface

🛠 Tech Stack

Python

Streamlit – UI framework

PyPDF2 – PDF text extraction

Google Generative AI (Gemini) – Resume analysis

dotenv – Environment variable management

📂 Project Structure
├── main.py                # Main Streamlit app
├── requirements.txt       # Required dependencies
├── .env                   # API key storage (not uploaded to GitHub)
├── README.md              # Project documentation

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate     # On Mac/Linux
venv\Scripts\activate        # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set up Environment Variables

Create a .env file in the root folder:

GOOGLE_API_KEY=your_gemini_api_key_here


Get your API key from Google AI Studio.

5️⃣ Run the App Locally
streamlit run main.py

🌐 Deployment on Streamlit Cloud

Push your project to GitHub.

Ensure requirements.txt contains:

streamlit
PyPDF2
python-dotenv
google-generativeai


Go to Streamlit Cloud, connect your GitHub repo, and deploy.

Add GOOGLE_API_KEY as a secret in Streamlit Cloud settings.

🖼 Screenshot

(Add your project screenshot here)

📌 Example Prompt

Job Role: Software Engineer
The AI will analyze the uploaded resume and provide:

Content clarity feedback

Skill presentation improvements

Formatting suggestions

Experience enhancement tips

Role-specific recommendations