from ultralytics import YOLO  # Certifique-se de ter o pacote ultralytics instalado

# Caminho para o modelo treinado
model = YOLO("meus_resultados/experimento3/weights/best.pt")  # Caminho para o modelo

# Caminho da imagem de entrada
image_path = 'teste_image5.jpg'  # Caminho da imagem de teste

# Realizar a predição
results = model.predict(source=image_path, save=True, save_txt=True, show=False, iou=0.3, conf=0.25)

