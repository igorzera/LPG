from random import randint,random,randrange,choice

numero_de_pessoas = 4

for c in range(numero_de_pessoas):
    print(1)

    n_letras = randint(3,7)
    nome = ''
    for i in range(n_letras):
        nome += chr(randint(97,122))
    
    n_sobrenomes = randint(1,2)

    for i in range(n_sobrenomes):
        nome += ' '
        sobrenome = ''
        for i in range(n_letras):
            sobrenome += chr(randint(97,122))
        nome += sobrenome
    
    nome = nome.title()

    print(nome)

    emails = ['@gmail.com','@hotmail.com','@outlook.com','@udesc.com']
    print(nome.split()[0].lower() + choice(emails))

    # endereco

    ruas = ['Jõao Colin','Ministro Calógeras','Blumenau','Santos Drumont','Dona Fancisca']
    print(choice(ruas))

    print(randint(100,3000))

    complementos = ['casa', str(randint(100,900))]
    print(choice(complementos))

    bairros = ['Bom Retiro', 'Centro', 'Itaum', 'Escolinha', 'Saguaçu']
    print(choice(bairros))

    print(str(randint(11111,99999)) + '-' + str(randint(111,999)))

    cidades = ['Mafra', 'Joinville', 'Porto Alegre', 'Campina Grande']
    print(choice(cidades))

    estados = ['SC', 'PR', 'RS', 'PA', 'SP', 'RJ']
    print(choice(estados))

    paises = ['Brasil', 'Russia', 'EUA', 'Paraguai', 'Argentina']
    randpais = randrange(len(paises))
    print(paises[randpais])

    codigointernacional = ['55','7','1','595','54']
    print(codigointernacional[randpais])

    print(randint(10,99))

    numero_telefone = ''
    for i in range(8):
        numero_telefone += str(randint(0,9))
    print(numero_telefone)

    print(randint(1,30))
    print(randint(1,12))
    print(randint(1960,2005))

    n_lero_lero = randint(5,20)
    lero_lero = ''
    for i in range(n_lero_lero):
        if i!=0:
            lero_lero += ' '
        palavra = ''
        for i in range(n_letras):
            palavra += chr(randint(97,122))
        lero_lero += palavra
        
    lero_lero += '.'
    print(lero_lero[1].upper() + lero_lero)