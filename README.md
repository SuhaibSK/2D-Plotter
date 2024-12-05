# 2D-Plotter
This repository contains two Python scripts designed to process images captured from a webcam, detect contours, and generate G-code based on the detected contours. These scripts are ideal for applications in robotics, CNC machining, or other automated systems requiring contour-based path planning.
Files in the Repository
1. web_cam_processing.py

This script handles the image capture and preprocessing pipeline, including:

    Capturing live video feed from a webcam.
    Saving a captured image upon user input.
    Applying image preprocessing steps such as grayscale conversion, Gaussian blur, edge detection, dilation, and contour detection.
    Resizing and saving the processed image.

The script also calculates contours from the processed image and returns the contours along with the image dimensions.
Key Features

    User Interaction:
        Press s to save the current frame and process it.
        Press q to exit the webcam capture.

    Image Processing Pipeline:
        Grayscale conversion
        Gaussian blur
        Edge detection with Canny
        Contour detection and dilation
        Image resizing

Outputs

    Returns:
        List of contours
        Dimensions of the processed image.

2. processed image to gcode conversion.py

This script uses the contours and image dimensions obtained from webcamPreprocess.py to generate G-code commands for CNC or robotics systems.
Key Features

    Contour Mapping to G-Code:
        Scales the contour coordinates to fit a 150x150 unit workspace.
        Generates G-code commands for each contour point.

    G-code Commands:
        G00 for rapid movement.
        M03 for spindle/laser activation.
        G04 for dwell time.

    Output:
        A .nc file (gcode.nc) containing the generated G-code.
