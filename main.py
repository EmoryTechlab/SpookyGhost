import detector
import movement

if __name__ == "__main__":
    detector = detector.Detector()
    detector.startCapture()
    for i in range(100000):
        send_angle(90)
        detected, pose = detector.getFace(True)
        if detected:
            print(pose)
            
    detector.stopCapture()
