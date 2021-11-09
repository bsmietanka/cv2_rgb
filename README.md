# OpenCV RGB

This project is a python wrapper over OpenCV library that overrides IO operations so that they work on RGB (not BGR) images by default. Main goal is to mitigate all those pesky bugs when combining operations from multiple computer vision libraries.

## Getting Started

Install the package:

`pip install cv2-rgb`

And replace cv2 packages in your project:

```python
import cv2_rgb as cv2

img_rgb = cv2.imread("file.png")
```
