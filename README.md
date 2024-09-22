# Virtual_Painter

# Overview
**Virtual Painter** is a Python-based application that enables users to create digital art using hand gestures. By employing computer vision and hand tracking techniques, the project allows users to "paint" in the air using their hands, with the colors being reflected on the screen.

# Dependencies
To run this project, ensure you have the following libraries installed:

* OpenCV
* MediaPipe
* NumPy

You can install these using pip:
```bash
pip install opencv-python mediapipe numpy
```

# Project Structure
* **main.py:** Contains the core logic for capturing video, hand tracking, color detection, and canvas drawing.
* **utils.py:** (Optional) Can be used for helper functions related to image processing or color manipulation. This includes hand_tracking module, facemesh module and headers folder.

# How to Run
1. **Clone the repository** or download the project files.
2. **Install dependencies** as mentioned above.
3. **Run the main script:** Execute `python main.py` in your terminal.

# Output
* **Video Output**
 https://github.com/user-attachments/assets/77cbd0fd-f8f5-40e0-a13c-5d079e291153

# Usage
* **Start the application:** Run the main script.
* **Calibrate the hand:** The application might require initial calibration for hand detection. Follow on-screen instructions.
* **Paint:** Move your hand in the air to draw on the virtual canvas. Two fingers for selection and one finger(index ) for drawing.

# Customization
* **Colors:** Modify the color palette in the code to experiment with different color schemes. You can do it by code or by making different headers.
* **Brush size:** Implement logic to control brush size based on hand gestures or other parameters.
* **Canvas size:** Adjust the canvas dimensions to fit your screen or preferences.
* **Hand tracking model:** Explore different hand tracking models provided by MediaPipe for better accuracy or performance.

# Known Issues
* **Hand occlusion:** The system might struggle if the hand is fully occluded.
* **Lighting conditions:** Varying lighting conditions can affect hand detection accuracy.

# Future Improvements
* **Multiple users:** Allow multiple users to paint simultaneously.
* **Different painting styles:** Implement various painting styles like oil, watercolor, etc.
* **Saving and loading paintings:** Enable users to save their artwork and load it later.
* **Interactive elements:** Add interactive elements like color palettes, etc.

# Contributions
Contributions to this project are welcome. Please feel free to fork the repository and submit pull requests.
 




