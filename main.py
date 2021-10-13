import detector
import movement
import math
import time

FOV = 160
WIDTH = 400
HEIGHT = 400
CENTER = (0, 0)

if __name__ == "__main__":
    detector = detector.Detector(WIDTH, HEIGHT)
    detector.startCapture()
    movement.send_angle(90, 90)
    input("Press ENTER to begin tracking...")
    while True:
        detected, pose = detector.getPose()
        if detected and pose is not None:
            angle_base = int(((pose[0] * WIDTH - CENTER[0]) * FOV) / WIDTH)
            angle_height = abs(int(((pose[1] * HEIGHT - CENTER[1]) * FOV) / HEIGHT) - 180)
            movement.send_angle(angle_base, angle_height)
            # time.sleep(0.5)

    detector.stopCapture()
