#connecting to capture device 
import cv2
import mediapipe as mp
 #selecting source, in this case a webcam 

#tracker = cv2.legacy.TrackerMOSSE_create()

class poseDetector():
    
    def __init__(self, 
                 mode = False, 
                 model_complex = 1,
                 smooth_landm = True,
                 upBody = False, 
                 smooth = True,
                 detectionCon = 0.5, 
                 trackCon = 0.5):
        ''' 
        Initial parameters
        '''
        self.mode = mode
        self.model_complex = 1
        self.smooth_landm = True
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(
            self.mode,
            self.model_complex, 
            self.smooth_landm,
            self.upBody,
            self.smooth,
            self.detectionCon,
            self.trackCon
        )

    def findPose(self, img, draw = True):
        
        ''' 
        method to find the pose
        img: inputs a cv2 img
        '''
        results = self.pose.process(img)
        if results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img



def main():
    cap = cv2.VideoCapture(1)
    '''
    This function is just to stream the video from a webcam 
    '''
    
    detector = poseDetector()

    if not cap.isOpened(): #error handling 
        return "Error opening the video."
    while cap.isOpened():   #when there is video, capture it and stream it 
        timer = cv2.getTickCount()
        
        success, img = cap.read() #unpacking and then the frame
        
        img = detector.findPose(img)
        
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



if __name__ == "__main__":
    main()