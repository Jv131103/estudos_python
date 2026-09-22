import os
import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch

sys.path.append("..")
from segment_anything import (SamAutomaticMaskGenerator, SamPredictor,
                              sam_model_registry)

# Pasta onde este script está salvo (independe de onde o terminal foi aberto)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Carregamento da imagem ---
image_path = os.path.join(BASE_DIR, 'dog.jpg')  # Altere aqui a imagem a ser segmentada
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Imagem não encontrada: {os.path.abspath(image_path)}")

image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 10))
plt.imshow(image)
plt.axis('off')
plt.show()

# --- Carregamento do modelo SAM ---
sam_checkpoint = os.path.join(BASE_DIR, "sam_vit_h_4b8939.pth")
model_type = "vit_h"

if not os.path.exists(sam_checkpoint):
    raise FileNotFoundError(
        f"Checkpoint não encontrado: {os.path.abspath(sam_checkpoint)}\n"
        "Baixe com: wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth"
    )

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Usando device: {device}")

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)

# Existem diversas configurações para o uso da biblioteca!
mask_generator_ = SamAutomaticMaskGenerator(
    model=sam,
    points_per_side=32,
    pred_iou_thresh=0.9,
    stability_score_thresh=0.96,
    crop_n_layers=1,
    crop_n_points_downscale_factor=2,
    min_mask_region_area=100,  # Requires open-cv to run post-processing
)

masks = mask_generator_.generate(image)

print(len(masks))


# Plotando tudo o que foi encontrado
def show_anns(anns):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)

    for ann in sorted_anns:
        m = ann['segmentation']
        img = np.ones((m.shape[0], m.shape[1], 3))
        color_mask = np.random.random((1, 3)).tolist()[0]
        for i in range(3):
            img[:, :, i] = color_mask[i]
        ax.imshow(np.dstack((img, m * 0.35)))


plt.figure(figsize=(10, 10))
plt.imshow(image)
show_anns(masks)
plt.axis('off')
plt.show()
