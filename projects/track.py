"""
tracker.py
Face tracking + reconocimiento de gestos + pose corporal en tiempo real
usando la webcam, con MediaPipe Tasks API + OpenCV.

Antes de correr esto:
  1. python download_models.py   (una sola vez, descarga los 3 modelos)
  2. python test_camera.py       (verificá que la cámara abre bien sola)

Cómo probar módulo por módulo:
  Cambiá los flags ENABLE_FACE / ENABLE_HANDS / ENABLE_POSE de a uno para
  aislar problemas. Si con los tres en True algo no anda, apagá dos y
  dejá solo el que sospechás.
"""

import os
import time
import platform

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

BaseOptions = python.BaseOptions
RunningMode = vision.RunningMode

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------
ENABLE_FACE = True
ENABLE_HANDS = True
ENABLE_POSE = True

CAM_INDEX = 0
CAM_BACKEND = cv2.CAP_DSHOW if platform.system() == "Windows" else cv2.CAP_ANY

MODEL_DIR = "models"
FACE_MODEL = os.path.join(MODEL_DIR, "face_landmarker.task")
GESTURE_MODEL = os.path.join(MODEL_DIR, "gesture_recognizer.task")
POSE_MODEL = os.path.join(MODEL_DIR, "pose_landmarker_lite.task")

# ---------------------------------------------------------------------------
# Topologías de conexión, a mano (no dependemos de mp.solutions, que ya no
# viene incluido en versiones recientes de mediapipe).
# ---------------------------------------------------------------------------
HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),          # pulgar
    (0, 5), (5, 6), (6, 7), (7, 8),          # índice
    (5, 9), (9, 10), (10, 11), (11, 12),     # medio
    (9, 13), (13, 14), (14, 15), (15, 16),   # anular
    (13, 17), (17, 18), (18, 19), (19, 20),  # meñique
    (0, 17),                                 # base de la palma
]

POSE_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 7), (0, 4), (4, 5), (5, 6), (6, 8), (9, 10),
    (11, 12), (11, 13), (13, 15), (15, 17), (15, 19), (15, 21), (17, 19),
    (12, 14), (14, 16), (16, 18), (16, 20), (16, 22), (18, 20),
    (11, 23), (12, 24), (23, 24), (23, 25), (25, 27), (27, 29), (29, 31),
    (27, 31), (24, 26), (26, 28), (28, 30), (30, 32), (28, 32),
]


def draw_points(frame, landmarks, color, radius=2):
    h, w = frame.shape[:2]
    for lm in landmarks:
        cx, cy = int(lm.x * w), int(lm.y * h)
        cv2.circle(frame, (cx, cy), radius, color, -1)


def draw_connections(frame, landmarks, connections, color, thickness=2):
    h, w = frame.shape[:2]
    n = len(landmarks)
    for a, b in connections:
        if a < n and b < n:
            pa = (int(landmarks[a].x * w), int(landmarks[a].y * h))
            pb = (int(landmarks[b].x * w), int(landmarks[b].y * h))
            cv2.line(frame, pa, pb, color, thickness)


def check_models():
    needed = []
    if ENABLE_FACE and not os.path.exists(FACE_MODEL):
        needed.append(FACE_MODEL)
    if ENABLE_HANDS and not os.path.exists(GESTURE_MODEL):
        needed.append(GESTURE_MODEL)
    if ENABLE_POSE and not os.path.exists(POSE_MODEL):
        needed.append(POSE_MODEL)
    if needed:
        print("[ERROR] Faltan estos modelos:")
        for m in needed:
            print(f"  - {m}")
        print("Corré primero: python download_models.py")
        return False
    return True


def main():
    if not check_models():
        return

    face_landmarker = gesture_recognizer = pose_landmarker = None

    if ENABLE_FACE:
        opts = vision.FaceLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=FACE_MODEL),
            running_mode=RunningMode.VIDEO,
            num_faces=1,
            output_face_blendshapes=True,
        )
        face_landmarker = vision.FaceLandmarker.create_from_options(opts)
        print("[OK] Face landmarker cargado")

    if ENABLE_HANDS:
        opts = vision.GestureRecognizerOptions(
            base_options=BaseOptions(model_asset_path=GESTURE_MODEL),
            running_mode=RunningMode.VIDEO,
            num_hands=2,
        )
        gesture_recognizer = vision.GestureRecognizer.create_from_options(opts)
        print("[OK] Gesture recognizer cargado")

    if ENABLE_POSE:
        opts = vision.PoseLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=POSE_MODEL),
            running_mode=RunningMode.VIDEO,
            num_poses=1,
        )
        pose_landmarker = vision.PoseLandmarker.create_from_options(opts)
        print("[OK] Pose landmarker cargado")

    cap = cv2.VideoCapture(CAM_INDEX, CAM_BACKEND)
    if not cap.isOpened():
        print("[ERROR] No se pudo abrir la cámara. Corré test_camera.py para diagnosticar.")
        return

    start_time = time.time()
    frame_count = 0
    fps = 0.0
    fps_timer = time.time()

    print("Ventana abierta. Presioná 'q' para salir.")

    while True:
        ok, frame = cap.read()
        if not ok:
            print("[ERROR] No se pudo leer un frame de la cámara.")
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        timestamp_ms = int((time.time() - start_time) * 1000)

        # ---- FACE ----
        if face_landmarker:
            result = face_landmarker.detect_for_video(mp_image, timestamp_ms)
            if result.face_landmarks:
                for face in result.face_landmarks:
                    draw_points(frame, face, (0, 255, 255), radius=1)
                if result.face_blendshapes:
                    top = max(result.face_blendshapes[0], key=lambda c: c.score)
                    cv2.putText(frame, f"Expresion: {top.category_name} ({top.score:.2f})",
                                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
            else:
                cv2.putText(frame, "Cara: no detectada", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        # ---- GESTOS DE MANO ----
        if gesture_recognizer:
            result = gesture_recognizer.recognize_for_video(mp_image, timestamp_ms)
            if result.hand_landmarks:
                h, w = frame.shape[:2]
                for i, hand in enumerate(result.hand_landmarks):
                    draw_connections(frame, hand, HAND_CONNECTIONS, (255, 0, 255))
                    draw_points(frame, hand, (255, 0, 255), radius=3)
                    if result.gestures and i < len(result.gestures) and result.gestures[i]:
                        g = result.gestures[i][0]
                        wrist = hand[0]
                        cv2.putText(frame, f"{g.category_name} ({g.score:.2f})",
                                    (int(wrist.x * w), int(wrist.y * h) - 20),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

        # ---- POSE ----
        if pose_landmarker:
            result = pose_landmarker.detect_for_video(mp_image, timestamp_ms)
            if result.pose_landmarks:
                for pose in result.pose_landmarks:
                    draw_connections(frame, pose, POSE_CONNECTIONS, (0, 255, 0))
                    draw_points(frame, pose, (0, 0, 255), radius=3)

        # ---- FPS ----
        frame_count += 1
        if time.time() - fps_timer >= 1.0:
            fps = frame_count / (time.time() - fps_timer)
            frame_count = 0
            fps_timer = time.time()
        cv2.putText(frame, f"FPS: {fps:.1f}", (10, frame.shape[0] - 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.imshow("Face + Gestos + Pose Tracker", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    if face_landmarker:
        face_landmarker.close()
    if gesture_recognizer:
        gesture_recognizer.close()
    if pose_landmarker:
        pose_landmarker.close()


if __name__ == "__main__":
    main()