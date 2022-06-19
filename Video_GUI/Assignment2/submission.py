import cv2

# load the image
im = cv2.imread("truth.png")

# create the window to display result
windowName = "Resize Image"
cv2.namedWindow(windowName,cv2.WINDOW_AUTOSIZE)

trackbarValue = "Scale"
scaleValue = 1
maxScaleUp = 100


trackbarType = "Type: \n 0: Scale Up \n 1: Scale Down"
scaleType = 0
maxType = 1

# set default scaleFactor value
scaleFactor = 1.0

# Build callback functions
def scaleImage (*args):
    #need to reset some default values
    global scaleValue
    global scaleType
    global scaleFactor
    scaleValue = args[0]
    #when scaleType is 1, scale down
    if scaleType == 1:
        scaleFactor = 1 - scaleValue/100.0
    # when scaleType is 0, scale up
    else:
        scaleFactor = 1 + scaleValue / 100.0
    #note: scaleFactor cannot be 0 unless image size will be 0
    if scaleFactor == 0:
        scaleFactor = 1

    # resize image
    scaled_Image = cv2.resize(im, None, fx=scaleFactor,
                             fy=scaleFactor, interpolation=cv2.INTER_LINEAR)
    #show resized image results
    cv2.imshow(windowName, scaled_Image)

# create trackbarValue with default values
cv2.createTrackbar(trackbarValue, windowName, scaleValue, maxScaleUp, scaleImage)

def scaleTypeImage (*args):
    # need to reset some default values
    global scaleValue
    global scaleType
    global scaleFactor
    scaleType = args[0]
    # It has same conditions as scaleImage
    if scaleType == 1:
        scaleFactor = 1 - scaleValue/100.0
    else:
        scaleFactor = 1 + scaleValue/100.0
    if scaleFactor == 0:
        scaleFactor = 1

    scaled_Image = cv2.resize(im, None, fx=scaleFactor,
                             fy=scaleFactor, interpolation=cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaled_Image)

# create trackbarType with default values
cv2.createTrackbar(trackbarType, windowName, scaleType, maxType, scaleTypeImage)

# starting with showing default image
cv2.imshow(windowName, im)
while True:
    k = cv2.waitKey(0)
    #press ESC to exit
    if k ==27:
        break

cv2.destroyAllWindows()