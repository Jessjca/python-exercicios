import cv2

# Carregar a imagem
imagem_colorida = cv2.imread('coins.png')

# Converter a imagem para escala de cinza
imagem_grayscale = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Definir um valor de limiar (threshold)
limiar = 96

# Aplicar o limiar para converter os pixels abaixo do limiar em preto
_, imagem_limiarizada = cv2.threshold(imagem_grayscale, limiar, 255, cv2.THRESH_TOZERO)

# Salvar a nova imagem
cv2.imwrite('nova_imagem.jpg', imagem_limiarizada)

# Mostrar a nova imagem (opcional)
cv2.imshow('Nova Imagem', imagem_limiarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
