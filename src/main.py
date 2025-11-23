from alarm_example import RealtimeYOLODetectionWithAlerts

if __name__ == "__main__":
    detector = RealtimeYOLODetectionWithAlerts(target_object='person')
    detector.run()
