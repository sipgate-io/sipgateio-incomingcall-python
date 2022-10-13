import incoming_call.server as server
from dotenv import load_dotenv
import os

load_dotenv()
WEBHOOK_PORT = os.environ.get("WEBHOOK_PORT")

if __name__ == "__main__":
    server.app.run(port=WEBHOOK_PORT)
