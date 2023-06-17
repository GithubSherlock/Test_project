import cv2

def process_video(video_path):
    video = cv2.VideoCapture(video_path)
    frame_count = 0  # Initialize frame counter
    all_frames = []

    while True:
        ret, frame = video.read()
        if ret is False:
            break
        all_frames.append(frame)
        frame_count += 1

    print("Count the number of frames:", frame_count)
    print("There are", len(all_frames), "frames")  # Total number of frames

    (major_ver, minor_ver, subminor_ver) = cv2.__version__.split('.')
    if int(major_ver) >= 3:
        fps = video.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS): {0}".format(fps))
    else:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    video.release()

# Set the video file path as input
video_path = './input/park.mp4'
process_video(video_path)
