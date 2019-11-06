'''
uvicorn API:app --reload --reload-dir '.'

'''

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response
from starlette.middleware.cors import CORSMiddleware
import cv2
import numpy as np

from P0_generate_samples import eyeGAN

G = eyeGAN()

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


class Coordinate(BaseModel):
    a0: float
    a1: float
    f_img: str = "sample.jpg" 


@app.get("/")
def read_root():
    return "eyeGAN"


@app.post("/render")
def render(coord: Coordinate):
    print(coord)
    
    # Multiple images can be generated, here just serve one
    imgs = G(coord.f_img, [coord.a0], [coord.a1])

    # Take on the first (and only!) image
    img = imgs.reshape(*imgs.shape[1:])

    # Image is served as floats from [-1, 1], convert to uint8
    img += 1
    img *= 127.5
    img = img.astype(np.uint8)

    # Encoded with cv2, fix colorspace
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Encode with fixed quality
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    raw_bytes = cv2.imencode(".jpg", img, encode_param)[1].tostring()

    return Response(raw_bytes, media_type="image/jpg")
