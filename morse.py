english_morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

def load_file(filename: str) -> list[str]:
    """
    Returns the lines in an input file.

    Args:
        filename(str): path to input file
    Returns:
        list[str]: list of lines from input file
    """
    infile = open(filename, "r")
    lines = infile.readlines()
    infile.close()
    return lines

def main():
    
    
    
    #print("Enter -m for english to morse and -t for morse to english. \nFollow your command with the input file name and output file name.\CMD>", end="")
    #user_str = input()
    #args = user_str.split(" ")
    #conversion_type, infile_name, outfile_names = args
    
    lines = load_file("english.txt")
    print(lines)
    #if conversion_type == "-m":
        # TO DO: call converted_lines = convert_english_to_morse(lines)
     #   pass
    #elif conversion_type == "-t":
        # TO DO: call converted_lines = convert_morse_to_english(lines)
     #   pass
    # TO DO: call save_file(outfile_name, converted_lines)
    

main() 