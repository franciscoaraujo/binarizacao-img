from PIL import Image
import matplotlib.pyplot as plt

def binarizar_img(input_path, threshold=127):
    # Abre a imagem e converte para tons de cinza
    img = Image.open(input_path).convert('L')
    largura, altura = img.size

    # Cria nova imagem binarizada (P&B)
    bin_img = Image.new('L', (largura, altura))

    for x in range(largura):
        for y in range(altura):
            pixel = img.getpixel((x, y))
            bin_pixel = 255 if pixel >= threshold else 0
            bin_img.putpixel((x, y), bin_pixel)

    return img, bin_img

# Caminho da imagem de entrada
entrada = 'perfil.jpg'

# Processa a imagem
original, binarizada = binarizar_img(entrada, threshold=128)

# Exibe as imagens
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Original (tons de cinza)")
plt.imshow(original, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Binarizada (P&B)")
plt.imshow(binarizada, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
