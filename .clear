import uvicorn
from fastapi import FastAPI
from openenv.core.env_server import create_fastapi_app 
from src.environment import MigrationEnv
from src.models import MigrationAction, MigrationObservation

# CRITICAL: We pass MigrationEnv (the class), NOT an instance like MigrationEnv()
app = create_fastapi_app(MigrationEnv, MigrationAction, MigrationObservation)

def main():
    """Entry point for the OpenEnv server."""
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=False)

if __name__ == "__main__":
    main()