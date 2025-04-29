from ultralytics import YOLO
yolo = YOLO("./yolov8n.pt", task="detect")
result = yolo(source="ultralytics-main\\ultralytics\\assets\\bus.jpg", save=True)