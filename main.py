import detector
import movement
import math

FOV = 160
WIDTH = 400
HEIGHT = 400
CENTER = (200, 200)

if __name__ == "__main__":
    detector = detector.Detector(WIDTH, HEIGHT)
    detector.startCapture()
    movement.send_angle(90, 90)
    while True:
        detected, pose = detector.getPose()
        if detected:
            angle_base = ((pose[0] - CENTER[0]) * FOV) / WIDTH
            angle_height = ((pose[1] - CENTER[1]) * FOV) / HEIGHT
            movement.send_angle(angle_base, angle_height)

    detector.stopCapture()
