import asyncio
import os
import json
from aiocoap import Context, Message, POST
from dotenv import load_dotenv
from datetime import datetime, timezone

class TimeFormatter:
    @staticmethod
    def get_iso8601() -> str:
        """Returns current time in ISO 8601 format with milliseconds and Z"""
        return datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace("+00:00", "Z")


class CoAPClient:
  def __init__(self, server_url: str):
      self.server_url = server_url

  async def post(self, payload: str) -> str:
      context = await Context.create_client_context()

      request = Message(code=POST, uri=self.server_url, payload=payload.encode('utf-8'))

      try:
          response = await context.request(request).response
          return response.payload.decode('utf-8')
      except Exception as e:
          return f"Request failed: {e}"

# def main():
#     # Load environment variables
#     load_dotenv()
#     server_url = os.getenv("COAP_SERVER")
#     tf = TimeFormatter()
#     print("ISO 8601:", tf.get_iso8601())

#     if not server_url:
#         print("Missing COAP_SERVER in .env")
#         return

#     print(f"Server URL from .env: {server_url}")

#     client = CoAPClient(server_url)
#     payload_dict = {
#       "type": "data",
#       "source": "Coral Dev Board",
#       "local_time":  tf.get_iso8601(),
#       "vehicle_count": 2,
#     }

#     coap_payload = json.dumps(payload_dict)

#     response = asyncio.run(client.post(coap_payload))
#     print("Response:", response)

# if __name__ == "__main__":
#     main()
