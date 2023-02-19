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
for i in range(0, len(wahl)):
    sense.set_pixels(wahl[i])
    sleep(1)

# Set up the colour sensor
#sense.color.gain = 60 # Set the sensitivity of the sensor
#sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image

# Display the image
