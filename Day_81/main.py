
morse_code = {
    "A":    "*-",
    'B':	'-***',
    'C':	'-*-*',
    'D':	'-**',
    'E':	'*',	
    'F':	'**-*',
    'G':	'--*',
    'H':	'****',
    'I':	'**',	
    'J':	'*---',
    'K':	'-*-',
    'L':	'*-**',
    'M':	'--',	
    'N':	'-*',	
    'O':	'---',
    'P':	'*--*',
    'Q':	'--*-',
    'R':	'*-*',
    'S':	'***',
    'T':	'-',	
    'U':	'**-',
    'V':	'***-',
    'W':	'*--',
    'X':	'-**-',
    'Y':	'-*--',
    'Z':	'--**',
    '1':    '*----'	,
    '2':	'**---'	,
    '3':	'***--'	,
    '4':	'****-'	,
    '5':	'*****'	,
    '6':	'-****'	,
    '7':	'--***'	,
    '8':	'---**'	,
    '9':	'----*'	,
    '0':	'-----',
    ".":	'*-*-*-',
    ",":	'--**--',
    ";":	'---***',
    "?":	'**--**',
    "'":	'*----*',
    '-':	'-****-',
    "(":	'-*--*-',
    '"':    '*-**-*',
}

def main():
    user_plain_text = input("Type text to translate into morse code: ")
    user_morse_code = ''
    for letter in user_plain_text:
        user_morse_code += morse_code.get(letter.upper(), letter)
        user_morse_code += " "
    print(f"Your text as a morse code:\n{user_morse_code}")



if __name__ == '__main__':
    main()