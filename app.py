import uvicorn
from openenv.core.env_server import create_fastapi_app # FIXED NAME
from environment import MigrationEnv
from models import MigrationAction, MigrationObservation


app = create_fastapi_app(MigrationEnv, MigrationAction, MigrationObservation)

def main():
    uvicorn.run("app:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()