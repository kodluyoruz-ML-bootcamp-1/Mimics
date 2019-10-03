# import the necessary packages
import cv2.cv2 as cv2
import dlib
import imutils
# construct the argument parser and parse the arguments
from imutils import face_utils


class LandMarker:
    def __init__(self, landmark_predictor_path: str):
        # initialize dlib's face detector (HOG-based) and then create
        # the facial landmark predictor
        self.predictor = dlib.shape_predictor(landmark_predictor_path)
        self.detector = dlib.get_frontal_face_detector()

    def img_to_landmarks(self, img_path: str):
        # load the input image, resize it, and convert it to grayscale
        image = cv2.imread(img_path)
        image = imutils.resize(image, width=500)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # detect faces in the grayscale image
        rects = self.detector(gray, 1)

        shape = None
        # loop over the face detections
        for (i, rect) in enumerate(rects):
            # determine the facial landmarks for the face region, then
            # convert the facial landmark (x, y)-coordinates to a NumPy
            # array
            shape = self.predictor(gray, rect)

            data_points = []
            for idx in range(0, shape.num_parts):
                data_points.append(shape.part(idx).x)
                data_points.append(shape.part(idx).y)

            shape_np = self.shape_to_np(shape)
            print([shape_np])
            print(data_points)
            exit(99)
            # print(shape_np)

            """
            # convert dlib's rectangle to a OpenCV-style bounding box
            # [i.e., (x, y, w, h)], then draw the face bounding box
            (x, y, w, h) = self.rect_to_bb(rect)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
            # show the face number
            cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
            print(cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2))
    
            # loop over the (x, y)-coordinates for the facial landmarks
            # and draw them on the image
            for (x, y) in shape_np:
                cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
    
            cv2.imshow("Output", image)
            # cv2.imwrite(IMAGE.replace('.jpg', '_landmarked.bmp'), image)
            cv2.waitKey(0)
            
            """

            return data_points  # Assumed that number of face in picture = 1

    @staticmethod
    def rect_to_bb(rect):
        # take a bounding predicted by dlib and convert it
        # to the format (x, y, w, h) as we would normally do
        # with OpenCV
        x = rect.left()
        y = rect.top()
        w = rect.right() - x
        h = rect.bottom() - y

        # return a tuple of (x, y, w, h)
        return x, y, w, h

    @staticmethod
    def shape_to_np(shape, dtype="int"):
        # initialize the list of (x, y)-coordinates
        # coords = np.zeros((68, 2), dtype=dtype)
        coords = []

        # loop over the 68 facial landmarks and convert them
        # to a 2-tuple of (x, y)-coordinates
        for i in range(0, 68):
            coords.append((shape.part(i).x, shape.part(i).y))

        # return the list of (x, y)-coordinates
        return coords
