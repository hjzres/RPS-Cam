import cv2 as cv

def main():
    vid = cv.VideoCapture(0)

    while True:
        ret, frame = vid.read()

        cv.imshow('frame', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    vid.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()