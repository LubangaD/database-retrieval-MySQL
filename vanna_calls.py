import streamlit as st
from vanna.remote import VannaDefault


@st.cache_resource(ttl=3600)
def setup_vanna():
    vn = VannaDefault(api_key=st.secrets.get("VANNA_API_KEY"), model='retriever')
    vn.connect_to_sqlite("Akinsurance.db")
    return vn


# @st.cache_resource(ttl=3600)
# def train_vanna_with_schema():
#     vn = setup_vanna()
#     if vn:
#         try:
#             # Fetch the schema information
#             schema_query = """
#             SELECT table_name, column_name, data_type
#             FROM information_schema.columns
#             WHERE table_schema = 'public'
#             """
#             schema_df = vn.run_sql(schema_query)
            
#             # Generate DDL statements
#             ddl_statements = []
#             for table_name in schema_df['table_name'].unique():
#                 columns = schema_df[schema_df['table_name'] == table_name]
#                 ddl = f"CREATE TABLE {table_name} (\n"
#                 ddl += ",\n".join([f"    {row['column_name']} {row['data_type']}" for _, row in columns.iterrows()])
#                 ddl += "\n);"
#                 ddl_statements.append(ddl)
            
#             # Train Vanna with the DDL statements
#             vn.train("\n\n".join(ddl_statements))
#             return True
#         except Exception as e:
#             st.error(f"Failed to train Vanna with schema: {str(e)}")
#             return False
#     return False
# @st.cache_resource(ttl=3600)
# def setup_vanna():
#     """
#     Sets up the Vanna connection using the API key stored in Streamlit secrets.
#     Attempts to connect to a PostgreSQL database using the provided credentials.
#     """
#     try:
#         vn = VannaDefault(api_key=st.secrets.get("VANNA_API_KEY"), model='retriever')
#         vn.connect_to_postgres(
#             host="aws-0-us-east-1.pooler.supabase.com",
#             dbname="database",
#             user="postgres.vgxpxmrxmevhnknrkrej", 
#             password="Peakyblinders@123",
#             port="6543",
#         )
#         return vn
#     except Exception as e:
#         st.error(f"Failed to connect to PostgreSQL: {str(e)}")
#         return None

# @st.cache_resource(ttl=3600)
# def setup_vanna():
#     try:
#         vn = VannaDefault(api_key=st.secrets.get("VANNA_API_KEY"), model='retriever')
#         vn.connect_to_postgres(
#             host="aws-0-us-east-1.pooler.supabase.com",
#             dbname="postgres",
#             user="postgres.vgxpxmrxmevhnknrkrej", 
#             password="Peakyblinders@123",
#             port="6543",
#         )
#         if train_vanna_with_schema():
#             st.success("Vanna trained successfully with database schema.")
#         else:
#             st.warning("Failed to train Vanna with database schema. Some features may not work correctly.")
#         return vn
#     except Exception as e:
#         st.error(f"Failed to connect to PostgreSQL: {str(e)}")
#         return None

@st.cache_data(show_spinner="Generating sample questions ...")
def generate_questions_cached():
    vn = setup_vanna()
    if vn is None:
        st.error("Failed to set up Vanna. Cannot generate questions.")
        return []
    try:
        questions = vn.generate_questions()
        if not questions:
            st.warning("No questions were generated. The model might need more training data.")
        return questions
    except Exception as e:
        st.error(f"Error generating questions: {str(e)}")
        return []

# Rest of the code remains the same


@st.cache_data(show_spinner="Generating SQL query ...")
def generate_sql_cached(question: str):
    vn = setup_vanna()
    return vn.generate_sql(question=question, allow_llm_to_see_data=True)

@st.cache_data(show_spinner="Checking for valid SQL ...")
def is_sql_valid_cached(sql: str):
    vn = setup_vanna()
    return vn.is_sql_valid(sql=sql)

@st.cache_data(show_spinner="Running SQL query ...")
def run_sql_cached(sql: str):
    vn = setup_vanna()
    return vn.run_sql(sql=sql)

@st.cache_data(show_spinner="Checking if we should generate a chart ...")
def should_generate_chart_cached(question, sql, df):
    vn = setup_vanna()
    return vn.should_generate_chart(df=df)

@st.cache_data(show_spinner="Generating Plotly code ...")
def generate_plotly_code_cached(question, sql, df):
    vn = setup_vanna()
    code = vn.generate_plotly_code(question=question, sql=sql, df=df)
    return code


@st.cache_data(show_spinner="Running Plotly code ...")
def generate_plot_cached(code, df):
    vn = setup_vanna()
    return vn.get_plotly_figure(plotly_code=code, df=df)


@st.cache_data(show_spinner="Generating followup questions ...")
def generate_followup_cached(question, sql, df):
    vn = setup_vanna()
    return vn.generate_followup_questions(question=question, sql=sql, df=df)

@st.cache_data(show_spinner="Generating summary ...")
def generate_summary_cached(question, df):
    vn = setup_vanna()    
    return vn.generate_summary(question=question, df=df)

