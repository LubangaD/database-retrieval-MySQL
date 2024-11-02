


# AI Streamlit App for Database Information Retrieval
<img width="1392" alt="gif image of demo" src="./assets/demo.gif">

## Application Capabilities

This AI-powered Streamlit app enables users to interact with and analyze SQL-based insurance data through natural language queries. Key functionalities include:

- **Data Querying**: Users can input questions, and the app generates SQL queries to retrieve relevant data from the database.
- **Table and Chart Display**: Results can be displayed as tables or visualized with dynamic Plotly charts for enhanced understanding of trends and insights.
- **Automated Summaries**: The app provides concise summaries based on the data retrieved, allowing for quick insights without needing to analyze large datasets manually.
- **Suggested Follow-up Questions**: After each query, the app suggests relevant follow-up questions to deepen data exploration.
- **SQL and Code Transparency**: Users can view the SQL queries and Plotly code generated, ensuring transparency and flexibility in data analysis.

The application is tailored for insurance data but can be adapted for other SQL databases, making it versatile for various analytics needs.

## Install

```bash
git clone https://github.com/LubangaD/database-retrieval-MySQL.git
cd vanna-streamlit
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

Here’s the revised text with each instruction on a new line:

---

## Configure

- Modify the `setup_vanna` function in [vanna_calls.py](./vanna_calls.py) to use your desired Vanna setup.
- Create a Vanna account and set up a model, obtaining its API key. Alternatively, you can train the model with your database structure using DDL statements, SQL statements, and database documentation.
- Configure secrets in `.streamlit/secrets.toml` and access them in your app using `st.secrets.get(...)`.

---


## Run

```bash
streamlit run app.py
```


