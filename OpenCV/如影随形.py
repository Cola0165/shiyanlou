import cv2
import numpy as np

if __name__ == '__main__':
    img1 = cv2.imread('tower01.jpg', -1)
    img2 = cv2.imread('tower02.jpg', -1)

    # TODO(You):  请在此实现代码
    orb = cv2.ORB_create(nfeatures=500)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    matches = sorted(matches, key=lambda x: x.distance)
    match_img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None)
    
    cv2.imwrite('tower_match.jpeg', match_img)
    cv2.waitKey()
    cv2.destroyAllWindows()