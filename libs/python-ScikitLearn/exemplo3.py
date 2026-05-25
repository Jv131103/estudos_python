from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

# Carregar o conjunto de dados
digits = load_digits()

# Exibir algumas imagens de dígitos
fig, axes = plt.subplots(1, 4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    ax.set_title(f'Target: {label}')
plt.show()
