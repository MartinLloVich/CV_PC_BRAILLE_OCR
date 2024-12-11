import os
import glob

# Directorios de etiquetas
labels_base = 'labels'
subfolders = ['train', 'validation']

# Nuevas coordenadas del bounding box
x_center = 0.5
y_center = 0.5
width = 0.8
height = 0.9

for sub in subfolders:
    labels_dir = os.path.join(labels_base, sub)
    
    # Obtener todos los archivos .txt de etiquetas en la carpeta actual
    label_files = glob.glob(os.path.join(labels_dir, '*.txt'))
    
    for label_path in label_files:
        # Leer las líneas del archivo original
        with open(label_path, 'r') as f:
            lines = f.readlines()
        
        new_lines = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            # Formato original: class x_center y_center width height
            # Mantener class_id, cambiar resto
            class_id = parts[0]
            new_line = f"{class_id} {x_center} {y_center} {width} {height}\n"
            new_lines.append(new_line)
        
        # Sobrescribir el archivo con las nuevas líneas
        with open(label_path, 'w') as f:
            f.writelines(new_lines)

print("Proceso completado. Las etiquetas han sido modificadas.")
