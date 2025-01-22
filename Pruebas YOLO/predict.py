import cv2
import os
from ultralytics import YOLO

if __name__ == '__main__':

    # Define la ruta base relativa a este script
    base_dir = os.path.dirname(__file__)  # Directorio del script

    # Rutas relativas para los archivos
    img_name = os.path.join(base_dir, "touch.jpg")
    model_path = os.path.join(base_dir, "best.pt")

    img = cv2.imread(img_name)

    model = YOLO(model_path)


    pred = model.predict(img)[0]
    pred = pred.plot()
    cv2.imwrite(f"{img_name}_deteccion.png",pred)

