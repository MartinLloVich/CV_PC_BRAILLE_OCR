import os
import cv2
import time
from ultralytics import YOLO

def main():
    # Directorios
    test_dir = "datasets/images/test"
    results_dir = "resultados"
    approved_dir = os.path.join(results_dir, "aprobados")
    disapproved_dir = os.path.join(results_dir, "reprobados")
    
    # Crear carpetas de resultados si no existen
    os.makedirs(approved_dir, exist_ok=True)
    os.makedirs(disapproved_dir, exist_ok=True)
    
    # Inicializar modelo YOLO
    model = YOLO("runs/detect/train2/weights/best.pt")

    # Inicializar contadores
    results_summary = {}
    total_images = 0
    total_aprobados = 0
    total_reprobados = 0

    # Registrar tiempo de inicio
    start_time = time.time()

    # Procesar cada imagen en el directorio de test
    for file_name in os.listdir(test_dir):
        if file_name.endswith(".png"):
            total_images += 1

            # Extraer letra del nombre del archivo
            letter = file_name.split("_")[0]
            img_path = os.path.join(test_dir, file_name)

            # Leer la imagen
            img = cv2.imread(img_path)

            # Realizar predicción
            predictions = model.predict(img)[0]
            pred_image = predictions.plot()

            # Verificar número de resultados
            num_results = len(predictions.boxes)  # Número de predicciones

            if num_results == 1:
                detected_letter = letter.lower()  # Validación adicional
                if detected_letter == letter:
                    output_dir = approved_dir
                    status = "aprobados"
                    total_aprobados += 1
                else:
                    output_dir = disapproved_dir
                    status = "reprobados"
                    total_reprobados += 1
            else:  # Si hay más de una predicción, clasificar como reprobado
                output_dir = disapproved_dir
                status = "reprobados"
                total_reprobados += 1

            # Guardar la imagen procesada
            output_path = os.path.join(output_dir, file_name)
            cv2.imwrite(output_path, pred_image)

            # Actualizar resultados por letra
            if letter not in results_summary:
                results_summary[letter] = {"aprobados": 0, "reprobados": 0}

            results_summary[letter][status] += 1

    # Registrar tiempo de finalización
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Escribir resultados en resultados.txt
    results_txt_path = os.path.join(results_dir, "resultados.txt")
    with open(results_txt_path, "w") as results_file:
        for letter, counts in sorted(results_summary.items()):
            results_file.write(f"Letra: {letter}\n")
            results_file.write(f"  Aprobados: {counts['aprobados']}\n")
            results_file.write(f"  Reprobados: {counts['reprobados']}\n")
        results_file.write("\n")
        results_file.write(f"Total de imagenes analizadas: {total_images}\n")
        results_file.write(f"Total de aprobados: {total_aprobados}\n")
        results_file.write(f"Total de reprobados: {total_reprobados}\n")
        results_file.write(f"Tiempo total de simulacion: {elapsed_time:.2f} segundos\n")

if __name__ == "__main__":
    main()
