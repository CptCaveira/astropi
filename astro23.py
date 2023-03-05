# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

dgr = (0, 128, 0)
rot = (255, 0, 0)
org = (255, 140, 0)
gel = (255, 255, 0)
hgr = (124, 252, 0)
rbl = (0, 0, 255)
pur = (153, 50, 204)
bra = (255, 222, 173)
blu = (135, 206, 250)
sch = (0, 0, 0)
wei = (255, 255, 255)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image
col = sense.color.color
# Display the image

wahl = []


wahl.append([
    blu, blu, blu, blu, blu, blu, blu, blu,
    blu, blu, blu, blu, blu, blu, blu, blu,
    blu, blu, blu, blu, blu, blu, blu, blu,
    blu, blu, blu, blu, blu, blu, blu, blu,
    blu, blu, sch, sch, blu, blu, blu, blu,
    blu, sch, sch, wei, sch, blu, blu, blu,
    blu, sch, sch, sch, sch, sch, blu, sch,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    blu, blu, blu, blu, blu, blu, blu, blu,
    blu, blu, blu, blu, blu, blu, blu, blu,
    blu, blu, blu, wei, blu, blu, blu, blu,
    blu, blu, blu, wei, blu, blu, blu, blu,
    blu, blu, sch, sch, blu, blu, blu, blu,
    blu, sch, sch, wei, sch, blu, blu, blu,
    blu, sch, sch, sch, sch, sch, blu, sch,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    blu, blu, blu, blu, blu, blu, blu, blu,
    blu, blu, blu, wei, blu, blu, blu, blu,
    blu, blu, wei, wei, blu, blu, blu, blu,
    blu, blu, blu, wei, blu, blu, blu, blu,
    blu, blu, sch, sch, blu, blu, blu, blu,
    blu, sch, sch, wei, sch, blu, blu, blu,
    blu, sch, sch, sch, sch, sch, blu, sch,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    blu, blu, blu, wei, blu, blu, blu, blu,
    blu, blu, wei, wei, wei, blu, blu, blu,
    blu, blu, wei, wei, wei, blu, blu, blu,
    blu, blu, blu, wei, blu, blu, blu, blu,
    blu, blu, sch, sch, blu, blu, blu, blu,
    blu, sch, sch, wei, sch, blu, blu, blu,
    blu, sch, sch, sch, sch, sch, blu, sch,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    blu, blu, blu, wei, blu, blu, blu, blu,
    blu, blu, wei, wei, wei, blu, blu, blu,
    blu, blu, wei, blu, wei, blu, blu, blu,
    blu, blu, blu, blu, blu, blu, blu, blu,
    blu, blu, sch, sch, blu, blu, blu, blu,
    blu, sch, sch, wei, sch, blu, blu, blu,
    blu, sch, sch, sch, sch, sch, blu, sch,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

# rainbow starts
wahl.append([
    rot, blu, blu, blu, blu, blu, blu, blu,
    org, blu, blu, blu, blu, blu, blu, blu,
    gel, blu, blu, blu, blu, blu, blu, blu,
    hgr, blu, blu, blu, blu, blu, blu, blu,
    rbl, blu, sch, sch, blu, blu, blu, blu,
    pur, sch, sch, wei, sch, blu, blu, blu,
    blu, sch, sch, sch, sch, sch, blu, sch,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, blu, blu, blu, blu, blu, blu,
    org, gel, blu, blu, blu, blu, blu, blu,
    gel, hgr, blu, blu, blu, blu, blu, blu,
    hgr, rbl, blu, blu, blu, blu, blu, blu,
    rbl, pur, sch, sch, blu, blu, blu, blu,
    pur, sch, sch, wei, sch, blu, blu, blu,
    blu, sch, sch, sch, sch, sch, blu, sch,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, blu, blu, blu, blu, blu,
    org, gel, hgr, blu, blu, blu, blu, blu,
    gel, hgr, rbl, blu, blu, blu, blu, blu,
    hgr, rbl, pur, blu, blu, blu, blu, blu,
    rbl, pur, sch, sch, blu, blu, blu, blu,
    pur, sch, sch, wei, sch, blu, blu, blu,
    blu, sch, sch, sch, sch, sch, blu, sch,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, blu, blu, blu, blu,
    org, gel, hgr, rbl, blu, blu, blu, blu,
    gel, hgr, rbl, pur, blu, blu, blu, blu,
    hgr, rbl, pur, blu, blu, blu, blu, blu,
    rbl, pur, sch, sch, blu, blu, blu, blu,
    pur, sch, sch, wei, sch, blu, blu, blu,
    blu, sch, sch, sch, sch, sch, blu, sch,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, blu, blu, blu,
    org, gel, hgr, rbl, pur, blu, blu, blu,
    gel, hgr, rbl, pur, blu, blu, blu, blu,
    hgr, rbl, pur, blu, blu, blu, blu, blu,
    rbl, pur, sch, sch, blu, blu, blu, blu,
    pur, sch, sch, wei, sch, blu, blu, blu,
    blu, sch, sch, sch, sch, sch, blu, sch,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, pur, blu, blu,
    org, gel, hgr, rbl, pur, blu, blu, blu,
    gel, hgr, rbl, pur, blu, blu, blu, blu,
    hgr, rbl, pur, blu, blu, blu, blu, blu,
    rbl, pur, sch, sch, blu, blu, blu, blu,
    pur, sch, sch, wei, sch, blu, blu, blu,
    blu, sch, sch, sch, sch, sch, blu, sch,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, pur, blu, blu,
    org, gel, hgr, rbl, pur, blu, blu, blu,
    gel, hgr, rbl, pur, blu, blu, blu, blu,
    hgr, rbl, pur, blu, blu, blu, blu, blu,
    rbl, pur, blu, blu, blu, blu, blu, blu,
    pur, blu, sch, sch, blu, blu, blu, blu,
    blu, sch, sch, wei, sch, blu, blu, blu,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, pur, blu, blu,
    org, gel, hgr, rbl, pur, blu, blu, blu,
    gel, hgr, rbl, pur, blu, blu, blu, blu,
    hgr, rbl, pur, blu, blu, blu, blu, blu,
    rbl, pur, blu, blu, blu, blu, blu, blu,
    pur, blu, blu, blu, blu, blu, blu, blu,
    blu, blu, sch, sch, blu, blu, blu, blu,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, pur, blu, blu,
    org, gel, hgr, rbl, pur, blu, blu, blu,
    gel, hgr, rbl, pur, blu, blu, blu, blu,
    hgr, rbl, pur, blu, blu, blu, blu, blu,
    rbl, pur, blu, blu, blu, blu, blu, blu,
    pur, blu, blu, blu, blu, blu, blu, blu,
    blu, blu, blu, blu, blu, blu, blu, blu,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, pur, blu, blu,
    org, gel, hgr, rbl, pur, blu, blu, blu,
    gel, hgr, rbl, pur, blu, blu, blu, blu,
    hgr, rbl, pur, blu, blu, blu, blu, blu,
    rbl, pur, blu, blu, blu, blu, blu, blu,
    pur, blu, blu, blu, blu, blu, blu, blu,
    blu, blu, blu, blu, blu, blu, blu, sch,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, pur, blu, blu,
    org, gel, hgr, rbl, pur, blu, blu, blu,
    gel, hgr, rbl, pur, blu, blu, blu, blu,
    hgr, rbl, pur, blu, blu, blu, blu, blu,
    rbl, pur, blu, blu, blu, blu, blu, blu,
    pur, blu, blu, blu, blu, blu, sch, blu,
    blu, blu, blu, blu, blu, blu, sch, sch,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, pur, blu, blu,
    org, gel, hgr, rbl, pur, blu, blu, blu,
    gel, hgr, rbl, pur, blu, blu, blu, blu,
    hgr, rbl, pur, blu, blu, blu, blu, blu,
    rbl, pur, blu, blu, blu, sch, blu, blu,
    pur, blu, blu, blu, blu, sch, sch, blu,
    blu, blu, blu, blu, sch, sch, blu, blu,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, pur, blu, blu,
    org, gel, hgr, rbl, pur, blu, blu, blu,
    gel, hgr, rbl, pur, blu, blu, blu, blu,
    hgr, rbl, pur, blu, blu, sch, blu, blu,
    rbl, pur, blu, sch, sch, blu, blu, blu,
    pur, blu, blu, blu, sch, blu, blu, blu,
    blu, blu, blu, blu, sch, sch, blu, blu,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, pur, blu, blu,
    org, gel, hgr, rbl, pur, blu, blu, blu,
    gel, hgr, rbl, pur, blu, blu, blu, blu,
    hgr, rbl, pur, blu, blu, blu, blu, blu,
    rbl, pur, blu, blu, blu, sch, blu, blu,
    pur, blu, blu, sch, sch, blu, blu, blu,
    blu, blu, blu, blu, sch, blu, blu, blu,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, pur, blu, blu,
    org, gel, hgr, rbl, pur, blu, blu, blu,
    gel, hgr, rbl, pur, blu, blu, blu, blu,
    hgr, rbl, pur, blu, blu, blu, blu, blu,
    rbl, pur, blu, blu, blu, blu, blu, blu,
    pur, blu, blu, blu, sch, blu, blu, blu,
    blu, blu, blu, sch, sch, blu, blu, blu,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, pur, blu, blu,
    org, gel, hgr, rbl, pur, blu, blu, blu,
    gel, hgr, rbl, pur, blu, blu, blu, blu,
    hgr, rbl, pur, blu, blu, blu, blu, blu,
    rbl, pur, blu, blu, blu, blu, blu, blu,
    pur, blu, blu, blu, blu, blu, blu, blu,
    blu, blu, blu, blu, sch, blu, blu, blu,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, pur, blu, blu,
    org, gel, hgr, rbl, pur, blu, blu, blu,
    gel, hgr, rbl, pur, blu, blu, blu, blu,
    hgr, rbl, pur, blu, blu, blu, blu, blu,
    rbl, pur, blu, blu, blu, blu, blu, blu,
    pur, blu, blu, blu, blu, blu, blu, blu,
    blu, blu, blu, blu, blu, blu, blu, blu,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, pur, blu, blu,
    org, gel, hgr, rbl, pur, blu, blu, blu,
    gel, hgr, rbl, pur, blu, blu, blu, blu,
    hgr, rbl, pur, col, col, blu, blu, blu,
    rbl, pur, blu, col, col, blu, blu, blu,
    pur, blu, blu, blu, blu, blu, blu, blu,
    blu, blu, blu, blu, blu, blu, blu, blu,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, pur, blu, blu,
    org, gel, hgr, rbl, pur, blu, blu, blu,
    gel, hgr, col, col, col, col, blu, blu,
    hgr, rbl, col, sch, sch, col, blu, blu,
    rbl, pur, col, sch, sch, col, blu, blu,
    pur, blu, col, col, col, col, blu, blu,
    blu, blu, blu, blu, blu, blu, blu, blu,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    rot, org, gel, hgr, rbl, pur, blu, blu,
    org, col, col, col, col, col, col, blu,
    gel, col, sch, sch, sch, sch, col, blu,
    hgr, col, sch, sch, sch, sch, col, blu,
    rbl, col, sch, sch, sch, sch, col, blu,
    pur, col, sch, sch, sch, sch, col, blu,
    blu, col, col, col, col, col, col, blu,
    rbl, rbl, rbl, rbl, rbl, rbl, rbl, rbl
])

wahl.append([
    col, col, col, col, col, col, col, col,
    col, sch, sch, sch, sch, sch, sch, col,
    col, sch, sch, sch, sch, sch, sch, col,
    col, sch, sch, sch, sch, sch, sch, col,
    col, sch, sch, sch, sch, sch, sch, col,
    col, sch, sch, sch, sch, sch, sch, col,
    col, sch, sch, sch, sch, sch, sch, col,
    col, col, col, col, col, col, col, col
])

wahl.append([
    sch, sch, sch, sch, sch, sch, sch, sch,
    sch, sch, sch, sch, sch, sch, sch, sch,
    sch, sch, sch, sch, sch, sch, sch, sch,
    sch, sch, sch, sch, sch, sch, sch, sch,
    sch, sch, sch, sch, sch, sch, sch, sch,
    sch, sch, sch, sch, sch, sch, sch, sch,
    sch, sch, sch, sch, sch, sch, sch, sch,
    sch, sch, sch, sch, sch, sch, sch, sch
])
for i in range(0, len(wahl)):
    sense.set_pixels(wahl[i])
    sleep(0.1)
