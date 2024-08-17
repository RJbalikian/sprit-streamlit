app_url = r"https://raw.githubusercontent.com/RJbalikian/SPRIT-HVSR/main/sprit/sprit_streamlit_ui.py"

import requests
r = requests.get(app_url)
print(r.text)
