import roboflow

# Inicializa a biblioteca Roboflow usando a chave da API fornecida
rf = roboflow.Roboflow(api_key="3ky4agwNennrYm6hr0FC")

# Obtém um espaço de trabalho específico no Roboflow a partir de sua URL
workspace = rf.workspace("WORKSPACE_URL")

# Faz o upload de um conjunto de dados para um projeto (novo ou existente) no Roboflow
workspace.upload_dataset(
    "./dataset/", # Caminho para o conjunto de dados local que será enviado
    "PROJECT_ID", # Identificador do projeto; cria ou acessa o projeto com este ID
    num_workers=10, # Define o número de processos de trabalho para realizar o upload
    project_license="MIT", # Licença do projeto especificada (neste caso, MIT)
    project_type="object-detection", # Tipo do projeto (neste caso, detecção de objetos)
    batch_name=None, # Nome do lote; se None, será gerado automaticamente
    num_retries=0 # Número de tentativas caso o upload falhe
)
