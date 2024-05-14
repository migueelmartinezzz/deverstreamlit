import random

def adivinhacao():
    st.write("Bem-vindo ao jogo de adivinhação!")
    st.write("Pense em um número de 1 a 100 e eu vou tentar adivinhá-lo.")
    
    limite_inferior = 1
    limite_superior = 100
    tentativas = 0
    
    while True:
        palpite = random.randint(limite_inferior, limite_superior)
        st.write(f"Meu palpite é: {palpite}")
        resposta = st.text_input("É maior, menor ou igual ao seu número? (maior/menor/igual): ").lower()
        
        if resposta == "maior":
            limite_inferior = palpite + 1
        elif resposta == "menor":
            limite_superior = palpite - 1
        elif resposta == "igual":
            print(f"Eu sabia! Seu número é {palpite}.")
            break
        else:
            st.write("Por favor, responda 'maior', 'menor' ou 'igual'.")
        
        tentativas += 1
    
    st.write(f"Levei {tentativas} tentativas para adivinhar o seu número.")
  
