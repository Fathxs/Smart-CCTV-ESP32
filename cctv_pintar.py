import sys
import os
from types import ModuleType


os.environ["QT_QPA_PLATFORM"] = "xcb"

if 'pkg_resources' not in sys.modules:
    pkg_mock = ModuleType('pkg_resources')
    def resource_filename(package_name, resource_name):
        for path in sys.path:
            potential_path = os.path.join(path, package_name, resource_name)
            if os.path.exists(potential_path):
                return potential_path
        return ""
    pkg_mock.resource_filename = resource_filename
    sys.modules['pkg_resources'] = pkg_mock
# =================================================================

import cv2
import face_recognition
import numpy as np
import time


cap = cv2.VideoCapture("http://192.168.1.5:81/stream")

database_path = "wajah database"
screenshot_path = "hasil_screenshot"

if not os.path.exists(database_path):
    print(f"Error: Folder {database_path} tidak ditemukan.")
    exit()

if not os.path.exists(screenshot_path):
    os.makedirs(screenshot_path)

# --- Memuat Database Wajah ---
known_face_encodings = []
known_face_names = []

print("Sedang memuat database wajah...")
for filename in os.listdir(database_path):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(database_path, filename)
        face_image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(face_image)
        if len(encodings) > 0:
            known_face_encodings.append(encodings[0])
            known_face_names.append(os.path.splitext(filename)[0])

print(f"Berhasil memuat {len(known_face_names)} wajah dari database.")


cv2.namedWindow('Smart CCTV 2.0 - Face Recognition Only', cv2.WINDOW_NORMAL)


frame_count = 0
process_every_n_frames = 3
face_locations = []
face_encodings = []
face_names = []
last_screenshot_time = 0
consecutive_failures = 0  


while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        consecutive_failures += 1

        if consecutive_failures < 15: 
            time.sleep(0.1)
            continue
        else:
            print("\nGagal mengambil gambar dari kamera setelah beberapa kali percobaan.")
            break
            

    consecutive_failures = 0 
    frame_count += 1
    

    image = cv2.flip(frame, 1)
    

    if frame_count % process_every_n_frames == 0:
        small_frame = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
        small_frame_rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        face_locations = face_recognition.face_locations(small_frame_rgb)
        face_encodings = face_recognition.face_encodings(small_frame_rgb, face_locations)
        
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
            name = "Stranger"
            
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
            
            face_names.append(name)


    for (top, right, bottom, left), name in zip(face_locations, face_names):

        top *= 2
        right *= 2
        bottom *= 2
        left *= 2
        
        box_color = (0, 255, 0) if name != "Stranger" else (0, 0, 255)
        cv2.rectangle(image, (left, top), (right, bottom), box_color, 2)
        cv2.putText(image, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, box_color, 2)
        

        if name == "Stranger":
            current_time = time.time()
            if current_time - last_screenshot_time > 5:
                filename = os.path.join(screenshot_path, f"stranger_{int(current_time)}.jpg")
                cv2.imwrite(filename, image)
                print(f"Peringatan! Orang asing terdeteksi. Bukti disimpan ke: {filename}")
                last_screenshot_time = current_time


    header_color = (0, 100, 0)
    cv2.rectangle(image, (0, 0), (image.shape[1], 60), header_color, -1)
    cv2.putText(image, "Status Sistem: Pemindai Wajah Aktif (Smooth Mode)", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(image, "Tekan 'q' untuk keluar", (20, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)
    
    cv2.imshow('Smart CCTV 2.0 - Face Recognition Only', image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Sistem CCTV ditutup dengan aman.")