import os

import cv2
import cv2_rgb
import numpy as np

def test_other_cv2_methods():
    assert cv2_rgb.cvtColor == cv2.cvtColor
    assert cv2_rgb.blur == cv2.blur
    assert cv2_rgb.Sobel == cv2.Sobel

def test_imread_imwrite():
    lena_path = "tests/lena.png"
    img_bgr = cv2.imread(lena_path)
    img_rgb = cv2_rgb.imread(lena_path)
    assert img_bgr is not None and img_rgb is not None
    assert (img_bgr[:,:,::-1] == img_rgb).all()

    path_bgr, path_rgb = "bgr.png", "rgb.png"
    cv2.imwrite(path_bgr, img_bgr)
    cv2_rgb.imwrite(path_rgb, img_rgb)

    with open(path_bgr, "rb") as f_bgr, open(path_rgb, "rb") as f_rgb:
        assert f_bgr.read() == f_rgb.read()
    os.remove(path_bgr)
    os.remove(path_rgb)

def test_imdecode_imencode():
    rng = np.random.default_rng()
    img_bgr = rng.integers(0, 256, (400, 400, 3), dtype=np.uint8)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    ret_bgr, buf_bgr = cv2.imencode(".jpg", img_bgr)
    ret_rgb, buf_rgb = cv2_rgb.imencode(".jpg", img_rgb)
    assert ret_rgb is True and ret_bgr is True
    assert (buf_bgr == buf_rgb).all()

    img_decoded_bgr = cv2.imdecode(buf_bgr, cv2.IMREAD_COLOR)
    img_decoded_rgb = cv2_rgb.imdecode(buf_rgb, cv2.IMREAD_COLOR)

    assert (img_decoded_bgr[:,:,::-1] == img_decoded_rgb).all()

def test_video_capture():
    file_path = "tests/video.mp4"
    cap_bgr = cv2.VideoCapture(file_path)
    cap_rgb = cv2_rgb.VideoCapture(file_path)

    assert cap_bgr.get(cv2.CAP_PROP_FRAME_COUNT) == cap_rgb.get(cv2.CAP_PROP_FRAME_COUNT)

    ret_bgr, frame_bgr = cap_bgr.read()
    ret_rgb, frame_rgb = cap_rgb.read()

    assert ret_bgr is True and ret_rgb is True
    assert (frame_bgr[:,:,::-1] == frame_rgb).all()

    cap_bgr.grab()
    cap_rgb.grab()

    ret_bgr, frame_bgr = cap_bgr.retrieve()
    ret_rgb, frame_rgb = cap_rgb.retrieve()

    assert ret_bgr is True and ret_rgb is True
    assert (frame_bgr[:,:,::-1] == frame_rgb).all()
