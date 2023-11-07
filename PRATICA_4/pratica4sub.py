import cv2
import numpy as np

# Carregar as duas imagens
image1 = cv2.imread('coins.png')
image2 = cv2.imread('coins2.png')

# Verificar se as imagens têm o mesmo tamanho
if image1.shape == image2.shape:
    # Realizar a operação de subtração das duas imagens
    result = cv2.subtract(image1, image2)

    # Mostrar a nova imagem
    cv2.imshow('Resultado da Subtração', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Salvar a nova imagem
    cv2.imwrite('resultado_subtracao.png', result)
else:
    print('As imagens têm tamanhos diferentes e não podem ser subtraídas.')
