def main():
    hello("Namit")
    world("Goodbye")

def hello(name):
    print("Hello, "+name)

def world(message):
    print(f"{message}, World!")

if __name__=="__main__":
    main()