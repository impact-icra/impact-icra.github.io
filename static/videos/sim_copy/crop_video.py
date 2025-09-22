import os
from moviepy.editor import VideoFileClip, vfx

# input_video = "scene206-table_top-center-lapp_video.mp4"
# output_video = f"{input_video[:-4]}_crop.mp4"


def crop_video(input_video):
    output_video = f"../sim/{input_video}"
    clip = VideoFileClip(input_video)
    # print("Width x Height:", clip.size) 

    # A) crop to a box (x1,y1,x2,y2) in pixels
    cropped = clip.fx(vfx.crop, x1=150, y1=200, x2=874, y2=768)
    print("Cropped Width x Height:", cropped.size)

    cropped = cropped.subclip(0.3, cropped.duration) 

    cropped = cropped.without_audio()
    # cropped = cropped.resize((1720, 1080)) 
    # cropped = cropped.fx(vfx.speedx, factor=0.25)

    cropped.write_videofile(output_video, codec="libx264", preset="medium", bitrate="4000k", 
        ffmpeg_params=["-vf", f"scale={cropped.w}:{cropped.h}"])



if __name__ == "__main__":
    input_dir = "./"
    for filename in os.listdir(input_dir):
        if filename.startswith("scene207"):
            input_video = os.path.join(input_dir, filename)
            crop_video(input_video)