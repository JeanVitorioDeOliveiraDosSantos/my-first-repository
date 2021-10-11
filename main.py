def hello():
    print("Hello World!")

def print_name(name):
    print(name)

def print_sobrenome(sobrenome):
    print(sobrenome)

if __name__ == '__main__':
    hello()

    print_name("Jean")
    print_sobrenome("Santos")

def muda_nomes(nome):
    nome = nome .upper()
    print (nome)

pessoa = muda_nomes("Otavio")