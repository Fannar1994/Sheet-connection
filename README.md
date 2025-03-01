Sheet-connection
Sheet-connection is a Flask-based application that integrates Google Sheets and OpenAI’s GPT models to help improve Icelandic translations. The app reads incorrect translations (e.g., from voice input) from a Google Sheet, uses GPT to generate the correct translation, and then logs both the original and corrected translations back to the sheet.

Features
Google Sheets Integration:
Connects to a Google Sheet using a service account and gspread. Reads data and appends new rows.

OpenAI GPT Integration:
Uses OpenAI’s Chat API (GPT-4 or GPT-3.5-turbo) to correct Icelandic text based on a provided prompt.

Automated Translation Correction:
Processes "wrong translation" inputs and generates the correct translation for learning and record-keeping.

Prerequisites
Python 3.11+
Pip
A Google Cloud Project with the Google Sheets API enabled
A Service Account JSON key file (downloaded and saved as gpt-sheets-key.json in the project root)
An OpenAI API key (set as an environment variable OPENAI_API_KEY)
Installation
Clone the Repository:

bash
Copy
git clone https://github.com/Fannar1994/Sheet-connection.git
cd Sheet-connection
Create a Virtual Environment and Activate It:

bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

bash
Copy
pip install -r requirements.txt
Set Up Environment Variables:

Ensure you have your OpenAI API key set in your environment. For example, on Unix-like systems:

bash
Copy
export OPENAI_API_KEY="your_openai_api_key_here"
Google Sheets Setup:

In your Google Cloud Console, enable the Google Sheets API.
Create a service account and download the JSON key file. Save it as gpt-sheets-key.json in the root of your project.
Open your target Google Sheet and share it with the service account’s email (found in the JSON file).
Usage
Running the Application Locally
Start the Flask App:

bash
Copy
python app.py
Endpoints:

Root Endpoint:
Visit http://localhost:5000/ to see a simple "Hello, World!" message.

Generate Endpoint:
Send a POST request to http://localhost:5000/generate with a JSON payload (e.g., {"prompt": "Your prompt here"}) to trigger GPT-based text correction.

Example Workflow
The app is designed to process Icelandic translations. For example:

A voice-to-text system captures an incorrect translation like "heima hjó honum".
The app builds a prompt instructing GPT to correct this.
GPT returns the corrected translation (e.g., "Heima hjá honum").
Both the original and corrected translations are appended as a new row in your Google Sheet.
Deployment
You can deploy this app on platforms like Render:

Configure the Service:

Push your code to a Git repository.
Connect your repository to Render.
Set the necessary environment variables (e.g., OPENAI_API_KEY).
Deploy: Render will install dependencies, build your app, and provide you with a public URL (e.g., https://sheet-connection.onrender.com).

Testing: After deployment, test the endpoints (especially /generate) using tools like curl or Postman.

Customization
Model Selection:
Adjust the GPT model in your code (e.g., change between gpt-4 and gpt-3.5-turbo) depending on your needs.

Prompt & Processing:
Modify the prompt text in your code to tailor the translation correction instructions.

Sheet Structure:
If your Google Sheet structure changes, update the code that reads/writes rows accordingly.

Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements.

