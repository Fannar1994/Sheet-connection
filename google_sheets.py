import gspread
from oauth2client.service_account import ServiceAccountCredentials
import openai
import os

# 🔥 Load your API key securely from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure this variable is set in your environment

# 🔥 Connect to Google Sheets API 🔥
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("gpt-sheets-key.json", scope)
client = gspread.authorize(creds)

# 🔥 Open your Google Sheet by URL 🔥
sheet_url = "https://docs.google.com/spreadsheets/d/1OR9rV2t2MBIW0FhV1mE2YZWYE5OD-xK1wxT2wx_a8Yc/edit?usp=sharing"
spreadsheet = client.open_by_url(sheet_url)
worksheet = spreadsheet.sheet1  # Using the first worksheet

# 🔥 Voice Text Input: Wrong Translation 🔥
# This is the wrong translation obtained from the voice text.
wrong_translation = "heima hjó honum"

# 🔥 Create a prompt for GPT to correct the wrong translation 🔥
prompt = f"""Réttaðu eftirfarandi rangt orðasamband og gefðu upp rétta leiðréttinguna:
Rangt orðasamband: {wrong_translation}
Rétt leiðrétting:"""

# 🔥 Call GPT to get the correct translation 🔥
response = openai.ChatCompletion.create(
    model="gpt-4",  # or use "gpt-3.5-turbo" if preferred
    messages=[
        {"role": "system", "content": "Þú ert málfræðingur sem leiðréttir rangt orðasambönd til réttrar íslenskrar málnotkunar."},
        {"role": "user", "content": prompt}
    ]
)
correct_translation = response['choices'][0]['message']['content'].strip()

# 🔥 Append the wrong and correct translation as a new row in the Google Sheet 🔥
new_row = [wrong_translation, correct_translation]
worksheet.append_row(new_row)

print("✅ New translation pair appended to the sheet!")
