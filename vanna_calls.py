import streamlit as st
from vanna.remote import VannaDefault

# @st.cache_resource(ttl=3600)
# def setup_vanna():
#     vn = VannaDefault(api_key=st.secrets.get("VANNA_API_KEY"), model='retriever')
#     vn.connect_to_sqlite("vanna-streamlit/insurance.db")
#     return vn

# @st.cache_resource(ttl=3600)
# def setup_vanna():
#     # vn = VannaDefault(config={"model": "zephyr"})
#     vn = VannaDefault(api_key=st.secrets.get("VANNA_API_KEY"), model='zephyr')
#     vn.connect_to_postgres(
#         host="aws-0-us-east-1.pooler.supabase.com",
#         dbname="postgres",
#         user="postgres.dkfngbylkswqccbjpmgf",
#         password="V4asKTHIkLU2EllE",
#         port="6543",
#     )
#     return vn


@st.cache_resource(ttl=3600)
def setup_vanna():
    """
    Sets up the Vanna connection using the API key stored in Streamlit secrets.
    Attempts to connect to a PostgreSQL database using the provided credentials.
    """
    try:
        vn = VannaDefault(api_key=st.secrets.get("VANNA_API_KEY"), model='retriever')
        vn.connect_to_postgres(
            host="aws-0-us-east-1.pooler.supabase.com",
            dbname="postgres",
            user="postgres.vgxpxmrxmevhnknrkrej", 
            password="Peakyblinders@123",
            port="6543",
        )
        return vn
    except Exception as e:
        st.error(f"Failed to connect to PostgreSQL: {str(e)}")
        return None

@st.cache_data(show_spinner="Generating sample questions ...")
def generate_questions_cached():
    vn = setup_vanna()
    return vn.generate_questions()


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

# import streamlit as st
# from vanna.remote import VannaDefault

# @st.cache_resource(ttl=3600)
# def setup_vanna():
#     """
#     Sets up the Vanna connection using the API key stored in Streamlit secrets.
#     Attempts to connect to a PostgreSQL database using the provided credentials.
#     """
#     try:
#         st.write("Attempting to set up Vanna connection...")
        
#         # Debug the API key and credentials being used
#         api_key = st.secrets.get("VANNA_API_KEY")
#         st.write(f"VANNA_API_KEY: {api_key}")
        
#         # Set up Vanna connection
#         vn = VannaDefault(api_key=api_key, model='retriever')
        
#         # Log the connection details
#         st.write("Attempting to connect to PostgreSQL...")
#         st.write("Host: aws-0-us-east-1.pooler.supabase.com")
#         st.write("DB Name: postgres")
#         st.write("User: postgres.dkfngbylkswqccbjpmgf")
#         st.write("Port: 6543")
        
#         # Connect to PostgreSQL
#         vn.connect_to_postgres(
#             host="aws-0-us-east-1.pooler.supabase.com",
#             dbname="postgres",
#             user="postgres.dkfngbylkswqccbjpmgf",
#             password="Peakyblinders@123",  # You can replace this temporarily to check if secrets are incorrect
#             port="6543",
#         )
        
#         st.write("Vanna setup complete!")
#         return vn

#     except Exception as e:
#         st.error(f"Failed to connect to PostgreSQL or Vanna: {str(e)}")
#         return None


# @st.cache_data(show_spinner="Generating sample questions ...")
# def generate_questions_cached():
#     vn = setup_vanna()
#     if vn is None:
#         st.error("Vanna setup failed. Cannot generate questions.")
#         return None
#     try:
#         return vn.generate_questions()
#     except Exception as e:
#         st.error(f"Error generating questions: {str(e)}")
#         return None

# @st.cache_data(show_spinner="Generating SQL query ...")
# def generate_sql_cached(question: str):
#     vn = setup_vanna()
#     if vn is None:
#         st.error("Vanna setup failed. Cannot generate SQL.")
#         return None
#     try:
#         return vn.generate_sql(question=question, allow_llm_to_see_data=True)
#     except Exception as e:
#         st.error(f"Error generating SQL: {str(e)}")
#         return None

# @st.cache_data(show_spinner="Checking for valid SQL ...")
# def is_sql_valid_cached(sql: str):
#     vn = setup_vanna()
#     if vn is None:
#         st.error("Vanna setup failed. Cannot validate SQL.")
#         return None
#     try:
#         return vn.is_sql_valid(sql=sql)
#     except Exception as e:
#         st.error(f"Error validating SQL: {str(e)}")
#         return None

# @st.cache_data(show_spinner="Running SQL query ...")
# def run_sql_cached(sql: str):
#     vn = setup_vanna()
#     if vn is None:
#         st.error("Vanna setup failed. Cannot run SQL.")
#         return None
#     try:
#         return vn.run_sql(sql=sql)
#     except Exception as e:
#         st.error(f"Error running SQL: {str(e)}")
#         return None

# @st.cache_data(show_spinner="Checking if we should generate a chart ...")
# def should_generate_chart_cached(question, sql, df):
#     vn = setup_vanna()
#     if vn is None:
#         st.error("Vanna setup failed. Cannot check for chart generation.")
#         return None
#     try:
#         return vn.should_generate_chart(df=df)
#     except Exception as e:
#         st.error(f"Error checking chart generation: {str(e)}")
#         return None

# @st.cache_data(show_spinner="Generating Plotly code ...")
# def generate_plotly_code_cached(question, sql, df):
#     vn = setup_vanna()
#     if vn is None:
#         st.error("Vanna setup failed. Cannot generate Plotly code.")
#         return None
#     try:
#         return vn.generate_plotly_code(question=question, sql=sql, df=df)
#     except Exception as e:
#         st.error(f"Error generating Plotly code: {str(e)}")
#         return None

# @st.cache_data(show_spinner="Running Plotly code ...")
# def generate_plot_cached(code, df):
#     vn = setup_vanna()
#     if vn is None:
#         st.error("Vanna setup failed. Cannot generate plot.")
#         return None
#     try:
#         return vn.get_plotly_figure(plotly_code=code, df=df)
#     except Exception as e:
#         st.error(f"Error generating plot: {str(e)}")
#         return None

# @st.cache_data(show_spinner="Generating followup questions ...")
# def generate_followup_cached(question, sql, df):
#     vn = setup_vanna()
#     if vn is None:
#         st.error("Vanna setup failed. Cannot generate follow-up questions.")
#         return None
#     try:
#         return vn.generate_followup_questions(question=question, sql=sql, df=df)
#     except Exception as e:
#         st.error(f"Error generating follow-up questions: {str(e)}")
#         return None

# @st.cache_data(show_spinner="Generating summary ...")
# def generate_summary_cached(question, df):
#     vn = setup_vanna()
#     if vn is None:
#         st.error("Vanna setup failed. Cannot generate summary.")
#         return None
#     try:
#         return vn.generate_summary(question=question, df=df)
#     except Exception as e:
#         st.error(f"Error generating summary: {str(e)}")
#         return None