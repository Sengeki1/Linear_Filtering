import numpy as np
import matplotlib.pyplot as plt


def convolucao(imagem, filtro):
    altura, largura = imagem.shape
    f_altura, f_largura = filtro.shape
    resultado = np.zeros_like(imagem)

    for y in range(altura - f_altura + 1):
        for x in range(largura - f_largura + 1):
            janela = imagem[y:y+f_altura, x:x+f_largura]
            resultado[y, x] = np.sum(janela * filtro)

    return resultado

imagem = input("/home/rafael2883/Pictures/Horario.png")

filtro = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]]) / 9

imagem_filtrada = convolucao(imagem, filtro)

plt.imshow(imagem_filtrada, cmap='gray')
plt.show()