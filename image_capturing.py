import cv2
import time

def capture_images(interval):
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return
    try:
        while True:
            ret,frame=cap.read()
            if not ret:
                print("Error: cannot capture")
                break
            cv2.imshow('Frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            timestamp=time.strftime("%Y%m%d_%H%M%S")
            filename=f"image_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            time.sleep(interval)
    
    finally:
        cap.release()
        cv2.destroyAllWindows()
interval=5
capture_images(interval)
