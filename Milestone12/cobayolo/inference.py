from ultralytics import YOLO
import cv2

# Load model
model = YOLO("/home/veevry/loky_ws/cobayolo/runs/detect/runs/train/vision3/weights/best.pt")

# Buka video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    # Ambil hasil dan gambar bounding box
    annotated_frame = results[0].plot()

    # Tampilkan
    cv2.imshow("Deteksi YOLO", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()