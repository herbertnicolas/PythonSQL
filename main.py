import mysql.connector

BancoDeAlunos = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cdd12345",
    database="tabela"
)

cursor = BancoDeAlunos.cursor()
pesquisa = 'select * from alunos;'
cursor.execute(pesquisa)

resultado = cursor.fetchall()

for x in resultado:
    print(x)

while True:
    op = input("Digite a opção desejada. \n\n1 = INSERIR NOVO ITEM \n2 = BUSCAR ITEM \n3 = SAIR")

    if(op == "1"):
        nome1 = input("Digite o nome a ser inserido")
        telefone1 = input("Digite o telefone para contato")
        cursor = BancoDeAlunos.cursor()
        sql = 'insert into alunos (nome,telefone) values (%s,%s)'
        data = (nome1, telefone1)
        cursor.execute(sql, data)
        BancoDeAlunos.commit()
        cursor.close()
        BancoDeAlunos.close()

    elif (op == "2"):
        cursor = BancoDeAlunos.cursor()
        sql = 'select * from alunos'
        cursor.execute(sql)
        resultado = cursor.fetchall()

        for x in resultado:
            print(x[0],x[1],x[2]) #printando uma determinada linha da tabela

    else:
        print("Aplicação encerrada.")
        break;



