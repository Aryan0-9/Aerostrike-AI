import cv2
import sys

# 1. Load the video file into an OpenCV object
video_path = "free_kick.mov" 
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video file: " + video_path)
    print("Please check the file name and path.")
    sys.exit()

print("Processing video frames... Press 'q' on your keyboard to quit early.")

# 2. Infinite loop to process the video frame-by-frame
while True:
    # Read the next individual frame from the video
    ##ret --> determines true/false whether frame can be read and next frame can be opened
    #If cap.read can grab a frame, ret becomes true and data image loads from frame
    #Frame is the pixel array that holds the data(1920x1080 = 2073600 total pixels in array)
    ret, frame = cap.read()
    
    # If ret is False, it means the video has reached the final frame
    if not ret:
        print("Reached the end of the video file.")
        break
        
    # 3. Display the current frame in a window named "Soccer Tracking Workspace"
    cv2.imshow("Soccer Tracking Workspace", frame)
    
    # 4. Wait 30 milliseconds before showing the next frame, OR break if 'q' is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        print("Video playback stopped early by user.")
        break

# 5. Clean up computer memory when finished
cap.release()
cv2.destroyAllWindows()
print("Workspace successfully closed.")
