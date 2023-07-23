import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image

# Open the animated GIF file
gif_file = 'animated.gif'

# Open the text file for appending
with open('qr-test-decoded-gif.txt', 'a') as file:
    gif = Image.open(gif_file)
    try:
        while True:
            # Get the current frame
            current_frame = gif.tell()

            # Convert the frame to grayscale
            gray_frame = cv2.cvtColor(cv2.cvtColor(np.array(gif), cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY)

            # Decode QR codes from the frame
            decoded_objects = decode(gray_frame)

            # Process the decoded data and write to the text file
            for obj in decoded_objects:
                decoded_data = obj.data.decode('utf-8')
                print('Decoded data:', decoded_data)
                file.write(decoded_data + '\n')

            # Move to the next frame
            gif.seek(current_frame + 1)
    except EOFError:
        pass

# No need to release anything for a GIF
