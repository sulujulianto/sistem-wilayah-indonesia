import uvicorn
import argparse
from app.main import app

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sistem Informasi Wilayah Indonesia API")
    parser.add_argument("--host", default="127.0.0.1", help="Host untuk server")
    parser.add_argument("--port", type=int, default=8000, help="Port untuk server")
    args = parser.parse_args()
    
    uvicorn.run(app, host=args.host, port=args.port)