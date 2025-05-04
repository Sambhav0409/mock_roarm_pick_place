class RoArm:
    def __init__(self, port="/dev/ttyUSB0", baudrate=115200):
        print("[MOCK] Initialized fake RoArm")

    def move_to(self, x, y, z):
        print(f"[MOCK] Move to ({x:.2f}, {y:.2f}, {z:.2f})")

    def set_gripper(self, state):
        print(f"[MOCK] Gripper {'closed (picked)' if state else 'opened (released)'}")
