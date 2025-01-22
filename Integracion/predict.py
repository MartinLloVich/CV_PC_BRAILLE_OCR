import cv2
from ultralytics import YOLO
import os

if __name__ == '__main__':

    # Define la ruta base relativa a este script
    base_dir = os.path.dirname(__file__)  # Directorio del script

    # Rutas relativas para los archivos
    img_name = os.path.join(base_dir, "salida.png")
    model_path = os.path.join(base_dir, "best.pt")

    # Carga la imagen
    img = cv2.imread(img_name)

    # Cargar el modelo YOLO
    model = YOLO(model_path)

    # Obtener predicciones
    results = model.predict(img)[0]

    # Filtrar predicciones con confianza > 50%
    high_conf_predictions = [res for res in results.boxes if res.conf > 0.1]

    # Cargar nombres de clases si están disponibles
    class_names = model.names if hasattr(model, 'names') else None

    # Crear una copia de la imagen para dibujar
    img_copy = img.copy()

    # Dibujar las predicciones filtradas
    for box in high_conf_predictions:
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas del cuadro delimitador
        class_id = int(box.cls)  # Convertir la clase predicha a int

        # Obtener el nombre de la clase
        class_name = class_names[class_id] if class_names else str(class_id)

        # Calcular el tamaño del texto
        font_scale = 0.6  # Tamaño inicial del texto
        thickness = 2
        text_size = cv2.getTextSize(class_name, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)[0]

        # Ajustar el tamaño del texto si no cabe en el bounding box
        box_width = x2 - x1
        while text_size[0] > box_width and font_scale > 0.3:
            font_scale -= 0.05
            text_size = cv2.getTextSize(class_name, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)[0]

        # Dibujar cuadro negro (bounding box)
        cv2.rectangle(img_copy, (x1, y1), (x2, y2), (0, 0, 0), 2)

        # Dibujar texto un poco más abajo del bounding box
        text_x = x1
        text_y = y1 - 4  # Margen adicional de 5 píxeles debajo del cuadro
        cv2.putText(img_copy, class_name, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), thickness)

    # Guardar la imagen procesada
    output_name = f"{img_name}_procesado.png"
    cv2.imwrite(output_name, img_copy)
    print(f"Imagen guardada como {output_name}")
