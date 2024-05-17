import streamlit as st

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        st.write(" | ".join(linha))
        st.write("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador = "X"
    st.write("Jogo da Velha")
    while True:
        imprimir_tabuleiro(tabuleiro)
        linha = st.number_input(f"Jogador {jogador}, escolha uma linha (0, 1 ou 2):", min_value=0, max_value=2, step=1)
        coluna = st.number_input(f"Jogador {jogador}, escolha uma coluna (0, 1 ou 2):", min_value=0, max_value=2, step=1)
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
            if verificar_vitoria(tabuleiro, jogador):
                imprimir_tabuleiro(tabuleiro)
                st.write(f"Parabéns! Jogador {jogador} venceu!")
                break
            elif all(all(celula != " " for celula in linha) for linha in tabuleiro):
                imprimir_tabuleiro(tabuleiro)
                st.write("Empate!")
                break
            jogador = "O" if jogador == "X" else "X"
        else:
            st.write("Essa posição já está ocupada. Escolha outra.")

if __name__ == "__main__":
    jogo_da_velha()
