import cv2
import mediapipe as mp

class Detector():
    def __init__(self):
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_drawing = mp.solutions.drawing_utils
        self.cap = None

    def startCapture(self) -> None:
        # For webcam input:
        self.cap = cv2.VideoCapture(0)

    def stopCapture(self) -> None:
        if self.cap is not None:
            self.cap.release()

    def getFace(self, show: bool) -> (bool, list):
        with self.mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
            if self.cap.isOpened():
                success, image = self.cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    # If loading a video, use 'break' instead of 'continue'.
                    return False, None

                # Flip the image horizontally for a later selfie-view display, and convert
                # the BGR image to RGB.
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                # To improve performance, optionally mark the image as not writeable to
                # pass by reference.
                image.flags.writeable = False
                results = face_detection.process(image)

                # Draw the face detection annotations on the image.
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.detections:
                    for detection in results.detections:
                        self.mp_drawing.draw_detection(image, detection)
                    if show:
                        cv2.imshow('MediaPipe Face Detection', image)
                        if cv2.waitKey(5) & 0xFF == 27:
                            cv2.destroyAllWindows()
