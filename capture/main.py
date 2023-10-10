import cv2 as cv
import imutils

# Define the video capture object
cam = cv.VideoCapture(0)
cv.namedWindow("Python Capture")

img_counter =0

while True:
    # Capture the video frame
    # by frame
    ret, frame = cam.read()

    if not ret:
        print("failed to capture")
        break
    resized_frame = imutils.resize(frame, width=1000)


    #Display the resulting  frame
    cv.imshow('RC', resized_frame)

    #the 'q' button is set to stop the cam feed
    k = cv.waitKey(1)
    if k%256 == 27:
        print("EXITING!!!")
        break
    elif k%256 == 32:
        img_name= "opencv_frame_{}.png".format(img_counter)
        cv.imwrite(img_name, resized_frame)
        print("Captured")
        img_counter+1

#After the loop release the cam object
cam.release()

cv.destroyAllWindows()