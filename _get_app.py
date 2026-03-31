channel='dev'

app_url = f"https://raw.githubusercontent.com/RJbalikian/SPRIT-HVSR/{channel}/sprit/sprit_streamlit_ui.py"

import requests
r = requests.get(app_url)
print(r.text)

with open('./streamlit_app.py', mode='w', encoding='utf-8') as f:
    f.write(r.text)