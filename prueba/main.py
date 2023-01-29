import pandas as pd
import psycopg2

class CHARGES:
    def __init__(self,archivo):
        self.df = pd.read_csv(archivo)
        self.conn=psycopg2.connect(
                host="localhost",
                database="prueba",
                user="admin",
                password="admin"
        )
        self.cursor=self.conn.cursor()
    def CreateTables(self):
        self.cursor.execute('''
        DROP TABLE IF EXISTS companies CASCADE;
        DROP TABLE IF EXISTS charges CASCADE;
        
        CREATE TABLE companies(
           company_id varchar(24) NOT NULL,
           company_name VARCHAR(130) NOT NULL,
           PRIMARY KEY(company_id)
        );
        
        CREATE TABLE charges(
           id varchar(24) NOT NULL,
           company_id varchar(24) NOT NULL,
           amount decimal(16,2) NOT NULL,
           status varchar(30) NOT NULL,
           created_at timestamp NOT NULL,
           updated_at timestamp NULL,
           PRIMARY KEY(id),
           CONSTRAINT fk_company
              FOREIGN KEY(company_id) 
              REFERENCES companies(company_id)
        );''')
        self.conn.commit()

    def InsetValues(self):

        #Insertaremos las compañias dentro de la tabla companies
        pivot_table = self.df.pivot_table(index=['db_company_id', 'name'], aggfunc='size')
        data = [company[0] for company in pivot_table.items()]
        #print(data)
        self.cursor.executemany("INSERT INTO companies(company_id, company_name) VALUES (%s, %s)", data)
        self.conn.commit()


        #Insertamos las transacciones dentro de la tabla charges
        transactions=self.df[['db_id','db_company_id','amount','status','created_at','paid_at']]
        self.cursor.executemany("INSERT INTO charges(id, company_id, amount, status, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)",  transactions.to_records(index=False))
        self.conn.commit()

    def VIEW(self):
        self.cursor.execute('''
        SELECT 
	        companies.company_id,
            companies.company_name, 
            date(created_at) as date, 
            sum(amount) as total_amount_per_day
        FROM 
            charges
        LEFT JOIN 
            companies 
        ON 
            charges.company_id = companies.company_id
        GROUP BY 
            companies.company_id, date
        ORDER BY 
            date
        ''')
        resultado=self.cursor.fetchall()
        print(resultado)

if __name__ == "__main__":
    prueba=CHARGES('NewData.csv')
    prueba.CreateTables()
    prueba.InsetValues()
    prueba.VIEW()
    #prueba.show()