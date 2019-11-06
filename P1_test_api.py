import requests, json
import numpy as np
from tqdm import tqdm
import cv2

url = "http://127.0.0.1:8000/"
r = requests.get(url)
print(r.content.decode("utf-8"))

#######################################################

url = "http://127.0.0.1:8000/render"

for _ in tqdm(range(1000)):
    a0, a1 = np.random.uniform(-5, 5, size=(2,))
    data = {"a0": a0, "a1": a1}
    r = requests.post(url, json=data)

    raw_bytes = r.content

    bytes_as_np_array = np.frombuffer(raw_bytes, dtype=np.uint8)
    img = cv2.imdecode(bytes_as_np_array, 1)

    cv2.imshow("image", img)
    cv2.waitKey(1)
