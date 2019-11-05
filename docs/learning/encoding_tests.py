from tqdm import tqdm
import cv2
from PIL import Image
from io import BytesIO
from turbojpeg import TurboJPEG, TJPF_GRAY, TJSAMP_GRAY, TJFLAG_PROGRESSIVE

n_tests = 10 ** 5

f_img = "sample.jpg"
img = cv2.imread(f_img)
img2 = Image.open(f_img)


def cv2_test(img):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    raw_bytes = cv2.imencode(".jpg", img, encode_param)[1].tostring()
    # raw_bytes = cv2.imencode('.png', img)[1].tostring()
    return raw_bytes


def file_read_test(img):

    with open(f_img, "rb") as FIN:
        raw_bytes = FIN.read()

    return raw_bytes


def PIL_test(x):
    byte_io = BytesIO()
    raw_bytes = img2.save(byte_io, "JPEG")

    return raw_bytes


def TurboTest(img):
    raw_bytes = jpeg.encode(img, quality=90)
    return raw_bytes


jpeg = TurboJPEG("/opt/zoom/libturbojpeg.so")

test = cv2_test
# test = file_read_test
# test = PIL_test
# test = TurboTest

# print(test(img))
# exit()

for _ in tqdm(range(n_tests)):
    test(img)
