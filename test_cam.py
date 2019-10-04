from __future__ import division
import cv2.cv2 as cv2
import numpy as np
import time


def draw_rects(img, rects):
    """
    ?????????????
    :param img:
    :param rects:
    :return:
    """
    for x, y, w, h in rects:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 00), 2)
        face = cv2.resize(img, (224, 224))
        text = 'asda'
        cv2.putText(img, text, (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), lineType=cv2.LINE_AA)


def nothing(*arg):
    pass




FRAME_WIDTH = 320
FRAME_HEIGHT = 240

# Initialize webcam. Webcam 0 or webcam 1 or ...
vidCapture = cv2.VideoCapture(0)
print(vidCapture)
# vidCapture.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
# vidCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

while True:
    timeCheck = time.time()

    # Get webcam frame
    rect, frame = vidCapture.read()

    # ##############################################3
    img = np.zeros((512, 512, 3), np.uint8)
    # Draw a rectangle around the text
    ori = cv2.rectangle(frame, (10, 180), (500, 300), (0, 0, 255), 4)
    font = cv2.QT_FONT_NORMAL
    cv2.putText(ori, 'IREM SAHIN <3', (30, 256), font, 2.5, (255, 255, 255), 2, cv2.LINE_AA)
    # now use a frame to show it just as displaying a image
    cv2.imshow("Text", ori)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    exit(21)

    # ##############################################3

    # Show the original image.
    cv2.imshow('frame', frame)
    cv2.imwrite('smiling_berk.png', frame)
    exit(22)

    draw_rects(img=frame, rects=[rect])

    x, y, w, h = cv2.boundingRect([(35, 35)])
    exit(21)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    print('fps - ', 1 / (time.time() - timeCheck))

cv2.destroyAllWindows()
vidCapture.release()
