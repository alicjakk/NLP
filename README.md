Local LLM to SQL -- Northwind
- PostgreSQL with the Northwind database imported.
- pgAdmin (for viewing and managing the database).
- Python.
- Ollama with a local model installed (for example, qwen2.5:7b).
Project files
Keep these files in the same project folder:
- generator.py -- Streamlit user interface.
- database.py -- PostgreSQL connection, schema reading, and query
  execution.
- qwen.py -- sends the question and database schema to Ollama and
  receives SQL.
  
Setup
1. Make sure PostgreSQL is running and the Northwind tables are
   imported.
2. Install the Python dependencies:
   python -m pip install sqlalchemy psycopg2-binary ollama streamlit
3. In database.py, set DATABASE_URL to match your local PostgreSQL
   username, password, port, and database name. The database in this
   project is named nortwind (misspelled), so use nortwind in the
   connection URL unless you rename the database.
   Example:
   DATABASE_URL = "postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/nortwind"
4. Make sure Ollama is running and the model named in qwen.py is
   installed. Check installed models with:
   ollama list
5. Set MODEL in qwen.py to the exact model name shown by
   ollama list.
Run the app
From the project folder, run:
streamlit run generator.py
Streamlit will show a local web address in the terminal. Open that
address in your browser.
Expected workflow
1. Enter a question about the Northwind data.
2. The local LLM generates a PostgreSQL query using the database
   schema.
3. The app displays the generated SQL.
4. The app executes the query and displays the returned rows.
Important
The LLM can generate SQL with incorrect table names, columns, or joins.
If a query fails, check the actual schema in PostgreSQL and compare it
with the generated SQL. The database name nortwind is intentional in
the current configuration; it does not need to be changed for the app to
connect.
