#good luck brother
import random



def load_image_data(filename: str) -> list[list[list[int]]]:
    """
    Returns the lines in an input file.

    Args:
        filename(str): path to input file
    Returns:
        list[str]: list of lines from input file
    """
    infile = open(filename, "r")
    specification = infile.readline()
    col, row = infile.readline().split()
    colorMax = infile.readline().strip()
    image = [[[0, 0, 0] for c in range(int(col))] for r in range(int(row))] #initializing array

    #trackers along image array
    line_index = 0
    c = 0
    rgbValues = []


    #Loop to traverse each RGB value in PPM
    for line in infile:
        for color in line.split():
            rgbValues.append(int(color))

            if(len(rgbValues) == 3):
                image[line_index][c] = rgbValues
                rgbValues = []

                c+=1
                if c == int(col):
                    c = 0
                    line_index += 1

                    if line_index == int(row):
                        infile.close()
                        return image

def load_image_info(filename: str) -> str:
    """
    Returns heading of ppm file
    """
    infile = open(filename, "r")
    specification = infile.readline().strip()
    col, row = infile.readline().split()
    colorMax = infile.readline().strip()

    return specification, col, row, colorMax

def write_image_data(data: list[list[list[int]]], infile: str, outfile: str) -> None:
    outfile = open(outfile, "w")
    specification, col, row, colorMax = load_image_info(infile)
    outfile.write(specification + "\n")
    outfile.write(col + " " + row + "\n")
    outfile.write(colorMax + "\n")
    outfile.write("\n")
    

    for row in data:
        for col in row:
            for pixel in col:
                outfile.write(str(pixel))
                outfile.write("   ")
                pass
        outfile.write("\n")
    
"""
Image modifications:
apply_vertical_flip X
apply_horizontal_flip X
remove_red X
remove_green X
remove_blue X
apply_high_contrast X
add_random_noise
apply_grayscale
"""

def vertical_flip(data: list[list[list[int]]]) -> list[list[list[int]]]:
    return data[::-1]

def horizontal_flip(data: list[list[list[int]]]) -> list[list[list[int]]]:
    return [row[::-1] for row in data]

def remove_red(data: list[list[list[int]]]) -> list[list[list[int]]]:
    for row in range(len(data)):
        for col in range(len(data[row])):
            data[row][col][0] = 0
            pass

    return data
def remove_green(data: list[list[list[int]]]) -> list[list[list[int]]]:
    for row in range(len(data)):
        for col in range(len(data[row])):
            data[row][col][1] = 0
            pass
    
    return data

def remove_blue(data: list[list[list[int]]]) -> list[list[list[int]]]:
    for row in range(len(data)):
        for col in range(len(data[row])):
            data[row][col][2] = 0
            pass
    
    return data

def high_contrast(data: list[list[list[int]]]) -> list[list[list[int]]]:
    for row in range(len(data)):
        for col in range(len(data[row])):
            for i in range(3):
                if data[row][col][i] > 128:
                    data[row][col][i] = 255
                else:
                    data[row][col][i] = 0


    return data

def random_noise(data: list[list[list[int]]]) -> list[list[list[int]]]: 
    for row in range(len(data)):
        for col in range(len(data[row])):
            for i in range(3):
                if data[row][col][i] >= 205:
                    data[row][col][i] -= random.randint(0,50)
                elif data[row][col][i] <= 55:
                    data[row][col][i] += random.randint(0,50)
                else:
                    coinflip = random.randint(0,1)
                    if coinflip == 1:
                        data[row][col][i] += random.randint(0,50)
                    else: 
                        data[row][col][i] -= random.randint(0,50)
                        

    return data  
                

def apply_modification(data: list[list[list[int]]], mod: str) -> list[list[list[int]]]:
    return "Not finished yet"



def main():

    lines = load_image_data("ny.ppm")
    specification, col, row, colorMax = load_image_info("ny.ppm")
    print(lines)
    print(specification, col, row, colorMax)
    mod = random_noise(lines)
    write_image_data(mod, "ny.ppm", "out_ny.ppm")
    

main()