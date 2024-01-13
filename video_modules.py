#connecting to capture device 
import cv2
import mediapipe as mp

def main():
    cap = cv2.VideoCapture(1)
    '''
    This function is just to stream the video from a webcam 
    '''
    
    #detector = poseDetector()

    if not cap.isOpened(): #error handling 
        return "Error opening the video."
    while cap.isOpened():   #when there is video, capture it and stream it 
        timer = cv2.getTickCount()
        
        success, img = cap.read() #unpacking and then the frame
        
        #img = detector.findPose(img)
        
        fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer) #calculating the fps value 
        cv2.putText(img, str(int(fps)), (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
        #calculate fps 
        if success:
            #gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow("Tracking", img)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break
        else:
            break

