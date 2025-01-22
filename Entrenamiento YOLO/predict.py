import cv2
from ultralytics import YOLO

if __name__ == '__main__':
    img_name = "prueba ruda.jpg"
    img = cv2.imread(img_name)

    model = YOLO("runs/detect/train/weights/best.pt")


    pred = model.predict(img)[0]
    pred = pred.plot()
    cv2.imwrite(f"{img_name}.png",pred)

