from fabric.api import local

def serve():
     local("uvicorn API:app --reload --reload-dir '.'")
