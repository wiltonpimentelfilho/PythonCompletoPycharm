import psycopg2

User = "postgres"
Pass = "19Genius63"
Host = "150.162.96.3"
Port = "5432"
Database = "SeadDB"


def search():
    connection = psycopg2.connect(user=User, password=Pass, host=Host, port=Port, database=Database)

    cursor = connection.cursor()
    print(f"Connected to PostgreSQL on {Host}:{Port} as {User}")
    print("Busque por um nome:")

    Tipo = input("Nome ou CPF? (Nome/Cpf): ").lower()
    InputName = input(f"{Tipo}:").lower()

    cursor.execute(
        f"SELECT * FROM concluintes WHERE unaccent({Tipo}) ilike unaccent(\'{InputName}%\') order by nome asc")
    record = cursor.fetchall()
    cursor.close()

    if (len(record) == 0):
        print("Nenhum registro encontrado")
        return

    if (len(record) > 100):
        print(f"{len(record)} registros encontrados para {InputName}")
        I = input("Deseja mostrar todos os registros? (S/N)").lower()

        if (I == "s"):
            for Entry in record:
                print(f"Nome: {Entry[1]} | CPF: {Entry[5]} | Email: {Entry[2]} | Cidade: {Entry[3]} | UF: {Entry[4]}")
        else:
            return
        return

    print(f"{len(record)} registros encontrados para {InputName}")
    for Entry in record:
        print(f"Nome: {Entry[1]} | CPF: {Entry[5]} | Email: {Entry[2]} | Cidade: {Entry[3]} | UF: {Entry[4]}")


search()
