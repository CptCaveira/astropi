from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(270)

g = (255, 255, 0)
r = (255, 0, 0)
s = (0, 0, 0)
gr = (200, 200, 200)

sense.show_message("My name should be -------", back_colour=gr, text_colour=r)

def bocafechada():
    g = (255, 255, 0)
    r = (255, 0, 0)
    s = (0, 0, 0)
    gr = (200, 200, 200)
    
    banana1 = [
    gr, gr, gr, gr, gr, gr, gr, gr,
    gr, gr, g, g, g, s, s, gr,
    gr, g, s, g, s, gr, gr, gr,
    gr, g, g, g, gr, gr, gr, gr,
    gr, r, r, r, gr, gr, gr, gr,
    gr, g, g, g, g, gr, gr, gr,
    gr, gr, g, g, g, s, gr, gr,
    gr, gr, gr, gr, gr, gr, gr, gr
    ]
    return banana1

def bocaaberta():
    g = (255, 255, 0)
    r = (255, 0, 0)
    s = (0, 0, 0)
    gr = (200, 200, 200)

    banana2 = [
    gr, gr, gr, gr, gr, gr, gr, gr,
    gr, gr, g, g, g, s, s, gr,
    gr, g, s, g, s, gr, gr, gr,
    gr, g, r, r, gr, gr, gr, gr,
    gr, r, s, s, gr, gr, gr, gr,
    gr, g, r, r, g, gr, gr, gr,
    gr, gr, g, g, g, s, gr, gr,
    gr, gr, gr, gr, gr, gr, gr, gr
    ]
    return banana2

sense.set_pixels(bocafechada())
for count in range(3):
    sense.set_pixels(bocaaberta())
    sleep(0.5)
    sense.set_pixels(bocafechada())
    sleep(0.5)

humidity = sense.get_temperature()
# sense.show_message("ISS is Cool!",scroll_speed=0.2 )
sense.show_message("Humidity is " + str(round(humidity,2)) + "%", back_colour=gr, text_colour=r)


