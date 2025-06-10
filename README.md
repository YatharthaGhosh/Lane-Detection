# Lane Detection for Videos

\<p align="center"\>
\<img src="[suspicious link removed]" alt="Example Lane Detection Output" width="600"\>
\<br\>
\<em\>An example of the lane detection in action on a video.\</em\>
\</p\>

## Table of Contents

  - About The Project
  - Features
  - Getting Started
      - Prerequisites
      - Installation
  - Usage
  - Project Structure
  - Contributing
  - License
  - Contact
  - Acknowledgements

## About The Project

This repository contains a Python project for real-time lane detection in video streams. The project utilizes computer vision techniques, primarily OpenCV, to identify and draw lane lines on video frames. This capability is fundamental for Advanced Driver-Assistance Systems (ADAS) and can serve as a building block for autonomous vehicle navigation.

The core pipeline involves:

1.  **Preprocessing**: Converting frames to grayscale and applying Gaussian blur to reduce noise.
2.  **Edge Detection**: Using the Canny edge detector to identify potential lane boundaries.
3.  **Region of Interest (ROI) Masking**: Focusing the detection on the relevant area of the road ahead.
4.  **Hough Transform**: Detecting straight lines from the edged image.
5.  **Lane Averaging and Extrapolation**: Processing the detected line segments to form continuous left and right lane lines.
6.  **Overlay**: Superimposing the detected lane lines onto the original video frame.

## Features

  * **Video Lane Detection**: Processes video files frame by frame to detect and display lane lines.
  * **Robust Edge Detection**: Employs Canny edge detection for reliable edge identification.
  * **Dynamic Region of Interest**: Defines a triangular region to focus on the immediate road ahead.
  * **Hough Line Transform**: Utilizes `cv2.HoughLinesP` for efficient line segment detection.
  * **Lane Line Averaging**: Calculates and averages the slope and intercept of detected line segments to form stable left and right lane lines.
  * **Line Extrapolation**: Extends the averaged lane lines to cover a desired vertical range on the image.
  * **Visual Overlay**: Draws prominent blue lines on the original video frames, blending the output seamlessly.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

  * Python 3.x
  * `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your_username/Lane-Detection.git
    cd Lane-Detection
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install numpy opencv-python
    ```
    *(Note: You might need `opencv-contrib-python` if you encounter issues with `opencv-python`.)*

## Usage

To run the lane detection on a video file:

1.  Place your input video file (e.g., `test2.mp4`) in the same directory as `Lanes_Video.py`, or update the `os.chdir` and video path in the script.

2.  Execute the script from your terminal:

    ```bash
    python Lanes_Video.py
    ```

The script will open a new window displaying the video with the detected lane lines. Press `q` to quit the video playback.

The current setup uses `test2.mp4` as the input video. You can change this by modifying the line `cap = cv2.VideoCapture("test2.mp4")` in `Lanes_Video.py` to point to your desired video file.

## Project Structure

```
Lane-Detection/
├── Lanes_Video.py
├── test2.mp4 (example input video)
├── README.md
└── LICENSE
```

  * `Lanes_Video.py`: The main script containing all the functions for lane detection and video processing.
  * `test2.mp4`: An example video file used for demonstration. You can replace this with your own video.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star\! Thanks again\!

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [your\_email@example.com](mailto:your_email@example.com)

Project Link: [https://github.com/your\_username/Lane-Detection](https://www.google.com/search?q=https://github.com/your_username/Lane-Detection)

## Acknowledgements

  * OpenCV Library for computer vision functionalities.
  * NumPy for numerical operations.

-----
