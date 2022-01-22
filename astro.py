from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
g = (255, 255, 0)
r = (255, 0, 0)
s = (0, 0, 0)
gr = (50, 50, 50)
banana = [
  gr, gr, gr, gr, gr, gr, gr, gr,
  gr, gr, gr, g, g, s, s, gr,
  gr, gr, s, g, s, gr, gr, gr,
  gr, g, g, g, gr, gr, gr, gr,
  gr, r, r, r, gr, gr, gr, gr,
  gr, gr, g, g, g, gr, gr, gr,
  gr, gr, gr, g, g, s, gr, gr,
  gr, gr, gr, gr, gr, gr, gr, gr
]
humid = sense.get_humidity()
print(humid)
sense.set_pixels(banana)
