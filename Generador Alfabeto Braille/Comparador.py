import os
import glob

# Directorios base
images_base = 'images'
labels_base = 'labels'

# Subcarpetas
subfolders = ['train', 'validation']

# Extensiones esperadas para las imágenes y etiquetas
image_extensions = ['.jpg', '.png', '.jpeg']
label_extension = '.txt'

def get_base_name(filename):
    """
    Devuelve el nombre base del archivo sin extensión.
    Por ejemplo, "a_1.png" -> "a_1"
    """
    return os.path.splitext(os.path.basename(filename))[0]

for sub in subfolders:
    images_dir = os.path.join(images_base, sub)
    labels_dir = os.path.join(labels_base, sub)

    # Obtener todas las imágenes en la carpeta actual (train o validation)
    # Filtramos por extensiones de imágenes
    image_files = []
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(images_dir, '*' + ext)))

    for img_path in image_files:
        img_base = get_base_name(img_path)
        
        # Archivo de etiqueta correspondiente
        label_path = os.path.join(labels_dir, img_base + label_extension)
        
        # Si no existe el label correspondiente, eliminamos la imagen
        if not os.path.exists(label_path):
            print(f"No existe etiqueta para {img_path}, eliminando la imagen...")
            os.remove(img_path)
