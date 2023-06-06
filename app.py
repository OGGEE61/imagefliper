from PIL import Image

def flip_image(image_path, flip_direction):
    # Open the image file
    image = Image.open(image_path)

    # Flip the image
    if flip_direction == 'horizontal':
        flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif flip_direction == 'vertical':
        flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        print("Invalid flip direction. Please choose 'horizontal' or 'vertical'.")
        return

    # Show the original and flipped images
    image.show()
    flipped_image.show()

    # Save the flipped image
    flipped_image.save('flipped_image.jpg')

# Provide the path to your image file and the flip direction
image_path = 'test1.jpg'
flip_direction = 'horizontal'  # or 'vertical'

flip_image(image_path, flip_direction)