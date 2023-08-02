import math
import random
import cairo
import imageio
import numpy as np

WIDTH, HEIGHT = 256, 256
NUM_FRAMES = 100
SPARKLE_FACTOR = 5  # Increase this value for more sparkly effect

def draw_frame(surface, frame_num):
    ctx = cairo.Context(surface)
    ctx.scale(WIDTH, HEIGHT)

    # Background
    ctx.rectangle(0, 0, 1, 1)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()

    # Stars
    for _ in range(3 * SPARKLE_FACTOR):  # More stars for a sparkly effect
        x = random.random()
        y = random.random()
        size = (random.random() + 1) / 2 * 0.01
        ctx.arc(x, y, size, 0, 2 * math.pi)
        ctx.set_source_rgb(1, 1, 1)
        ctx.fill()

    # Glitter
    for _ in range(5 * SPARKLE_FACTOR):  # More glitter for a sparkly effect
        x = random.random()
        y = random.random()
        size = (random.random() + 1) / 2 * 0.02
        ctx.arc(x, y, size, 0, 2 * math.pi)
        ctx.set_source_rgb(1, 1, 0)
        ctx.fill()

images = []
for frame_num in range(NUM_FRAMES + 1):  # Add one extra frame for the loop
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    draw_frame(surface, frame_num)

    # Convert the cairo surface to a numpy array
    buf = surface.get_data()
    arr = np.ndarray(shape=(HEIGHT, WIDTH, 4), buffer=buf, dtype=np.uint8)

    images.append(arr)

# Create loopable gif by appending the first frame to the end
images.append(images[0])

# Create gif
imageio.mimsave('glittery_star_loop.gif', images, duration=0.2)  # Adjust the duration as needed
