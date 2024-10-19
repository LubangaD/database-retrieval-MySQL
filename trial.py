import vanna
from vanna.remote import VannaDefault

api_key = "a4f5a012937a468f97d4fdfa012c88aa"

vanna_model_name = "retriever"
vn = VannaDefault(model=vanna_model_name, api_key=api_key)

vn.connect_to_postgres(host='aws-0-us-east-1.pooler.supabase.com', dbname='postgres', user='postgres.dkfngbylkswqccbjpmgf', password='Expendables@12', port='6543')
from vanna.flask import VannaFlaskApp
app = VannaFlaskApp(vn)
app.run()