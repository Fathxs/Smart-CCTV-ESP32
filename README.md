# Smart CCTV - Face Recognition with ESP32-CAM

An intermediate-level IoT and Computer Vision project built on Arch Linux using Python, OpenCV, and Deep Learning-based Face Recognition. This system captures a wireless video stream from an ESP32-CAM and automatically detects faces in real-time.

## 🚀 Features
- **Wireless Video Streaming:** Fetches HTTP stream directly from ESP32-CAM.
- **Anti-Freeze Optimization:** Utilizes frame-skipping and resolution downscaling to maintain smooth video rendering on limited hardware.
- **Automated Intruder Capture:** Automatically takes a screenshot and saves the evidence locally if an unrecognized face ("Stranger") is detected.
- **Wayland Compatible:** Configured to run flawlessly on XCB/Wayland compositors (Hyprland).

## 🛠️ Requirements
- Python 3.11+
- ESP32-CAM module
- Libraries listed in `requirements.txt`

## ⚙️ Installation & Usage
1. Clone this repository to your local machine.
2. Create and activate a virtual environment.
3. Install the required dependencies using: `pip install -r requirements.txt`
4. Place the target faces in the `wajah database/` directory (name the image file as the person's name, e.g., `John.jpg`).
5. Change the URL in `cctv_pintar.py` to match your ESP32-CAM IP address.
6. Run the script using: `python cctv_pintar.py`

## 📝 Note
This project integrates the `face_recognition` library by Adam Geitgey.