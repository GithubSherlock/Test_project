import cv2
import os

def save_img():
    video_path = './input'
    videos = os.listdir(video_path)
    for video_name in videos:
        file_name = video_name.split('.')[0]
        folder_name = video_path + file_name
        os.makedirs(folder_name, exist_ok=True)
        vc = cv2.VideoCapture(video_path + '/' + video_name)
        c = 0
        rval = vc.isOpened()

        while rval:
            c = c + 1
            rval, frame = vc.read()
            pic_path = folder_name + '/'
            if rval:
                cv2.imwrite(pic_path + str(c) + '.png', frame)
                cv2.waitKey(1)
            else:
                break
        vc.release()
        print('save_success')
        print(folder_name)
save_img()

