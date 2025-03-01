import gspread
from oauth2client.service_account import ServiceAccountCredentials
import openai
import datetime
import os

# 🔥 Load API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure API key is stored in an environment variable

# 🔥 1. Connect to Google Sheets API 🔥
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("gpt-sheets-key.json", scope)
client = gspread.authorize(creds)

# 🔥 2. Open Google Sheet 🔥
spreadsheet = client.open("Leiðréttingalisti GPT")  # Ensure this is the correct name
worksheet = spreadsheet.sheet1  # Select first sheet

# 🔥 3. Data for logging 🔥
dagsetning = datetime.datetime.today().strftime('%Y-%m-%d')  # Default to today's date
verkefni = "Skipta um blöndunartæki"
vinnustundir = 8
verkfæri = "Rafhlöðuborvél, skiptilykill"
athugasemdir = "Viðskiptavinur óskaði eftir sérstakri uppsetningu"

# 🔥 4. Correct Icelandic text using GPT 🔥
prompt = f"""Leiðréttu eftirfarandi vinnuskýrslu í réttu íslensku máli:
Dagsetning: {dagsetning}
Verkefni: {verkefni}
Vinnustundir: {vinnustundir}
Verkfæri: {verkfæri}
Athugasemdir: {athugasemdir}
"""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "system", "content": "Leiðréttu textann í réttu íslensku máli án þess að breyta merkingu."},
              {"role": "user", "content": prompt}]
)

leiðrétt_athugasemdir = response['choices'][0]['message']['content']

# 🔥 5. Write data to Google Sheets 🔥
new_row = [dagsetning, verkefni, vinnustundir, verkfæri, leiðrétt_athugasemdir]
worksheet.append_row(new_row)

print("✅ Vinnuskýrsla hefur verið skráð með leiðréttingu GPT!")
