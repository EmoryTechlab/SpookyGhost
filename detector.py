import cv2
import mediapipe as mp
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

DEBUG = True

class Detector():
    def __init__(self, width: int, height: int):
        self.cap = None
        self.width = width
        self.height = height

    def startCapture(self) -> None:
        # For webcam input:
        self.cap = cv2.VideoCapture(0)

    def stopCapture(self) -> None:
        if self.cap is not None:
            self.cap.release()
        cv2.destroyAllWindows()

    def getPose(self):
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            if self.cap.isOpened():
                success, image = self.cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    # If loading a video, use 'break' instead of 'continue'.
                    return False, None

                # Flip the image horizontally for a later selfie-view display, and convert
                # the BGR image to RGB.
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                image = cv2.resize(image, (self.width, self.height))                # Resize image
                # To improve performance, optionally mark the image as not writeable to
                # pass by reference.
                image.flags.writeable = False
                results = pose.process(image)
                if DEBUG:
                    mp_drawing.draw_landmarks(
                        image,
                        results.pose_landmarks,
                        mp_pose.POSE_CONNECTIONS,
                        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
                left = None
                right = None
                if results is not None and results.pose_landmarks is not None:
                    left = results.pose_landmarks.landmark[8]
                    right = results.pose_landmarks.landmark[7]
                    if DEBUG:
                        cv2.circle(image, (int(left.x * self.width), int(left.y * self.height)), 10, (255, 0, 0))
                        cv2.circle(image, (int(right.x * self.width), int(right.y * self.height)), 10, (255, 0, 0))

                if DEBUG:
                    cv2.imshow('MediaPipe Pose', image)
                    if cv2.waitKey(5) & 0xFF == 27:
                        return False, None

                if left is not None and right is not None:
                    return True, ((left.x + right.x)/2, (left.y + right.y)/ 2)
                else:
                    return False, None

if __name__ == "__main__":
    detector = Detector(400, 400)
    detector.startCapture()
    while True:
        ok, results = detector.getPose()
        # if results.pose_landmarks is not None:
            # print(results.pose_landmarks.landmark[12], results.pose_landmarks.landmark[11])
            # break
        if cv2.waitKey(5) & 0xFF == 27:
            break
    detector.stopCapture()
