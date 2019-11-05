from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse, Response
import io
import numpy

app = FastAPI()


@app.get("/serve_static_image")
def static_image():
    f_img = "sample.jpg"
    return FileResponse(f_img, media_type="image/jpg")


@app.get("/serve_image_bytes")
def static_bytes():
    f_img = "sample.jpg"
    with open(f_img, "rb") as FIN:
        raw_bytes = FIN.read()

    return Response(raw_bytes, media_type="image/jpg")


@app.get("/serve_modified_image")
def serve_modified_image():

    import cv2

    f_img = "sample.jpg"
    img = cv2.imread(f_img)
    img *= 3
    raw_bytes = cv2.imencode(".jpg", img)[1].tostring()

    return Response(raw_bytes, media_type="image/jpg")
