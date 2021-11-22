from classe import Empregado

# Instanciando o objeto da classe importada

vini = Empregado("Vinicius", "Mendes", "118922")


if __name__ == "__main__":

    # Checando __repr__:
    vini

    # Checando __str__:
    print(vini)


    # Checando método bate_ponto() input 1 (entrar 1 quando pedido a entrada)
    vini.bate_ponto()
    print("Log de entrada: ", vini.horario_entrada)
    print("Empregado está no trabalho? ", vini.no_trabalho)

    # Checando método bate_ponto() input 2 (entrar 2 quando pedido a entrada)
    vini.bate_ponto()
    print("Log de saída (almoço): ", vini.almoco_start)
    print("Empregado está no trabalho? ", vini.no_trabalho)

    # Checando método bate_ponto() input 3 (entrar 3 quando pedido a entrada)
    vini.bate_ponto()
    print("Log de retorno (almoço) - O empregado cumpriu o\
        horário corretamente?", vini.almoco_end)
    print("Empregado está no trabalho? ", vini.no_trabalho)

    # Checando método bate_ponto() input 4 (entrar 4 quando pedido a entrada)
    vini.bate_ponto()
    print(vini.horario_saida)
    print("Empregado está no trabalho? ", vini.no_trabalho)