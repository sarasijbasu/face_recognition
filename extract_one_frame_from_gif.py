import os
import glob
import cv2

path = os.getcwd()


# Function to extract frames
def FrameCapture(path):
    for index in range(0,11):
        dirlist = glob.glob(os.getcwd()+"/*.gif")
        path = dirlist[index]

        # Path to video file
        vidObj = cv2.VideoCapture(path)

        # Used as counter variable
        count = 0

        # checks whether frames were extracted
        success = 1

        while success:

            # vidObj object calls read
            # function extract frames
            success, image = vidObj.read()

            # Saves the frames with frame-count
            cv2.imwrite(path.split(os.sep)[-2]+"_"+path.split(os.sep)[-1].replace(".gif","")+".jpg", image)

            count += 1
            cv2.destroyAllWindows()
            break

# Driver Code
if __name__ == '__main__':

    # Calling the function
    FrameCapture(path)





