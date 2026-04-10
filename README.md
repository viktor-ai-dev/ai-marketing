# ai-marketing


🚀 AI Marketing Automation

An AI-powered marketing tool that generates complete high-converting marketing campaigns for e-commerce products in seconds.
Built with Streamlit and OpenAI.

🚀 Features

📊 Full Marketing Campaign Generation
Generate an entire marketing campaign from a single input:
-Product name
-Category
-Features

🧠 AI-Generated Content Includes
-📝 Product Description
-📢 Facebook Ad Copy
-🎬 TikTok Ad Script
-📧 Email Campaign

All content is designed to be high-converting and ready to use.

⚡ One-Click Campaign Creation
-Simple UI
-Instant generation
-No marketing experience required

💾 Save Campaigns
-Export generated campaigns to a .txt file
-Easy to reuse and edit

🏗️ Tech Stack
-Streamlit
-Python
-OpenAI API (GPT-4o-mini)
-dotenv (environment management)

📂 Project Structure
project/
│── app.py
│── modules/
│   ├── generator.py
│   ├── prompts.py
│── campaign.txt
│── .env

⚙️ How It Works
1. User inputs:
    -Product name
    -Category
    -Features
2. A structured marketing prompt is generated
3. The AI creates a full campaign including:
    -Product description
    -Ads
    -Scripts
    -Emails
4. The result is displayed and can be saved locally

🔑 Environment Setup
Create a .env file:
OPENAI_API_KEY=your_api_key

▶️ Run the App
pip install -r requirements.txt
streamlit run app.py

💡 Use Cases
-E-commerce store owners
-Dropshippers
-Marketing agencies
-Content creators
-Freelancers

🧠 Key Concepts
-Prompt engineering
-AI content generation
-Marketing automation
-Structured output generation

🔥 Why This Project Matters
This project demonstrates how AI can automate entire marketing workflows, 
not just single pieces of content.

Key highlights:
-Generates multi-channel campaigns (ads + email + content)
-Uses structured prompting for consistent output
-Designed for real-world marketing use

It showcases skills in:
-AI application development
-Prompt design for business use cases
-Building practical automation tools

🛠️ Future Improvements
-Add multi-platform ads (Google, Instagram, etc.)
-Campaign customization (tone, audience, goals)
-Save campaigns to database
-UI for editing generated content
-Integration with ad platforms
