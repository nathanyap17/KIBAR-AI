# 🧠 KIBAR-AI: Sign Recognition, Automatic Braille Response

> An innovative assistive device integrating AI-based sign language detection and physical Braille display for the deaf-blind community.

---

## 📌 Overview

**KIBAR-AI** stands for **"Kenali Isyarat, Braille Automatik Respons"** (Sign Recognition, Automatic Braille Response). It is a real-time AI-powered system that detects hand gestures through a camera and translates them into physical Braille patterns via a solenoid-based actuator grid, controlled by an Arduino board.

KIBAR-AI aims to bridge communication between deaf and blind individuals — a population often left behind by mainstream assistive technologies.

---

## 🔧 Features

- 🎯 **Real-Time Sign Detection** using YOLOv11
- 🤖 **Arduino-Controlled Braille Actuation**
- 🧩 **Seamless AI–Hardware Integration**
- 🦾 **Tactile Feedback for Enhanced Accessibility**
- 🖨️ **3D Printed Hardware Casing**

---

## 📂 Folder Structure

```bash
├── model/                 # Trained YOLOv11 models
├── arduino/              # Arduino source code (.ino)
├── data/                 # Dataset of hand gestures and Braille mappings
├── scripts/              # Python scripts (real-time detection, serial communication)
├── assets/               # Images, icons, diagrams
└── README.md             # This file
```

---

## 🚀 Getting Started

### 1. Setup Environment

Install the required Python packages:

```bash
pip install ultralytics opencv-python pyserial
```

Upload the Arduino code to your board (e.g., Arduino UNO) using PlatformIO or Arduino IDE.

### 2. Run Real-Time Detection

```bash
python model.py
```

Ensure your webcam is connected and Arduino is properly communicating over the correct COM port.

---

## 📈 Project Goals

| Objective                            | Achieved |
|-------------------------------------|----------|
| Real-time gesture recognition       | ✅        |
| Braille actuation via solenoids     | ✅        |
| Arduino & Python serial integration | ✅        |
| Custom dataset model training       | ✅        |
| Inclusive communication             | ✅        |

---

## 📊 Tech Stack

- **YOLOv11** – Real-time object detection
- **OpenCV** – Image capture and processing
- **Arduino C++** – Actuator control
- **PySerial** – Communication bridge
- **3D Design Tools** – Casing and mounting

---

## 🔍 Use Case

> “Imagine a deaf and blind person trying to communicate in a crowd — **KIBAR-AI** provides a private, silent, and tactile language channel.”

---

## 🧠 Innovation Highlights

- 🔄 **Real-Time Conversion**: Gestures to Braille in seconds.
- ⚙️ **Hardware-Software Synergy**: Fully functional device, not just a concept.
- 🧩 **Multi-Tech Integration**: AI + Arduino + Actuation + 3D Print.
- 🧑‍🤝‍🧑 **Social Impact**: Helps an underserved population.

---

## 📸 Visual Preview

![KIBAR-AI Poster](assets/KIBAR-AI Kenali Isyarat, Braille Automatik Respons (Landscape A1)-1.png) <!-- Replace with actual asset path -->

---

## 📞 Contact & Credits

**Project Lead**: Nathan Yap Jia De  
**Institution**: Universiti Malaysia Sarawak (UNIMAS)  
**Copyright**:

![Registered IP](assets/Copyright_KIBAR_AI-1.png)

📧 [nathanyap5352@outlook.com](mailto:nathanyap@5362@outlook.com)  
🔗 [LinkedIn](#) | [GitHub](#)

---

> _"Connecting communication, transcending barriers."_  
> Let’s build an inclusive future — one sign, one dot at a time.

---
