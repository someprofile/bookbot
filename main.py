def main():

    
    file_path = "books/frankenstein.txt"
    file_contents = read_in_text(file_path)
    
    
    words = len(file_contents.split())
    
    
    letters = split_and_analyze(file_contents)
    #print(letters)
    
    print_report(file_path, words, letters)
        



def read_in_text(path):
    with open(path) as f:
        x = f.read()
    return x




def split_and_analyze(text):
    
    character_list = list(text)
    character_dict = {
        "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0
        }
    
    
    for x in character_list:
#        if x == " " or x == "." or x == "'" or x == "!" or x == "/" or x == "?" or x == ",":
#            continue
#turned out to be unnessecary due to if statement in for loop requiring characters being in dictionary.  

        for i in character_dict:
            if x.lower() == i:
                character_dict[i] += 1
                
    
    
    return character_dict
    

def print_report(path, words_total, letters_total_dict):
    print(f"---Begin report of {path} ---")
    print(f"{words_total} words were found in the text.")
    print("")
    #i = list(letters_total_dict.values())
    #i = letters_total_dict.values()
    #e = i.sort()
    
    #print(i)
    
    
    for w in sorted(letters_total_dict, key = letters_total_dict.get, reverse = True):
        print(f"The {w} character was found {letters_total_dict[w]} times within the text.")
        
    print("")
    print("---End Report---")
    #for beep in i:
    #    print(letters_total_dict{beep})
    
    
    
    return
    






    



main()