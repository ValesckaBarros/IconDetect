import cv2
import os

def break_video_into_images(video_path, output_folder, frame_rate=1):
    """
    Quebra um vídeo em várias imagens, salvando cada quadro em uma pasta de saída.

    :param video_path: Caminho do vídeo.
    :param output_folder: Pasta onde as imagens serão salvas.
    :param frame_rate: Taxa de quadros (1 = salva todos os quadros, 2 = salva a cada 2 quadros, etc.).
    """
    # Verifica se a pasta de saída existe, caso contrário, cria.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Abre o vídeo
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Erro ao abrir o vídeo: {video_path}")
        return
    
    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        
        if not ret:
            break  # Sai do loop ao final do vídeo
        
        # Salva os quadros de acordo com a taxa de quadros definida
        if frame_count % frame_rate == 0:
            image_path = os.path.join(output_folder, f"{output_folder}_{saved_count:04d}.jpg")
            cv2.imwrite(image_path, frame)
            print(f"Salvando {image_path}")
            saved_count += 1
        
        frame_count += 1
    
    cap.release()
    print(f"Processamento concluído. {saved_count} imagens salvas na pasta '{output_folder}'.")

# Exemplo de uso
video_path = "C:/Users/vrmsb/Pictures/Camera Roll/realme4.mp4"  # Substitua pelo caminho do seu vídeo
output_folder = "realme4"      # Pasta onde as imagens serão salvas
frame_rate = 50                # Salva a cada 5 quadros (ajuste conforme necessário)

break_video_into_images(video_path, output_folder, frame_rate)
