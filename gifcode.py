import moviepy
import moviepy.editor
from moviepy.editor import VideoFileClip
clip=VideoFileClip("sample-10s.mp4")
clip.write_gif("mygif.gif",fps=5)
clip = clip.resize(0.5)