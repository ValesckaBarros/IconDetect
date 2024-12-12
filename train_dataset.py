from ultralytics import YOLO

# Caminho para o dataset 
dataset_path = 'detect_clickable_icons.v1i.yolov8/data.yaml'  

# Carregar o modelo YOLOv8
model = YOLO('yolov8n')  

# Treinar o modelo
model.train(
    data=dataset_path,          # Pasta onde estão os arquivos de treino, teste e validação
    epochs=10,                  # Número de épocas
    imgsz=640,                  # Tamanho das imagens de entrada
    batch=-1,                   # Tamanho do batch
    device='cpu',               # Defina para '0' para usar a primeira GPU, ou 'cpu' para usar a CPU
    project='meus_resultados',  # Nome do diretório do projeto
    name='experimento'          # Nome da experiência
)

