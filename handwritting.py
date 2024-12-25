from PIL import Image, ImageDraw, ImageFont

# Create an image
img = Image.new("RGB", (2000, 1000), color="white")

# Initialize a draw object
draw = ImageDraw.Draw(img)

# Load the Roboto Black font (ensure the file is in the same directory as your script)
font = ImageFont.truetype("DancingScript-VariableFont_wght.ttf", size=40)

# Write text on the image
text = '''Python is a versatile, high-level programming language known for its simplicity and readability. 
Developed by Guido van Rossum in 1991, Python supports multiple programming paradigms, including procedural,
object-oriented, and functional programming. 
Its extensive standard library and vast ecosystem of third-party packages make it ideal for 
tasks like web development, data analysis, artificial intelligence, and scientific computing. Python’s 
clean syntax and beginner-friendly nature have made it one of the most popular languages globally, 
empowering developers to create efficient, scalable, and innovative solutions. With a strong community and
continuous advancements, Python continues to shape the future of technology.'''
draw.text((50, 100), text, font=font, fill="black")

# Save the image
img.save("handwriting_output.png")

print("Image created successfully: handwriting_output.png")