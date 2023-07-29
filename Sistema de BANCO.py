import time
def espera():
    time.sleep(2)
    print("\nEspere um momento, por favor...\n")
    time.sleep(3)
palavra_passe = 1234  #senha PIN = 1234
escolha = 0
saldo = 10000  #Saldo na conta 10000
escolha1 = True
while escolha1 ==True:
    time.sleep(2)
    print(f"\n\nBem-Vindo ao Banco do Silvio Santos\n")
    time.sleep(2)
    print("Insira o cartão\n")
    time.sleep(2)
    pin = int(input("Digite quatro digitos PIN : "))

    time.sleep(2)
    if pin != palavra_passe:
        print("\033[1;31m\nPIN incorreto !\033[m\n")
        time.sleep(2)
        print("Tente Novamente...\n\n\n")

    else:
        while escolha !=4:
            time.sleep(1)
            print("\n====== OPÇÕES ======\n")
            print("\n1. Ver Saldo")
            print("2. Depósito")
            print("3. Sacar")
            print("4. Cancelar\n")
            escolha=int(input("\nEscolha a sua opção: "))
            if escolha==1:
                espera()
                print(f"\n\nO seu Saldo é : \033[0;32;40m{saldo}\033[m\n")
                time.sleep(2)
            elif escolha==2:
                espera()
                deposito = float(input("Digite o valor de depósito: "))
                saldo = saldo +deposito
                time.sleep(2)
                print(f"\nO seu Depósito de {deposito} foi efectuada com sucesso\n")
            elif escolha == 3:
                espera()
                levantamento = float(input("Digite o valor de Saque: "))
                time.sleep(2)
                saldo = saldo - levantamento
                if saldo<0:
                    saldo = saldo + levantamento
                    print("\033[1;31m\nnão foi possível efetuar o Saque\033[m\n")
                    time.sleep(2)
                    print("\033[1;31mO saldo é inferior ao montante que que voce tem !\033[m\n")
                else:
                    print(f"\nSeu Saque de {levantamento} foi efetuado com sucesso\n")
            elif escolha == 4:
                time.sleep(2)
                print("\nPode tirar o cartão\n")
                time.sleep(1)
                print("Banco Silvio Santos Agradece...")
                time.sleep(2)
                print("\nVolte Sempre...")
                time.sleep(3)
                print("\n"*30)
            else:
                print("\nNúmero Inválido!!\n")