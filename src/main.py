import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    uvicorn.run("server.app:app", port=int(os.environ.get('BACKEND_PORT')), host=os.environ.get('BACKEND_IP'))
