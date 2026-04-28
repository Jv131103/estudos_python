# Processamento de imagem
import numpy as np
from PIL import Image

# Carregando uma imagem e transformação em array
imagem = Image.open('./libs/python-numpy/imagem.jpeg')
img_array = np.array(imagem)

# Convertendo para escala de cinza
img_cinza = np.dot(img_array[..., :3], [0.29, 0.58, 0.11])

# Salvando a imagem em escala de cinza
img_final = Image.fromarray(img_cinza.astype('uint8'))
img_final.save('./libs/python-numpy/imagem_cinza.jpeg')
