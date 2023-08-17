import os
from moviepy.editor import VideoFileClip


def toMP3(path, file):
    file, extension = file.split('.')
    video = VideoFileClip(os.path.join(path, file + '.' + extension))
    video.audio.write_audiofile(os.path.join(path, file + '.mp3'))


conversions = {'mp3': toMP3}
