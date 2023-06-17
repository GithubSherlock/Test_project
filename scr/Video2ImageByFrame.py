import cv2
import os

#  Bild a function to save video files as PNG images with a frame interval
def save_frames(video_path, output_path, frame_interval=10):
    os.makedirs(output_path, exist_ok=True)  # Check if the output folder exists, and create it if it does not.
    video_capture = cv2.VideoCapture(video_path)  # Open video file
    frame_count = 0  # Initializing the frame counter

    while True:
        ret, frame = video_capture.read()  # Read the frames of the video
        if not ret:  # Determine if the frame was successfully read
            break
        frame_count += 1
        if frame_count % frame_interval == 0:  # Save only frames of the specified interval
            filename = os.path.join(output_path, f"frame_{frame_count}.png")  # Build the file name to save the image
            cv2.imwrite(filename, frame)  # Save frames as PNG images
    video_capture.release()  # Release video capture object
    return True

def main():
    video_path = './input/park.mp4'  # Set the video file path as input
    output_path = './output'  # Set the output folder path
    frame_interval = 10  # Set frame interval

    save_frames(video_path, output_path, frame_interval)  # Use the function to save the frame as PNG images
    if save_frames(video_path, output_path, frame_interval) == True:
        print("Save successfully!")

if __name__ == '__main__':
    main()