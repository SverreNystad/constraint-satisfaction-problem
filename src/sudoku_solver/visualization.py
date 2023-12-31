from PIL import Image, ImageDraw, ImageFont


def generate_sudoku_image(solution, title: str, output_path="docs/images/"):
    # Create a new image with white background
    img = Image.new('RGB', (450, 450), color = (255, 255, 255))
    canvas = ImageDraw.Draw(img)
    
    # Draw grid
    for i in range(10):
        line_width = 3 if i % 3 == 0 else 1
        canvas.line([(i*50, 0), (i*50, 450)], fill=(0,0,0), width=line_width)
        canvas.line([(0, i*50), (450, i*50)], fill=(0,0,0), width=line_width)
    
    # Load a font in the current directory
    fnt = ImageFont.load_default()
    size = 30
    
    fnt = ImageFont.truetype("arial", size)
    # Set color to red
    color = (255, 0, 0)
    
    # Fill grid with numbers
    for row in range(9):
        for col in range(9):
            val = solution['%d-%d' % (row, col)]
            if len(val) == 1:
                w, h = (len(val) * 15, 30)  # Approximating width and using a standard height
                number_pos = ((col*50)+(25-w/2), (row*50)+(25-h/2))
                number = val[0]
                canvas.text(number_pos, number, font=fnt, fill=color)
    
    # Save the image
    img.save(output_path + title + ".png")
    img.show()
