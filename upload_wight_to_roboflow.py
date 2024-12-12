import roboflow

# Inicializa o cliente do Roboflow com a sua API Key. Substitua "YOUR_API_KEY_HERE" pela sua chave de API obtida no Roboflow.
rf = roboflow.Roboflow(api_key="3ky4agwNennrYm6hr0FC")

# Acesse o projeto que você criou no Roboflow. Substitua "PROJECT_ID" pelo identificador do seu projeto.
project = rf.workspace().project("detect_clickable_icons")

# Carregue a versão do projeto. Substitua "VERSION_ID" pelo número da versão que você deseja usar para fazer o deploy.
version = project.version(1)

# Faz o deploy do modelo. Especifique o tipo do modelo ("yolov8" ou outro suportado), o caminho para os resultados do treinamento, 
# e o nome do arquivo de pesos (opcional, por padrão "weights/best.pt").
version.deploy("yolov8", "meus_resultados/experimento3/weights", "best.pt")

