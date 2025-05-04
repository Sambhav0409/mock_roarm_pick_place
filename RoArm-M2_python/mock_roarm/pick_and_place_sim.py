from roarm_mock import RoArm
from vision_mock import detect_disk

def main():
    # Initialize fake robot arm
    arm = RoArm()

    # Step 1: Detect disk position (x, y)
    x, y = detect_disk()
    z_pick = 0  # Assume flat surface height

    # Step 2: Move above the disk
    arm.move_to(x, y, z_pick + 5)  # Move above
    arm.move_to(x, y, z_pick)      # Move to pickup
    arm.set_gripper(True)          # Close gripper (pick)
    arm.move_to(x, y, z_pick + 5)  # Lift

    # Step 3: Move to fixed place position
    x_place, y_place, z_place = 20, 20, 0
    arm.move_to(x_place, y_place, z_place + 5)
    arm.move_to(x_place, y_place, z_place)
    arm.set_gripper(False)         # Release
    arm.move_to(x_place, y_place, z_place + 5)

    print("[MOCK] Pick-and-place operation complete.")

if __name__ == "__main__":
    main()
