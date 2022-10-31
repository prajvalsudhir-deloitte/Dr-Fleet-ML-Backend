import cv2
  
# Function to extract frames
def FrameCapture(path):
    
    try:
    # Path to video file
        vidObj = cv2.VideoCapture(path)
        
        if (vidObj.isOpened()== False): 
            print("Error opening video stream or file")
            
        # Used as counter variable
        count =0
    
        while vidObj.isOpene():
    
            # vidObj object calls read
            # function extract frames
            success, frame = vidObj.read()

            if success:
            # Saves the frames with frame-count
                cv2.imwrite("frame%d.jpg" % count, frame)

                # TODO : can pass frame to ML model 
                count += 1
            else: 
                print("video completed")
                break
        
        # release the resourse 
        vidObj.release()
    except:
        print("Error Occur")
