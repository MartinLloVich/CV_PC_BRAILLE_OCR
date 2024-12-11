import cv2
from ultralytics import YOLO

if __name__ == '__main__':
    img_name = "a_1218.png"
    img = cv2.imread(f"datasets/images/test/{img_name}")

    model = YOLO("runs/detect/train2/weights/best.pt")


    pred = model.predict(img)[0]
    pred = pred.plot()
    cv2.imwrite(f"{img_name}.png",pred)