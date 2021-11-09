from typing import Any, List, Optional, Tuple, Union

import cv2
import numpy as np


def imread(filename: str, flags: int = cv2.IMREAD_COLOR) -> Optional[np.ndarray]:
    img = cv2.imread(filename, flags)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def imwrite(filename: str, img: np.ndarray, params: List[int] = list()) -> bool:
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return cv2.imwrite(filename, img_bgr, params)


def imdecode(buf: np.ndarray, flags: int = cv2.IMREAD_COLOR) -> Optional[np.ndarray]:
    img = cv2.imdecode(buf, flags)
    if img is None:
        return None
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def imencode(extension: str, img: np.ndarray, params: List[int] = list()) -> Tuple[bool, Optional[np.ndarray]]:
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return cv2.imencode(extension, img_bgr, params)


class VideoCapture:

    def __init__(self, filename_or_camera_index: Union[str, int, None] = None,
                 apiPreference: int = cv2.CAP_ANY, params: List[int] = list()):
        if filename_or_camera_index is None:
            self.__cap = cv2.VideoCapture()
        else:
            self.__cap = cv2.VideoCapture(filename_or_camera_index, apiPreference, params)

    def read(self) -> Tuple[bool, Optional[np.ndarray]]:
        success, image = self.__cap.read()
        if success is True:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return success, image

    def retrieve(self, image: Optional[np.ndarray] = None, flags: int = 0) -> Tuple[bool, Optional[np.ndarray]]:
        success, image = self.__cap.retrieve(image, flags)
        if success is True:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return success, image

    def __getattr__(self, name: str) -> Any:
        return getattr(self.__cap, name)


def __getattr__(name: str) -> Any:
    return getattr(cv2, name)
