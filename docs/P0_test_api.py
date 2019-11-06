import requests, json
import numpy as np
from tqdm import tqdm
    
url = 'http://127.0.0.1:8000/'
r = requests.get(url)
print(r.content.decode('utf-8'))
#######################################################

url = 'http://127.0.0.1:8000/render'
data = {'a0' : 0.0, 'a1':1.0}
r = requests.post(url,json=data)

raw_bytes = r.content

import cv2
#img = cv2.imdecode(raw_bytes, 0)
bytes_as_np_array = np.frombuffer(raw_bytes, dtype=np.uint8)
img = cv2.imdecode(bytes_as_np_array, 1)
print(img)
cv2.imshow('image',img)
cv2.waitKey(0)
exit()
raw_bytes = cv2.imencode(".jpg", img, encode_param)[1].tostring()
print(r.status_code)
print(r.content)
#for _ in tqdm(range(10**5)):
#    
#    print(r.content)



