from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.resolution = (1920,1080)
camera.framerate = 30
camera.start_preview()
camera.awb_mode = 'fluorescent'
camera.exposure_mode = 'auto'
camera.annotate_text = "1920x1080 30fr auto exposure awb-flourescent"
camera.annotate_text_size = 50
camera.annotate_background = Color('black')
camera.annotate_foreground = Color('white')
camera.start_recording('/home/pi/darren.h264')
sleep(10)
#camera.capture('/home/pi/Desktop/fools.jpg')
camera.stop_recording()
camera.stop_preview()
