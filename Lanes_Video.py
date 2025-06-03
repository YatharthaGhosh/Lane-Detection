import numpy as np
import cv2
import os

# Change directory
os.chdir('D:/Internships/Pinnacle Labs/Data Science/Lane Detection')


# Convert slope-intercept line to pixel points
def make_points(lane_image, line):
    slope, intercept = line
    y1 = int(lane_image.shape[0])
    y2 = int(y1 * 3 / 5)
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return [x1, y1, x2, y2]


# Average left/right lane lines
def average_slope_intercept(lane_image, lines):
    left_fit = []
    right_fit = []
    if lines is None:
        return None
    for line in lines:
        for x1, y1, x2, y2 in line:
            fit = np.polyfit((x1, x2), (y1, y2), 1)
            slope, intercept = fit
            if slope < 0:
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))

    if not left_fit or not right_fit:
        return None

    left_avg = np.average(left_fit, axis=0)
    right_avg = np.average(right_fit, axis=0)
    left_line = make_points(lane_image, left_avg)
    right_line = make_points(lane_image, right_avg)
    return [left_line, right_line]


# Canny edge detection
def canny(lane_image):
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    return cv2.Canny(blur, 50, 150)


# Draw lines on a blank image
def display_lines(lane_image, lines):
    line_image = np.zeros_like(lane_image)
    if lines is not None:
        for x1, y1, x2, y2 in lines:
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image


# Define region of interest
def region_of_interest(lane_image):
    height = lane_image.shape[0]
    polygons = np.array([[(200, height), (1100, height), (550, 250)]])
    mask = np.zeros_like(lane_image)
    cv2.fillPoly(mask, polygons, 255)
    return cv2.bitwise_and(lane_image, mask)


# Load video
cap = cv2.VideoCapture("test2.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    canny_image = canny(frame)
    cropped_canny = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(cropped_canny, 2, np.pi/180, 100,
                            np.array([]), minLineLength=40, maxLineGap=5)
    averaged_lines = average_slope_intercept(frame, lines)
    line_image = display_lines(frame, averaged_lines)
    combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)

    cv2.imshow("Lane Detection - Video", combo_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
