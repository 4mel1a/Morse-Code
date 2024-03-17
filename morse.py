from tkinter import *

def breakToWords(text):
    return text.split(" ")

def breakToCharacters(text):
    return list(text)

def characterToMorse(character):
    morseTrans = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
    '\n':'',
}
    return morseTrans[character]

def toMorse(text,output):
    textList = breakToWords(text)
    for i in range(len(textList)):
        textList[i] = breakToCharacters(textList[i])
    for i in range(len(textList)):
        for j in range(len(textList[i])):
            textList[i][j] = characterToMorse(textList[i][j])
        textList[i] = "".join(textList[i])
    output.config(text="|".join(textList))
    

def main():
    window = Tk()
    window.title("Morse Code Translator")
    window.geometry("300x200")

    plainTextEntry = Text(window,height=1,width=20)
    plainTextEntry.grid(column=0,row=0,columnspan=4)

    transButton = Button(window,text="Translate",command=lambda: toMorse(plainTextEntry.get("1.0",END).upper(),output), width=20)
    transButton.grid(column=0,row=1,columnspan=4)

    output = Label(window,text="")
    output.grid(column=0,row=2,columnspan=4)

    window.mainloop()

if __name__ == "__main__":
    main()