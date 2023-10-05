import cv2 as cv
# Jessica Costa 20.2.8006
# Carregando a imagem em formato BGR
imagem_bgr = cv.imread('LOGOTIPO.png')

# Verificando se a imagem foi carregada corretamente
if imagem_bgr is None:
    print('Não foi possível carregar a imagem.')
else:
    # O cálculo que o OpenCV faz é gray = 0.299 × Red + 0.587 × Green + 0.114 × Blue
    # Essa fórmula atribui pesos diferentes para os canais de cor vermelho, 
    # verde e azul, levando em consideração a sensibilidade do olho humano a cada cor.
    # O peso é baseado na percepção da luminância, onde o olho humano é mais sensível ao verde, 
    # seguido pelo vermelho e depois pelo azul.
    # Convertendo a imagem de BGR para tons de cinza
    imagem_gray = cv.cvtColor(imagem_bgr, cv.COLOR_BGR2GRAY)

    # Exibindo a imagem original e a imagem em tons de cinza
    cv.imshow('Imagem Original (BGR)', imagem_bgr)
    cv.imshow('Imagem em Tons de Cinza', imagem_gray)
    cv.waitKey(0)
    cv.destroyAllWindows()
