from flask import Flask, Response
import cv2
from ultralytics import YOLO
import time

app = Flask(__name__)

# 🔹 Cargamos un modelo pequeño (más rápido, menos consumo)
# "n" = nano (más liviano). Evitar modelos grandes en tiempo real.
model = YOLO("yolo11n.pt")

# 🔹 Inicializamos la cámara (0 = webcam)
cap = cv2.VideoCapture(0)

def generate_frames():
    prev_time = 0  # Para calcular FPS y limitar procesamiento

    while True:
        success, frame = cap.read()
        if not success:
            break

        # 🔽 OPTIMIZACIÓN 1: Reducir resolución
        # Menos píxeles = menos cómputo (impacto MUY alto en CPU)
        frame = cv2.resize(frame, (640, 480))

        # 🔽 OPTIMIZACIÓN 2: Limitar FPS manualmente
        # 0.1 segundos ≈ 10 FPS
        # Esto evita procesar 30–60 FPS innecesarios
        current_time = time.time()
        if current_time - prev_time < 0.1:
            continue
        prev_time = current_time

        # 🔹 Inferencia con YOLO
        results = model(frame)
        annotated = results[0].plot()

        # 🔽 OPTIMIZACIÓN 3: Compresión JPEG
        # 70 = calidad media (0–100)
        # - Más bajo → menos peso, menos CPU, peor calidad
        # - Más alto → mejor calidad, más consumo
        ret, buffer = cv2.imencode(
            '.jpg',
            annotated,
            [int(cv2.IMWRITE_JPEG_QUALITY), 70]
        )

        frame_bytes = buffer.tobytes()

        # 🔹 Streaming tipo MJPEG (lo que entiende el navegador)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def video_feed():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

if __name__ == "__main__":
    print("Abre en tu navegador: http://TU_IP:5000")

    # 🔹 Permite acceso desde otros dispositivos en la red
    # 0.0.0.0 = escuchar en todas las interfaces
    app.run(host="0.0.0.0", port=5001, debug=False)