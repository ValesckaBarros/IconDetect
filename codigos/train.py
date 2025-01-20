from ultralytics import YOLO


# Carregar o modelo YOLOv8 com pesos pré-treinados
model = YOLO('yolov8s.pt') 

# Caminho para o dataset 
dataset_path = '/kaggle/input/detect-icons-v11/data.yaml' 

# Treinar o modelo em múltiplas GPUs
model.train(
    data=dataset_path,
    epochs=150,
    imgsz=(434, 930),           # Tamanho das imagens no formato (width, height)
    batch=16,
    device='0,1',
    lr0=0.01,
    patience=0,
    augment=True,
    project='resultados_treino4',
    name='experimento_v4',
    optimizer='AdamW'
)