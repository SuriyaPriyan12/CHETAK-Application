import cv2
import numpy as np

# Open video file
cap = cv2.VideoCapture('scenic_drive_lane_detector.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    height = frame.shape[0]
    width = frame.shape[1]
    roi_vertices = [
        (0, height),
        (width / 2, height / 2),
        (width, height)]
        
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge_frame = cv2.Canny(gray_frame, 100, 200)
    mask = np.zeros_like(edge_frame)
    cv2.fillPoly(mask, np.array([roi_vertices], np.int32), 255)
    mask_edges = cv2.bitwise_and(edge_frame,mask)
    lines = cv2.HoughLinesP(mask_edges, rho=5, theta=np.pi/60, threshold=100, minLineLength=40, maxLineGap=30)
    
    line_image = np.zeros_like(frame)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)
    
    processed_frame = cv2.addWeighted(frame, 0.7, line_image, 1, 0)
    
    cv2.imshow('Lane Detection', processed_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
