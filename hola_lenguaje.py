import os

def main():
    username = os.environ.get("USERNAME")
    city = os.environ.get("CITY")
    language = os.environ.get("LANGUAGE")
    
    print(f"Hola, {username}, tu lenguaje favorito es {language}")
    print("Vives en " + city)

if __name__ == "__main__":
    main()
