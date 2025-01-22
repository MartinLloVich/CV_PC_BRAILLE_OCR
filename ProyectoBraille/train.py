from ultralytics import YOLO

if __name__ == '__main__':
    # Carga del modelo
    model = YOLO('yolo11m.pt')

    # Entrenamiento del modelo
    model.train(
        data='train.yaml',  # Ruta al archivo de configuración del dataset
        epochs=45,           # Número de épocas
        imgsz = (128,128),   #imagenes
        batch=4,             # Tamaño del batch
        optimizer="Adam"
    )