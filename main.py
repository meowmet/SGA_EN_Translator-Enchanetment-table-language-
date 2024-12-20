english_to_sga = {
    'a': 'ᔑ', 'b': 'ʖ', 'c': 'ᓵ', 'd': '↸', 'e': 'ᒷ',
    'f': '⎓', 'g': '⊣', 'h': '⍑', 'i': '╎', 'j': '⋮',
    'k': 'ꖌ', 'l': 'ꖎ', 'm': 'ᒲ', 'n': 'リ', 'o': '!',
    'p': 'ᑑ', 'q': '∷', 'r': 'ᓭ', 's': 'ℸ', 't': '⚍',
    'u': '⍊', 'v': '∴', 'w': '̇/', 'x': '||', 'y': '⨅',
    'z': '⍎'
}

sga_to_english = {v: k for k, v in english_to_sga.items()} 
def translate_english_to_sga(english_text):
    result = []
    for char in english_text.lower():  
        if char in english_to_sga:
            result.append(english_to_sga[char])
        else:
            result.append(char)  
    return ''.join(result)

def translate_sga_to_english(sga_text):
    result = []
    for char in sga_text:
        if char in sga_to_english:
            result.append(sga_to_english[char])
        else:
            result.append(char) 
    return ''.join(result)

print("Minecraft Enchantment Table Translator")
print("1. English to SGA")
print("2. SGA to English")
choice = input("Choose an option (1 or 2): ")

if choice == '1':
    english_text = input("Enter text in English: ")
    sga_translation = translate_english_to_sga(english_text)
    print(f"Translation to SGA: {sga_translation}")

elif choice == '2':
    sga_text = input("Enter text in SGA: ")
    english_translation = translate_sga_to_english(sga_text)
    print(f"Translation to English: {english_translation}")

else:
    print("Invalid choice. Please restart the program and choose 1 or 2.")
