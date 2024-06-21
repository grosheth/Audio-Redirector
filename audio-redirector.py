import ffmpeg



# stream = ffmpeg.formats('pulse')
stream = ffmpeg.input('audio=default')
stream = ffmpeg.output(stream, 'format=wav', '/tmp/pulse.wav')
ffmpeg.run(stream)




# FFmpeg command
ffmpeg_command = [
    'ffmpeg',
    '-f', 'pulse',
    '-i', 'audio=default', '/tmp/pulse.wav', # Change to your virtual audio device name
    '-f', 'mpegts',
    'udp://localhost:12345'
]
#
try:
    while True:
        pass
except KeyboardInterrupt:
    exit()
