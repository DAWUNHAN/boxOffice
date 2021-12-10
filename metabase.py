# You'll need to install PyJWT via pip 'pip install PyJWT' or your project packages file

import jwt
import time

METABASE_SITE_URL = "http://boxoffice-ai.herokuapp.com"
METABASE_SECRET_KEY = "5337d57cec94b5492d64df309bdbf1484a7b339c501efb3eed96501729b5bcee"

payload = {
  "resource": {"dashboard": 6},
  "params": {
    
  },
  "exp": round(time.time()) + (60 * 10) # 10 minute expiration
}
token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token + "#bordered=true&titled=true"