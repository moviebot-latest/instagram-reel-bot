from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
from config import MUSIC_FILE, OUTPUT_FILE
from subtitles import generate_subtitles

def edit_video(clip_path):

    video = VideoFileClip(clip_path)

    music = AudioFileClip(MUSIC_FILE)

    subtitles = generate_subtitles(clip_path)

    text = TextClip(subtitles, fontsize=40, color="white")

    text = text.set_position(("center","bottom")).set_duration(video.duration)

    final = CompositeVideoClip([video, text]).set_audio(music)

    final.write_videofile(OUTPUT_FILE)

    return OUTPUT_FILE
