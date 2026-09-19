import cv2
import sys
import math

# 1. Setup video capture
video_path = "free_kick.mov" # Make sure this matches your file name!
cap = cv2.VideoCapture(video_path)

motion_detector = cv2.createBackgroundSubtractorMOG2(history=10, varThreshold=25, detectShadows=False)

if not cap.isOpened():
    print("Error: Could not open video file: " + video_path)
    sys.exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Reached the end of the video.")
        break
        
    # --- REGION OF INTEREST (ROI) CROP ---
    # Get the total height and width of the video frame
    height, width, channels = frame.shape
    
    # We want to ignore the player on the left and the logo on the very top right.
    start_x = int(width * 0.70)  # Cut out the entire left 55% of the video screen
    end_x = int(width * 0.95)

    start_y = int(height * 0.52)
    
    # Crop the frame using standard Python list slicing [ymin:ymax, xmin:xmax]
    # Only scan the lower portion of the screen where the ball actually travels
    
    roi_frame = frame[start_y:height, start_x:end_x]

    # -------------------------------------
        
    # 2. Convert our cropped ROI frame from BGR to HSV
    #HSV separates color (Hue) from lighting/brightness (Value), making it drastically easier to isolate specific colors regardless of shadows or highlights
    hsv_frame = cv2.cvtColor(roi_frame, cv2.COLOR_BGR2HSV)
    
    # 3. Define the color boundaries for the white soccer ball
    lower_white = (0, 0, 200)   
    upper_white = (180, 50, 255) 
    
    # 4. Create the mask using only the cropped frame
    color_mask = cv2.inRange(hsv_frame, lower_white, upper_white)
    motion_mask = motion_detector.apply(roi_frame)
    combined_mask = cv2.bitwise_and(color_mask, motion_mask)
    
    # 5. Find the outlines of the white shapes inside the mask
    #Countours gets filled with an array of shape boundaries
    #Hierarchy gets filled with organizational data 
    contours, hierarchy = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 6. Sort all contours from right-to-left based on their X coordinate
    # This guarantees the computer looks at objects on the right side of the screen first!
    if len(contours) > 0:
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        
    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        
        if perimeter == 0:
            continue
            
        circularity = (4 * math.pi * area) / (perimeter ** 2)
        (x, y), radius = cv2.minEnclosingCircle(contour)
        
        # Broad target filters for size and basic roundness
        if 15 < area < 1200 and circularity > 0.4:
            
            # Shift BOTH X and Y back to the original full-screen system
            center_x = int(x) + start_x
            center_y = int(y) + start_y
            ball_radius = int(radius)
            
            # Print coordinates to the terminal console
            print("Ball Found at X: " + str(center_x) + ", Y: " + str(center_y) + " | Radius: " + str(round(radius, 1)) + "px | Roundness: " + str(round(circularity, 2)))
            
            # Draw the target circles on the original full-frame
            cv2.circle(frame, (center_x, center_y), ball_radius, (0, 255, 0), 2)
            cv2.circle(frame, (center_x, center_y), 2, (0, 0, 255), -1)
            
            break

    # 8. Show the original frame and the clean cropped mask
    cv2.imshow("Tracking Workspace", frame)
    cv2.imshow("Color Filter Mask (ROI)", combined_mask)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        print("Stopped early by user.")
        break

cap.release()
cv2.destroyAllWindows()
print("Workspace cleanly closed.")
