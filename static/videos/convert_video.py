import os
import ffmpeg


input_dir = "./real/"
video_list = os.listdir(input_dir)

for i, video in enumerate(video_list):
    if not video.endswith(".mov"):
        continue

    input_file = os.path.join(input_dir, video)
    output_file = os.path.join(input_dir, video.replace(".mov", ".mp4"))
    
    if not os.path.exists(output_file):
        ffmpeg.input(input_file).output(output_file, vcodec="libx264", acodec="aac").run(overwrite_output=True)
        print(f"Conversion successful: {output_file}")
