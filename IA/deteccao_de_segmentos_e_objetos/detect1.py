import os
import subprocess

import cv2
import matplotlib.pyplot as plt


def predictImage(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Não achei a imagem em: {image_path}")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()


# ajuste esse caminho para onde está seu darknet clonado localmente

darknet_dir = "/home/debianjv/darknet"
darknet_exe = os.path.join(darknet_dir, "darknet")  # caminho absoluto do binário

subprocess.run(
    [darknet_exe, "detect", "cfg/yolov3.cfg", "yolov3.weights", "data/dog.jpg"],
    cwd=darknet_dir,
    check=True,
)

predictImage(os.path.join(darknet_dir, "predictions.jpg"))
