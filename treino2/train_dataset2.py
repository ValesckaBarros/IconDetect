import os
from sklearn.model_selection import StratifiedKFold
from ultralytics import YOLO
import shutil

# Caminho para o dataset original
dataset_path = 'dataset2/original'
images_dir = os.path.join(dataset_path, 'images')
labels_dir = os.path.join(dataset_path, 'labels')

# Configurações
k_folds = 5  # Número de folds
epochs = 10  # Número de épocas
imgsz = 640  # Tamanho da imagem
batch_size = -1  # Tamanho do batch
device = 'cpu'  # Use '0' para GPU ou 'cpu' para CPU

# Listar imagens e rótulos
images = sorted(os.listdir(images_dir))
labels = sorted(os.listdir(labels_dir))

# Verificar correspondência de nomes
assert len(images) == len(labels), "Número de imagens e rótulos não coincide!"
for img, lbl in zip(images, labels):
    assert os.path.splitext(img)[0] == os.path.splitext(lbl)[0], f"{img} e {lbl} não correspondem!"

# Gerar classes a partir dos rótulos
class_labels = []
for label_file in labels:
    with open(os.path.join(labels_dir, label_file), 'r') as f:
        lines = f.readlines()
        if lines:
            first_class = int(lines[0].split()[0])
            class_labels.append(first_class)
        else:
            class_labels.append(-1)

# Configurar k-Fold Cross-Validation
kf = StratifiedKFold(n_splits=k_folds, shuffle=True, random_state=42)

for fold, (train_idx, val_idx) in enumerate(kf.split(images, class_labels)):
    print(f"\n--- Treinando para o Fold {fold + 1}/{k_folds} ---")
    
    # Criar diretórios temporários para este fold
    fold_dir = f"fold_{fold}"
    os.makedirs(fold_dir, exist_ok=True)
    fold_train_images_dir = os.path.join(fold_dir, 'images/train')
    fold_val_images_dir = os.path.join(fold_dir, 'images/val')
    fold_train_labels_dir = os.path.join(fold_dir, 'labels/train')
    fold_val_labels_dir = os.path.join(fold_dir, 'labels/val')
    os.makedirs(fold_train_images_dir, exist_ok=True)
    os.makedirs(fold_val_images_dir, exist_ok=True)
    os.makedirs(fold_train_labels_dir, exist_ok=True)
    os.makedirs(fold_val_labels_dir, exist_ok=True)

    # Mover arquivos de treino e validação para os diretórios correspondentes
    for idx in train_idx:
        shutil.copy(os.path.join(images_dir, images[idx]), fold_train_images_dir)
        shutil.copy(os.path.join(labels_dir, labels[idx]), fold_train_labels_dir)
    for idx in val_idx:
        shutil.copy(os.path.join(images_dir, images[idx]), fold_val_images_dir)
        shutil.copy(os.path.join(labels_dir, labels[idx]), fold_val_labels_dir)

    # Criar arquivo data.yaml para o fold atual
    fold_data_yaml = os.path.join(fold_dir, 'data.yaml')
    with open(fold_data_yaml, 'w') as f:
        f.write(f"""
train: {os.path.abspath(fold_train_images_dir)}
val: {os.path.abspath(fold_val_images_dir)}
nc: 8  
names: ['Checkbox', 'CommunBotton', 'DropdownList', 'NumKeyboard', 'RadioButton', 'TextField', 'TextKeyboard', 'menu']
""")

    # Treinar o modelo para este fold
    model = YOLO('yolov8n')   # Criar um modelo vazio
    model.train(
        data=fold_data_yaml,
        epochs=epochs,
        imgsz=imgsz,
        batch=batch_size,
        device=device,
        project='cross_validation_results',
        name=f'fold_{fold}',
        pretrained=False  # Treinar do zero
    )

    # Limpar os diretórios temporários após o treino (opcional)
    shutil.rmtree(fold_dir)

print("\nTreinamento completo para todos os folds!")
