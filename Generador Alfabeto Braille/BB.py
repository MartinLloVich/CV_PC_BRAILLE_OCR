import cv2
import os

# Rutas de la imagen y su etiqueta
image_path = 'c_49.png'
label_path = 'c_49.txt'

# Cargar la imagen
img = cv2.imread(image_path)
if img is None:
    raise FileNotFoundError(f"No se pudo cargar la imagen {image_path}")

height, width = img.shape[:2]

# Leer el archivo de etiquetas
if not os.path.exists(label_path):
    raise FileNotFoundError(f"No se encontró el archivo de etiquetas {label_path}")

with open(label_path, 'r') as f:
    lines = f.readlines()

for line in lines:
    # Cada línea del txt: class x_center y_center width height
    data = line.strip().split()
    cls = int(data[0])
    x_center_norm = float(data[1])
    y_center_norm = float(data[2])
    w_norm = float(data[3])
    h_norm = float(data[4])

    # Convertir coordenadas normalizadas a pixeles
    x_center = x_center_norm * width
    y_center = y_center_norm * height
    w = w_norm * width
    h = h_norm * height

    x1 = int(x_center - w/2)
    y1 = int(y_center - h/2)
    x2 = int(x_center + w/2)
    y2 = int(y_center + h/2)

    # Imprimir el bounding box
    print(f"Clase: {cls}, Bounding Box: x1={x1}, y1={y1}, x2={x2}, y2={y2}")

    # Opcional: Dibujar el bounding box sobre la imagen
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(img, f"Class {cls}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

# Mostrar la imagen con el bounding box (requiere entorno gráfico)
# cv2.imshow("Imagen con Bounding Box", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Guardar la imagen con el bounding box dibujado
cv2.imwrite("imagen_con_bb.jpg", img)
