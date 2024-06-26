import ffmpeg
import subprocess


subprocess.run(['aplay', '-l'])


stream = ffmpeg.input('audio=USB')
stream = ffmpeg.output(stream, 'formats=pulse', './pulse.wav')
ffmpeg.run(stream)




# # FFmpeg command
# ffmpeg_command = [
#     'ffmpeg',
#     '-f', 'pulse',
#     '-i', 'audio=default', '/tmp/pulse.wav', # Change to your virtual audio device name
#     '-f', 'mpegts',
#     'udp://localhost:12345'
# ]
#
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     exit()
