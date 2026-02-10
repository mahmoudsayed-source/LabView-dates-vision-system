import cv2
import numpy as np
import onnxruntime as ort

MODEL_PATH = r"D:\9th\LabVIEW\testing\best.onnx"
try:
    session = ort.InferenceSession(MODEL_PATH, providers=['CPUExecutionProvider'])
except Exception:
    session = None

def predict_grade(image_2d_array):

    if session is None:
        return -1  # Model initialization failed

    try:
        arr = np.array(image_2d_array, dtype=np.uint32)
        
        r = (arr >> 16) & 0xFF
        g = (arr >> 8) & 0xFF
        b = arr & 0xFF
        
        img_rgb = np.stack([r, g, b], axis=-1).astype(np.uint8)

        if img_rgb.shape[0] != 640 or img_rgb.shape[1] != 640:
            img_rgb = cv2.resize(img_rgb, (640, 640))
            
        img_input = img_rgb.transpose(2, 0, 1).astype(np.float32) / 255.0
        img_input = np.expand_dims(img_input, axis=0)

        outputs = session.run(None, {session.get_inputs()[0].name: img_input})
        preds = np.squeeze(outputs[0])

        if len(preds.shape) > 1 and preds.shape[0] < preds.shape[1]:
            preds = preds.T
            
        if len(preds.shape) == 1:
            return int(np.argmax(preds))
        else:
            scores = preds[:, 4:]
            max_conf = np.max(scores, axis=1)
            best_idx = np.argmax(max_conf)

            if max_conf[best_idx] > 0.4:  # 40% Confidence threshold
                return int(np.argmax(scores[best_idx]))
            else:
                return -4  # No object detected
            
    except Exception:
        return -99  # General processing error