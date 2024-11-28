def obter_arquivo_escolhido():
    print("Escolha um dos arquivos abaixo para executar o problema de transporte:")
    print("1. Excesso de Demanda (Desbalanceado)")
    print("2. Excesso de Oferta (Desbalanceado)")
    print("3. Balanceado - 3 Pontos de Oferta e 2 Pontos de Demanda")
    print("4. Balanceado - 10 Pontos de Oferta e 10 Pontos de Demanda")

    opcao = input("Digite o número correspondente à sua escolha: ")
    
    arquivos = {
        "1": "testes/excesso_demanda.txt",
        "2": "testes/excesso_oferta.txt",
        "3": "testes/balanceado3ofetas2demandas.txt",
        "4": "testes/balanceado10ofertas10demandas.txt"
    }

    return arquivos.get(opcao, None)