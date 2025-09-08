# import os
# import ffmpeg


# input_dir = "./real/"

# video_list = os.listdir(input_dir)

# for i, video in enumerate(video_list):
#     if not video.endswith(".MOV"):
#         continue

#     input_file = os.path.join(input_dir, video)
#     output_file = os.path.join(input_dir, video.replace(".MOV", ".mp4"))
    
#     if not os.path.exists(output_file):
#         ffmpeg.input(input_file).output(output_file, vcodec="libx264", acodec="aac").run(overwrite_output=True)
#         print(f"Conversion successful: {output_file}")


import os
import subprocess

for filename in os.listdir('./real-old/'):
    if filename.endswith('.mp4'):
        output_file = f"./real/{os.path.splitext(filename)[0]}.mp4"
        cmd = ['ffmpeg', '-i', f"./real-old/{filename}", '-an', '-y', output_file]
        subprocess.run(cmd)
        print(f"Processed: {filename} -> {output_file}")