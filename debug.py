from app import get_app
from debug_settings import DevConfig

app = get_app(DevConfig)

from flask_cors import CORS

CORS(app)

if __name__ == '__main__':
    app.run(host="192.168.128.222", port=5000, use_debugger=True, use_reloader=True, passthrough_errors=True)