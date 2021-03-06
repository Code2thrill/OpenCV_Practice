# Import module
import cv2


cap = cv2.VideoCapture('data/videos/chaplin.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # Display the resulting frame
    cv2.imshow('Frame',frame)

    # Press esc on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == 27:
      break
    #27 is the ASCII value for “ESC”

  # Break the loop
  else:
    break
