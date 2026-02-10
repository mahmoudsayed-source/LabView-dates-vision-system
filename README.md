# LabVIEW-dates-vision-system


This repository contains a set of LabVIEW Virtual Instruments (VIs) designed to capture images, process them using a trained AI model, and classify date fruits into different quality grades.

The system integrates **LabVIEW**, **Python**, and an **ONNX AI model** to perform automated image-based classification for both stored images and live video streams.

---

## 🚀 Project Overview

The project consists of **four main LabVIEW files**, each responsible for a specific task in the classification pipeline:

1. **Image taking VI**
   - Captures images from a live camera stream.
   - Saves the captured images to a specified directory.

2. **Image Read VI**
   - Reads images from the saved directory.
   - Loads selected images for further processing.

3. **image input VI**
   - Takes a saved image as input.
   - Starts a Python session.
   - Executes the trained AI model (ONNX format).
   - Returns the predicted grade as an integer value.

4. **video input VI**
   - Works directly with the live camera stream.
   - Sends frames to Python for inference.
   - Uses the ONNX model to classify images in real time.
   - Outputs the predicted grade as an integer.

---

## 🧠 AI Model

- Model Format: **ONNX**
- Training: Performed externally and exported to ONNX
- Purpose: Classify date fruits into quality grades

### Classification Output

| Value | Grade   |
|-------|---------|
| 0     | Grade 1 |
| 1     | Grade 2 |
| 2     | Agwa    |

---

## ⚙️ System Requirements

### Software

- LabVIEW (Vision Development Module recommended)
- Python 3.x
- ONNX Runtime
- Required Python libraries:

```txt
numpy
opencv-python
onnxruntime
```

### Hardware

- USB / IP Camera
- PC capable of running LabVIEW and Python

---

## 📁 Repository Structure

```txt
LabVIEW-AI-Date-Classification/
│
├── LabVIEW_Files/
│   ├── Capture_Save.vi
│   ├── Read_Image.vi
│   ├── Offline_AI_Classification.vi
│   └── Live_AI_Classification.vi
│
├── Python/
│   └── inference.py
│
├── Model/
│   └── model.onnx
│
├── Sample_Images/
│
└── README.md
```

---

## ▶️ How to Use

### 1. Capture Images
- Open `Capture_Save.vi`
- Connect your camera
- Start acquisition
- Images will be saved automatically

### 2. Read Saved Images
- Open `Read_Image.vi`
- Select the image directory
- Load images

### 3. Offline Classification
- Open `Offline_AI_Classification.vi`
- Select image file
- Configure Python & model paths
- Run the VI

### 4. Live Classification
- Open `Live_AI_Classification.vi`
- Connect camera
- Start VI
- View predictions

---

## 🔗 LabVIEW–Python Integration

This project uses LabVIEW’s Python Node to:

- Start Python session
- Transfer image data
- Run ONNX inference
- Return results

Configure Python in:

Tools → Options → Python

---

## 🛠️ Configuration

Before running, update:

- Python executable path
- ONNX model path
- Image folder path

Inside VI block diagrams.

---

## 📊 Applications

- Date fruit grading
- Agricultural inspection
- Smart production lines
- Research projects

---

## 🤝 Contributing

1. Fork repository
2. Create branch
3. Commit changes
4. Open Pull Request

---

## 👤 Author

Mahmoud Sayed Sayed Ismail

Graduation / Research Project

Give this repo a ⭐ if useful.

---

## 📬 Contact

Open an issue on GitHub for questions.
