import cv2

if __name__ == '__main__':
    img = cv2.imread("lena.png")
    cv2.imshow("lena", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()