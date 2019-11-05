import requests, json
from tqdm import tqdm
import cv2
import io
import numpy as np

url = "http://127.0.0.1:8000/serve_static_image"
url = "http://127.0.0.1:8000/serve_image_bytes"
url = "http://127.0.0.1:8000/serve_modified_image"

r = requests.get(url)
raw_bytes = r.content
array_buff = np.frombuffer(raw_bytes, np.uint8)
img = cv2.imdecode(array_buff, 1)


cv2.imshow("img", img)
cv2.waitKey(0)
print(img)

# np.fromstring(img_stream.read(), np.uint8)


### Examine speed which is faster, CV2, PIL or scipy for encoding to jpg?
