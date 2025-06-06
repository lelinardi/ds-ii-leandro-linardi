import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        database="etecDB",
        user="root",
        password="",  # Coloque a senha correta do root aqui
        port=3306,
        auth_plugin='mysql_native_password'  # Use isso APENAS se não puder alterar a autenticação no MySQL
    )
    cursor = conexao.cursor()

    # ... resto do seu código ...


    while True:
        print("\n=== Novo Cadastro de Usuário ===") # LL
        nome = input("Digite o Nome: ")
        sobrenome = input("Digite o Sobrenome: ")
        while True:
            idade_input = input("Digite a Idade: ")
            if idade_input.isdigit():
                idade = int(idade_input)
                break
            else:
                print("Por favor, digite somente números inteiros")
        while True:
            sexo = input("Digite o Sexo (M/F): ").upper()
            if sexo in ("M", "F"):
                break
            else:
                print('Por favor, digite "M" ou "F", somente')

        # Inserção
        try:
            cursor.execute("INSERT INTO Log (Name, Lastname, Age, Gender) VALUES (%s, %s, %s, %s)", (nome, sobrenome, idade, sexo))
            conexao.commit()
            print("Dados inseridos com sucesso!")

        except mysql.connector.Error as e: # Correção: mysql.connector.Error
            print(f"Erro ao inserir dados: {e}")
            conexao.rollback()

        continuar = input("Deseja continuar? (s/n) ")
        if continuar.lower() == "n":
            break

    # Consulta (após o loop de inserção)
    cursor.execute("SELECT * FROM Log") # Nome da tabela corrigido
    registros = cursor.fetchall()

    for row in registros:
        print("IDName = ", row[0]) # Índices corrigidos
        print("Name = ", row[1])
        print("Lastname = ", row[2])
        print("Age = ", row[3])
        print("Gender  = ", row[4], "\n")

except mysql.connector.Error as e: # Correção: mysql.connector.Error
    print(f"Erro de conexão/operação com o banco de dados: {e}")

finally:
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()


