import cv2
video=cv2.VideoCapture("Video\18.mp4") #opens video file
ret = True
while ret:
    ret , frame = video.read() #reads frame-by-frame
    if ret:
        cv2.imshow('Frame',frame) #shows each frame
        cv2.waitKey(40) #waits 40ms (controls playback speed)


video.release() #frees video
video.destroyAllWindows() #closes all windows