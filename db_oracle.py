import oracledb

def insert_carro(dado):
    try:
        with oracledb.connect(
            user='rm552579', 
            password='fiap23',
            dsn='oracle.fiap.com.br/orcl') as con:

            with con.cursor() as cur:
                sql = '''insert into carro values(:id, :ano, 
                               :montadora, :modelo, :placa)'''
                cur.execute(sql, dado)
            
            con.commit()
    except Exception as erro:
        print("deu erro!")
        raise erro
    
def consulta_todos():
    try:
        with oracledb.connect(
            user="rm552579",
            password="fiap23",
            dsn = 'oracle.fiap.com.br/orcl') as con:
        
            with con.cursor() as cur:
                sql = '''select * from carro'''
                cur.execute(sql)
                return cur.fetchall()
    except Exception as erro:
        print('falha na consulta')
        raise erro


#c = {"id": 1, "ano": 2020, "montadora": "Fiat", "modelo": "mobi",
#        "placa": "GRT-5722"}
#insert_carro(c)