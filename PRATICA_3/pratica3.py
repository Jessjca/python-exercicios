import cv2

# Carregar a imagem colorida "coins.png"
imagem_colorida = cv2.imread('coins.png')

# Converter a imagem para escala de cinza
imagem_grayscale = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Definir um valor de limiar (threshold)
limiar = 80  # Você pode ajustar o valor do limiar conforme necessário

# Aplicar o limiar para converter os pixels abaixo do limiar em preto e os demais em branco
limiar, imagem_limiarizada = cv2.threshold(imagem_grayscale, limiar, 255, cv2.THRESH_BINARY)

# Imprimir o valor do limiar
print("Valor do Limiar:", limiar)

# Salvar a nova imagem
cv2.imwrite('nova_imagem_coins.png', imagem_limiarizada)

# Mostrar a nova imagem (opcional)
cv2.imshow('Nova Imagem', imagem_limiarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
