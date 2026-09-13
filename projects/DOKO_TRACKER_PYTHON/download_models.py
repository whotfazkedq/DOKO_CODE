"""
download_models.py
Descarga los modelos .task que necesita MediaPipe Tasks API para
face landmarker, gesture recognizer y pose landmarker.
Solo hace falta correrlo una vez.
"""

import os
import urllib.request

MODELS = {
    "face_landmarker.task":
        "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task",
    "gesture_recognizer.task":
        "https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task",
    "pose_landmarker_lite.task":
        "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/1/pose_landmarker_lite.task",
}


def main():
    os.makedirs("models", exist_ok=True)

    for filename, url in MODELS.items():
        path = os.path.join("models", filename)

        if os.path.exists(path):
            print(f"[SKIP] {filename} ya existe, no se vuelve a descargar")
            continue

        print(f"[...] Descargando {filename}")
        try:
            urllib.request.urlretrieve(url, path)
            size_kb = os.path.getsize(path) / 1024
            print(f"[OK]   {filename} descargado ({size_kb:.0f} KB)")
        except Exception as e:
            print(f"[ERROR] No se pudo descargar {filename}: {e}")
            print(f"        Probá descargarlo manualmente desde: {url}")

    print("\nListo. Deberías tener una carpeta 'models/' con los 3 archivos .task")


if __name__ == "__main__":
    main()
