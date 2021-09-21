import detector

if __name__ == "__main__":
    detector = detector.Detector()
    detector.startCapture()
    for i in range(100000):
        detector.getFace(True)
    detector.stopCapture()
