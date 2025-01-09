from PIL import Image
import os

def process_images(input_folder, output_folder, coordinates, rotation_angle=0):
    """
    Processa imagens em uma pasta, cortando e girando de acordo com os parâmetros fornecidos.

    Args:
        input_folder (str): Caminho para a pasta de entrada.
        output_folder (str): Caminho para a pasta de saída.
        coordinates (tuple): Coordenadas para o recorte (x1, y1, x2, y2).
        rotation_angle (int): Ângulo de rotação em graus (padrão: 0).
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                # Caminho completo da imagem
                img_path = os.path.join(input_folder, filename)
                # Carrega a imagem
                with Image.open(img_path) as img:
                    # Corta a imagem
                    cropped_img = img.crop(coordinates)
                    # Gira a imagem
                    rotated_img = cropped_img.rotate(rotation_angle, expand=True)
                    # Salva a imagem processada
                    output_path = os.path.join(output_folder, filename)
                    rotated_img.save(output_path)
                    print(f"Processada: {filename}")
            except Exception as e:
                print(f"Erro ao processar {filename}: {e}")

# Exemplo de uso
input_folder = "original_images-realme"
output_folder = "cropped_images-realme"
coordinates = (327, 246, 1772, 935)  # Exemplo de coordenadas (x1, y1, x2, y2)
rotation_angle = 90  # Ângulo de rotação em graus

process_images(input_folder, output_folder, coordinates, rotation_angle)
