import os
import cv2
import numpy as np
from glob import glob

def makeJPGS(path):
    """
    Converts images og png to jpg foramt of all images located in path directory

    :param path: path of images to be converted to jpg format
    """
    outPath = path + "/jpgs"
    if not os.path.exists(outPath):
        os.mkdir(outPath)
        imgs = glob("./data/*g")
        for imgPath in imgs:
            img = cv2.imread(imgPath)
            os.remove(imgPath)
            imgName = os.path.basename(imgPath)[0]
            cv2.imwrite(f"{outPath}/{imgName}.jpg", img)
    else: print("jpgs already exists!")
    return glob(outPath + "/*.jpg")


def getSceneCanny(imgArr):
    """
    Takes the GaussianBlur Filter of the scene then extract edges of the images

    :param imgArr: numpy array image which edges get extracted from
    :returns edges: numpy array of the scene extracted edges
    """
    grayFrame = cv2.cvtColor(imgArr, cv2.COLOR_BGR2GRAY)
    gauBlur = cv2.GaussianBlur(grayFrame, (5, 5), 0)
    edges = cv2.Canny(gauBlur, 50, 150)                     # minVal, maxVal = 1 : 3
    return edges


def getRegOfInterest(imgArr):
    """
    Extract the lanes edges only from a scene of an extracted edges

    :param imgArr: numpy array image of the extracted scene edges
    :returns lanes: numpy array image of the extracted lane edges only
    """
    height = imgArr.shape[0]
    regOfInterest = np.array([[(25, height-75), (1250, height-75), (650, 290)]])
    mask = np.zeros_like(imgArr)
    cv2.fillPoly(mask, regOfInterest, (255, 255, 255))
    lanes = cv2.bitwise_and(imgArr, mask)
    return lanes


def getPointsFromLine(imgShape, line):
    m, b = line
    y1 = imgShape[0]
    y2 = int(y1 * (2/5))
    x1 = int((y1 - b) / m)
    x2 = int((y2 - b) / m)
    return np.array([x1, y1, x2, y2])

def drawLanesLines(sceneImg, laneEdges, rho=2, theta=1,
    minLineLength=50, maxLineGap=5, threshold=100):
    """
    Draws straight lines over the scene source image using the lane extracted edges

    :param sceneImg: numpy array of the scene source image
    :param laneEdges: numpy array of the extracted lane edges
    :param rho: the radious of the line in the Hough Transform
    :param theta: line angle in radian scale
    :param threshold: minimum num of intersection to detect a line
    :param minLineLength: lane length connect points
    :param maxLineGap: maximum gap between 2 points to connect them by a line
    :returns sceneLanes: numpy array image with overlayed lane lines
    """
    leftLines, rightLines = [], []

    lines = cv2.HoughLinesP(
        laneEdges, rho, theta*np.pi/180, threshold, lines = np.array([]),
        minLineLength=minLineLength, maxLineGap=maxLineGap
    )
    lineMask = np.zeros_like(sceneImg)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(-1)
            slope, intercept = np.polyfit((x1, x2), (y1, y2), 1)
            if slope > 0:
                leftLines.append((slope, intercept))
            else:
                rightLines.append((slope, intercept))
        leftLine = np.average(leftLines, axis=0)
        rightLine = np.average(rightLines, axis=0)
        x1, y1, x2, y2 = getPointsFromLine(sceneImg.shape, leftLine)
        cv2.line(lineMask, (x1, y1), (x2, y2), (0, 255, 255), thickness=10)
        x1, y1, x2, y2 = getPointsFromLine(sceneImg.shape, rightLine)
        cv2.line(lineMask, (x1, y1), (x2, y2), (0, 255, 255), thickness=10)
    sceneLanes = cv2.addWeighted(sceneImg, 0.8, lineMask, 1, 1)
    return sceneLanes


imgsPath = sorted(makeJPGS("./data"))
laneImg = cv2.imread(imgsPath[0])
sceneEdges = getSceneCanny(laneImg)
laneEdges = getRegOfInterest(sceneEdges)
sceneLanes = drawLanesLines(laneImg, laneEdges, minLineLength=50, maxLineGap=5)
cv2.imwrite("data/outImgs/sceneEdges.jpg", sceneEdges)
cv2.imwrite("data/outImgs/laneEdges.jpg", laneEdges)
cv2.imwrite("data/outImgs/detectedLane.jpg", sceneLanes)

cv2.imshow("window", sceneLanes)
cv2.waitKey(0)
cv2.destroyAllWindows()
