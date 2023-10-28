import pyfiglet

def generate_ascii_art(name):
    try:
        ascii_art = pyfiglet.figlet_format(name)
        return ascii_art
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    ascii_art = generate_ascii_art(user_name)
    
    print("\nASCII Art for your name:")
    print(ascii_art)
