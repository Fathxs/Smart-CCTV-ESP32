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

## 💻 Arduino Code Setup & Wi-Fi Configuration
To make the ESP32-CAM stream video, we will use the default Camera Web Server example. Follow these steps:
1. Open Arduino IDE.
2. Navigate to **File** $\rightarrow$ **Examples** $\rightarrow$ **ESP32** $\rightarrow$ **Camera** $\rightarrow$ **CameraWebServer**.
3. In the code, select the correct camera model by **uncommenting** the AI-Thinker model and commenting out the others. It should look exactly like this:
   ```cpp
   // Select camera model
   //#define CAMERA_MODEL_WROVER_KIT
   //#define CAMERA_MODEL_ESP_EYE
   //#define CAMERA_MODEL_M5STACK_PSRAM
   //#define CAMERA_MODEL_M5STACK_V2_PSRAM
   //#define CAMERA_MODEL_M5STACK_WIDE
   //#define CAMERA_MODEL_M5STACK_ESP32CAM
   //#define CAMERA_MODEL_M5STACK_UNITCAM
   #define CAMERA_MODEL_AI_THINKER // <-- UNCOMMENT THIS LINE

4. Enter your Wi-Fi credentials in the provided variables:
   const char* ssid = "YOUR_WIFI_SSID";
   const char* password = "YOUR_WIFI_PASSWORD";
5. Click Upload to flash the code into your ESP32-CAM.
6. Once the upload is complete, open the Serial Monitor and set the baud rate to 115200.
7. Press the RST (Reset) button on your ESP32-CAM or the downloader board.
8. The Serial Monitor will display an IP Address (e.g., http://192.168.1.5). Copy this IP Address and paste it into the cctv_pintar.py script to connect the AI program to your camera.

## 📝 Note
This project integrates the `face_recognition` library by Adam Geitgey.
