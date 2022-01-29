from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(270)

g = (255, 255, 0)
r = (255, 0, 0)
s = (0, 0, 0)
gr = (100, 100, 100)

sense.show_message("My name should be -------", back_colour=gr, text_colour=r, scroll_speed=0.01)

def bocafechada():
       
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
for count in range(2):
    sense.set_pixels(bocaaberta())
    sleep(0.5)
    sense.set_pixels(bocafechada())
    sleep(0.5)

humidity = sense.get_humidity()
sense.show_message("Humidity is " + str(round(humidity)) + "%", back_colour=gr, text_colour=r, scroll_speed=0.1)
sense.show_message(" - ISS is COOL!", back_colour=gr, text_colour=r, scroll_speed=0.1)
sense.clear()


