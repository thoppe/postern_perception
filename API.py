from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response
from starlette.middleware.cors import CORSMiddleware
import io
import cv2

#from P0_generate_samples import eyeGAN
#G = eyeGAN()

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"],
    allow_headers=["*"]
)

class Coordinate(BaseModel):
    a0: float
    a1: float


@app.get("/")
def read_root():
    return "eyeGAN"

@app.post("/render")
def render(coord: Coordinate):
    
    f_img = 'sample.jpg'   
    img = cv2.imread(f_img)
    
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    raw_bytes = cv2.imencode(".jpg", img, encode_param)[1].tostring()
    return Response(raw_bytes, media_type='image/jpg')
    
    '''
    f_img = 'sample.jpg'
        
    with open(f_img, 'rb') as FIN:
        raw_bytes = FIN.read()
        
    return Response(raw_bytes, media_type='image/jpg')
    '''
