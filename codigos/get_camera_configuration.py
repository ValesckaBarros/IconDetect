import cv2

# Abrir a câmera (0 indica a câmera padrão)
camera = cv2.VideoCapture(0)

# Verificar se a câmera foi aberta corretamente
if not camera.isOpened():
    print("Erro ao abrir a câmera")
else:
    # Obter várias configurações da câmera
    brilho = camera.get(cv2.CAP_PROP_BRIGHTNESS)
    contraste = camera.get(cv2.CAP_PROP_CONTRAST)
    saturacao = camera.get(cv2.CAP_PROP_SATURATION)
    matiz = camera.get(cv2.CAP_PROP_HUE)
    ganho = camera.get(cv2.CAP_PROP_GAIN)
    exposicao = camera.get(cv2.CAP_PROP_EXPOSURE)
    balanco_de_branco = camera.get(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U)
    nitidez = camera.get(cv2.CAP_PROP_SHARPNESS)
    autofoco = camera.get(cv2.CAP_PROP_AUTOFOCUS)
    zoom = camera.get(cv2.CAP_PROP_ZOOM)
    foco = camera.get(cv2.CAP_PROP_FOCUS)  # Adicionado foco aqui

    # Exibir as configurações obtidas
    print(f"Brilho: {brilho}")
    print(f"Contraste: {contraste}")
    print(f"Saturação: {saturacao}")
    print(f"Matiz: {matiz}")
    print(f"Ganho: {ganho}")
    print(f"Exposição: {exposicao}")
    print(f"Balanço de branco: {balanco_de_branco}")
    print(f"Nitidez: {nitidez}")
    print(f"Autofoco: {autofoco}")
    print(f"Zoom: {zoom}")
    print(f"Foco: {foco}")  # Exibindo o valor do foco

# Liberar a câmera
camera.release()
