import cv2
import os
import numpy as np

# leitura da imagem
caminho_imagem = 'faces/image_0001.jpg' #onde a imagem está localizada no disco
img = cv2.imread(caminho_imagem) #lê a imagem

# codificação para bytes
_, img_bytes = cv2.imencode('.jpg', img) #transforma a imagem em bytes
img_bytes = bytes(img_bytes)
tamanho_da_imagem_codificado = len(img_bytes).to_bytes(4, 'big') #protocolo manda o tamanho da imagem e depois a imagem

# decodificação
tam = int.from_bytes(tamanho_da_imagem_codificado, 'big') #decodifica tamanho
img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR) #decodifica imagem


# processamento
xml_classificador = os.path.join(os.path.relpath( 
    cv2.__file__).replace('__init__.py', ''), 'data\haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(
    xml_classificador)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Desenha retângulos nas áreas onde as faces foram detectadas
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


cv2.imshow('Imagem Processada', img) #exibindo imagens na tela
cv2.waitKey(0)
cv2.destroyAllWindows()
