# ClickableIconDetection  
Projeto de detecção de ícones clicáveis em telas de celulares, voltado para automação de testes não invasivos. Este trabalho utiliza técnicas de visão computacional e inteligência artificial para identificar elementos clicáveis, mesmo sob condições adversas, como variações de iluminação e ângulos.  

## Tecnologias  
- **Python**  
- **YOLO**  
- **OpenCV**
- **Roboflow**

## Objetivo  
Desenvolver um modelo robusto capaz de identificar ícones clicáveis em telas de celulares em tempo real, garantindo alta precisão mesmo em ambientes com interferências externas.  

## Metodologia
foram realizados alguns treinamentos em busca de obter as melhores métricas (precisão, recall e Map) segue abaixo um resumo de cada treinamento:

| **Version** | **Dataset Size** | **Image Size** | **Epochs** | **Augmentations** | **Precision** | **Recall** | **mAP-50** | **mAP-50-95** |
|-------------|-------------------|----------------|------------|--------------------|---------------|------------|-------------|----------------|
| 1           | 1590             | 800            | 150        | Flip: Vertical, Saturation: ±50%, Brightness: ±49%, Blur: Up to 9.7px | 0.762         | 0.871      | 0.839       | 0.517          |
| 2           | 3747             | 640            | 150        | Flip: Vertical, Saturation: ±50%, Brightness: ±49%, Blur: Up to 9.7px | 0.888         | 0.879      | 0.911       | 0.680          |
| 3           | 3747             | 640            | 150        | Flip: Vertical, Saturation: ±50%, Brightness: ±49%, Blur: Up to 9.7px, padding | 0.880         | 0.880      | 0.920       | 0.700          |
| 4           | 7561             | 640            | 100        | Saturation: ±50%, Brightness: ±49%, Blur: Up to 9.7px                  | 0.917         | 0.926      | 0.952       | 0.790          |
| 5           | 7561             | 640            | 150        | Saturation: ±50%, Brightness: ±49%, Blur: Up to 9.7px                  | 0.910         | 0.920      | 0.950       | 0.800          |
| 6           | 7561             | 434x930        | 100        | Saturation: ±50%, Brightness: ±49%, Blur: Up to 9.7px                  | 0.922         | 0.916      | 0.950       | 0.800          |
| 7           | 7561             | 434x930        | 150        | Saturation: ±50%, Brightness: ±49%, Blur: Up to 9.7px                  | 0.917         | 0.924      | 0.948       | 0.805          |

Mais detalhes sobre os treinamentos podem ser obtidos consultando a pasta [treinos](treinos)

## Códigos

#### [train.py](codigos/train.py)
Código responsável por treinar um modelo YOLOv8 utilizando datasets configurados. Ele inclui funcionalidades como definição de hiperparâmetros, carregamento de dados e salvamento de pesos treinados.

#### [predict.py](codigos/predict.py)
Script para realizar predições utilizando um modelo treinado. Ele aceita imagens ou vídeos como entrada e gera saídas com objetos detectados e suas respectivas classes.

#### [video_to_image.py](codigos/video_to_image.py)
Esse código foi utilizado para extrair frames de vídeos e salvá-los como imagens individuais. Foi útil para gerar as imagens do dataset.

#### [get_camera_configuration.py](get_camera_configuration/train.py)
Código que obtem os parâmetros da câmera para captura de dados. é importante que a configuração da câmera ao capturar as imagens do dataset sejam as mesmas. 

#### [download_dataset_from_roboflow.py](codigos/download_dataset_from_roboflow.py)
Script para baixar datasets diretamente da plataforma Roboflow. Facilita o acesso rápido a dados rotulados para treinamento ou validação.

#### [upload_dataset_to_roboflow.py](codigos/upload_dataset_to_roboflow.py)
Ferramenta para enviar datasets para o Roboflow. Útil para armazenar e compartilhar dados de treinamento com outras equipes ou para uso em outras sessões de treinamento.

#### [upload_weight_to_roboflow.py](codigos/upload_weight_to_roboflow.py)
Código para fazer upload de pesos de modelos treinados para o Roboflow, permitindo armazenar e compartilhar os resultados do treinamento de forma centralizada.

## Dataset
As imagens capturadas foram obtidas a partir de filmagens de interações aleatórias com diversos aplicativos dos celulares utilizados. foram utiliazados 8 modelos de celulares (Realme 11 Pro+, Xiaomi POCO M4 PRO, Xiaomi POCO X3 Pro, Xiaomi Redmi Note 12, Xiaomi 13 Lite, Samsung A34, Samsung S20FE, Moto G32 ) disponibilizados pela Rsidência em Robótica e IA.
todas as imagens capturadas estão armazenadas na pasta [**Original_images**](https://drive.google.com/drive/folders/1-AYjCTlnAyspbGdZxViw-F-SIS0umxJ2?usp=sharing).
O **[Dataset](https://drive.google.com/drive/folders/1-AYjCTlnAyspbGdZxViw-F-SIS0umxJ2?usp=sharing)** foi rotulado e revisado utilizando a plataforma Roboflow. No total foram geradas 3151 imagens rotuladas, sendo separadas 70% para treinamento, 20% para validação e 10% para teste. 
 
