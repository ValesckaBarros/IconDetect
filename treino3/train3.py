from ultralytics import YOLO

# Caminho para o dataset 
dataset_path = 'C:/Users/vrmsb/Documents/GitHub/IconDetect/dataset1/data.yaml'  

# Carregar o modelo YOLOv8 com pesos pré-treinados
model = YOLO('yolov8s.pt')  # Experimente outras versões yolov8m.pt ou yolov8l.pt

# Treinar o modelo
model.train(
    data=dataset_path,          # Pasta onde estão os arquivos de treino, teste e validação
    epochs=10,                  # Número de épocas
    imgsz=800,                  # Tamanho das imagens de entrada
    batch=16,                   # Tamanho do batch (ajuste com base no hardware)
    device='cpu',               # Use GPU (0 para primeira GPU)
    lr0=0.01,                   # Taxa de aprendizado inicial
    patience=10,                # Early stopping após 10 épocas sem melhora
    augment=True,               # Ativa aumento de dados
    project='meus_resultados',  # Nome do diretório do projeto
    name='experimento_v3',      # Nome da experiência
    optimizer='AdamW'           # Alternativa ao otimizador padrão
)
