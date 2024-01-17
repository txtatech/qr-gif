# qr-gif
A method to extract code (javascript in this example) from qr codes in an animated gif, print it to the terminal and output it as a text file.

A fork of https://github.com/txtatech/qr-vid

## QR-GIF Decoder

### Description

This Python script decodes QR codes from an animated GIF file and writes the decoded data to a text file and prints it to the terminal. It uses OpenCV for image processing and Pyzbar for QR code decoding.

### Installation

1. Ensure you have Python 3 installed on your system.
2. Install the required Python packages using pip:

```bash
pip install opencv-python-headless pyzbar pillow
```

### Usage

0. Make an animated gif of qr codes from a directory containing png files with qr-gif.py

1. Save your animated GIF file containing QR codes to a location on your system.

2. Open the `qr-gif-decode.py` script in a text editor.

3. Replace `'path/to/animated.gif'` with the actual file path of your animated GIF in the script.

4. Run the script:

```bash
python qr-gif-decode.py
```

5. The script will decode the QR codes frame by frame and print the decoded data to the console. Additionally, it will write the decoded data to a text file named `qr-test-decoded.txt` in the same directory as the script.

6. Press `Ctrl + C` to stop the script when you want to exit.

### Notes

- This script uses OpenCV to process the animated GIF frames and Pyzbar to decode the QR codes.
- The GIF must contain QR codes for successful decoding.
- If any errors occur during decoding, they will be printed to the console.

### License

This script is open-source and licensed under the [MIT License](https://opensource.org/licenses/MIT).
