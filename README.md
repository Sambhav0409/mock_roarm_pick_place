# Mock RoArm-M2 Pick and Place Simulation

This repository contains a **mock pipeline** simulating a pick-and-place task using the [RoArm-M2 robotic arm](https://github.com/waveshareteam/roarm_m2). It includes mocked arm movement logic and vision tracking, suitable for demonstration and algorithm development **without requiring the physical hardware**.

---

## 🔧 Project Structure
mock_roarm_pick_place/
│
├── mock_arm.py # Simulates RoArm-M2 movement logic
├── mock_vision.py # Simulates metal disk detection using mock coordinates
├── main.py # Integrates vision + mock arm to simulate pick and place
This simulation demonstrates:
- How the RoArm-M2 Python interface might be used
- Vision tracking via OpenCV (mocked)
- Integration of detection and robotic arm movement logic

**Use-case:** For testing logic before real hardware is available.

---

## 🔄 Original Repository (for reference)

The real RoArm-M2 Python SDK is available here:  
🔗 [waveshareteam/roarm_m2](https://github.com/waveshareteam/roarm_m2)

The original repo contains:
- Low-level serial and HTTP control files (`serial_simple_ctrl.py`, `http_simple_ctrl.py`)
- Actual Python examples for dragging movements
- README and setup for flashing firmware

---

## 🧪 Testing Steps

1. Clone this repo or download the ZIP.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
Run the simulation:
bash
Copy
Edit
python main.py
You’ll see mock logs indicating object detection, pick and place logic, etc.

✅ Files from Original Repo Referenced
These were not modified but served as reference:

RoArm-M2_python/http_simple_ctrl.py
RoArm-M2_python/serial_simple_ctrl.py


You’ll find detailed steps we followed to:
Set up the repo
Simulate the robotic arm
Create the mock object tracker
Integrate everything logically
🙋 Contribution or Help
Since this is a simulated setup, you’re welcome to fork this and replace mocks with real hardware when available!

👨‍💻 Author
Sambhav Sachdeva
