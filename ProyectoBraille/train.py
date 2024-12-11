from ultralytics import YOLO

if __name__ == '__main__':
    # Carga del modelo
    model = YOLO('yolov8m.pt')

    # Entrenamiento del modelo
    model.train(
        data='train.yaml',  # Ruta al archivo de configuración del dataset
        epochs=90,           # Número de épocas
        imgsz = (100,100),   #imagenes
        batch=4,             # Tamaño del batch
        optimizer="Adam"
    )
