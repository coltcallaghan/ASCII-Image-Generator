import PIL.Image

#Get ASCII Characters
ASCII_characters = ["@","#","S","%","?","*","+",";",":",",","."]

#Resize Image
def resize(image, new_width=100):
    width, height = image.size
    ratio = height / width  
    print(ratio)
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

#Convert Image to grey
def greyify(image):
    grey_image = image.convert("L")
    return(grey_image)

#Convert pixels to ASCII Chars
def ASCIIfy(image):
    pixels = image.getdata()
    chars = "".join([ASCII_characters[pixel//25] for pixel in pixels])
    return(chars)


def main(new_width=100):
    #Input Image
    path = input("Enter path to image: \n")
    try: 
       image = PIL.Image.open(path)
    except:
        print(path + " not found")

    #Convert
    new_img_data = ASCIIfy(greyify(resize(image)))

    #Loop through formatting
    pixel_count = len(new_img_data)
    ascii_img = "\n".join(new_img_data[i:i+new_width] for i in range(0, pixel_count, new_width))

    #Print image
    print(ascii_img)

    #Save image as txt file
    with open("ascii_img.txt", "w") as f:
        f.write(ascii_img)

main()  
