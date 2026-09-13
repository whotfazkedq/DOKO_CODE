"""
test_camera.py
PASO 0: verificar que OpenCV puede abrir tu cámara ANTES de meter mediapipe
en la ecuación. Si esto no funciona, nada de lo demás va a funcionar,
así que arrancá siempre por acá.
"""

import platform
import cv2

CAM_INDEX = 0  # si falla, probá 1 o 2 (a veces hay cámaras virtuales antes)

# En Windows, CAP_DSHOW evita que la apertura de cámara tarde varios segundos
# o falle silenciosamente con el backend por defecto (MSMF).
backend = cv2.CAP_DSHOW if platform.system() == "Windows" else cv2.CAP_ANY


def main():
    cap = cv2.VideoCapture(CAM_INDEX, backend)

    if not cap.isOpened():
        print(f"[ERROR] No se pudo abrir la cámara con índice {CAM_INDEX}.")
        print("Cosas para probar:")
        print("  1. Cambiá CAM_INDEX a 1 o 2 arriba en este archivo.")
        print("  2. Revisá que ninguna otra app (Zoom, Teams, Discord) esté usando la cámara.")
        print("  3. Revisá los permisos de cámara del sistema operativo para Python/terminal.")
        return

    print("[OK] Cámara abierta correctamente.")
    print("Se debería abrir una ventana con tu video en vivo. Presioná 'q' para cerrar.")

    while True:
        ok, frame = cap.read()
        if not ok:
            print("[ERROR] La cámara abrió pero no se pudo leer un frame.")
            break

        frame = cv2.flip(frame, 1)  # efecto espejo, más natural
        cv2.putText(frame, "Camara OK - presiona 'q' para salir", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imshow("Test de camara", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
