import oracledb

def insert_carro(dado):
    try:
        with oracledb.connect(
            user='pf0313', 
            password='professor#23',
            dsn='oracle.fiap.com.br/orcl') as con:

            with con.cursor() as cur:
                sql = '''insert into carro values(:id, :ano, 
                               :montadora, :modelo, :placa)'''
                cur.execute(sql, dado)
            
            con.commit()
    except Exception as erro:
        print("deu erro!")
        raise erro


#c = {"id": 1, "ano": 2020, "montadora": "Fiat", "modelo": "mobi",
#        "placa": "GRT-5722"}
#insert_carro(c)