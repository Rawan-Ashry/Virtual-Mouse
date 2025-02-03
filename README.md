# 🖱️ Virtual Mouse using Hand Gestures

## 🔍 Overview
This project implements a **Virtual Mouse** using **hand gestures**, powered by **OpenCV, MediaPipe, and PyAutoGUI**. It allows users to control the mouse cursor, click, drag, right-click, and scroll using simple hand movements.

## 🎯 Features
✅ **Move Cursor** → Move index finger.
✅ **Left-Click** 🖱️ → Tap index & thumb together.
✅ **Right-Click** 👆 → Tap middle finger & thumb together.
✅ **Drag & Drop** ✊ → Hold index & thumb close, move to drag, release to drop.
✅ **Scroll Up** 📜⬆️ → Move index finger **up** while middle finger is extended.
✅ **Scroll Down** 📜⬇️ → Move index finger **down** while middle finger is extended.

## 📦 Installation
### Prerequisites
Ensure you have Python installed on your system. Then, install the required libraries:
```sh
pip install opencv-python mediapipe pyautogui
```

## ▶️ How to Run
1. **📷 Connect a webcam** to your computer.
2. **🖥️ Run the script** using the following command:
   ```sh
   python virtual_mouse.py
   ```
3. **🖐️ Control the mouse** using hand gestures.
4. **❌ Press 'Esc'** to exit the program.

## 🏗️ Code Explanation
The script performs the following steps:
1. 📸 Captures video using OpenCV.
2. ✋ Detects hands using MediaPipe.
3. 🎯 Tracks finger positions and maps them to screen coordinates.
4. 🎮 Executes actions like clicking, scrolling, and dragging based on finger positions.

## 🛠️ Usage
- 👉 Move your **index finger** to control the cursor.
- 🖱️ **Tap your thumb and index finger** together to click.
- 👆 **Tap your thumb and middle finger** together to right-click.
- ✊ **Hold your thumb and index finger close** to drag.
- 📜 **Move the index finger up/down** (while the middle finger is extended) to scroll.

## 🚀 Future Improvements
- 🔄 Add **double-click detection**
- 🔊 Implement **gesture-based volume control**
- 🎯 Improve **accuracy with smoothing techniques**

## 👨‍💻 Credits
Developed using:
- 🖼️ **OpenCV** for real-time video processing
- ✋ **MediaPipe** for hand tracking
- 🖱️ **PyAutoGUI** for mouse automation

