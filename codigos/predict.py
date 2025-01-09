from ultralytics import YOLO  # Certifique-se de ter o pacote ultralytics instalado
import os

# Caminho para o modelo treinado
model = YOLO("treino7_3797img_150epochs/experimento_v4/weights/best.pt")  # Caminho para o modelo

# Caminho da pasta contendo as imagens de entrada
image_folder = 'C:/Users/vrmsb/Desktop/take_picture/cropped_images-realme'  # Substitua pelo caminho da pasta

# Caminho para salvar os resultados
output_folder = 'resultados'  # Substitua pelo caminho onde deseja salvar os resultados
os.makedirs(output_folder, exist_ok=True)  # Cria a pasta de saída se não existir

# Parâmetros para a predição
iou_threshold = 0.3
conf_threshold = 0.25

# Iterar por todas as imagens na pasta
for file_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, file_name)

    # Verifica se é um arquivo de imagem
    if os.path.isfile(image_path) and file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        print(f"Processando: {file_name}")

        # Realizar a predição
        results = model.predict(
            source=image_path,
            save=True,
            save_txt=True,
            show=False,
            save_dir=output_folder,  # Define o local de saída
            iou=iou_threshold,
            conf=conf_threshold
        )

print("Processamento concluído!")