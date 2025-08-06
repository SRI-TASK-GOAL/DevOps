import pyfiglet

def print_ascii_art(text, font="straight"):
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        print(ascii_art)
    except:
        print(f"\n{text}\n")

print_ascii_art("Grey Hat Thamizha", font="big")
