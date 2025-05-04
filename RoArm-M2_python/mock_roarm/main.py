USE_MOCK = True

if USE_MOCK:
    from roarm_mock import RoArm
    from vision_mock import detect_disk
else:
    from roarm_real import RoArm
    from vision_real import detect_disk
