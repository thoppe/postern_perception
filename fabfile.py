from fabric.api import local

def small():
    local("xdg-open docs/small_eyes.html")


def serve():
     local("uvicorn API:app --reload --reload-dir '.'")
