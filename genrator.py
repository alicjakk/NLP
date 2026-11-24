
import streamlit as st

from database import get_database_schema, execute_sql
from qwen import generate_sql

st.set_page_config(
    page_title="Northwind AI",
    layout="wide"
)

st.title("Northwind Database AI Assistant")
# st.caption("Ask questions about your database using natural language.")

@st.cache_resource
def load_schema():
    return get_database_schema()

try:
    schema = load_schema()
    # st.success("Connected to Northwind database")
except Exception as e:
    st.error(f"Database connection error: {e}")
    st.stop()

question = st.text_input(
    "Ask a question:",
    placeholder="Example: Show me the 10 most expensive products..."
)

if st.button("Generate SQL and Execute", type="primary"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        try:
            with st.spinner("Generating SQL with local LLM..."):

                sql = generate_sql(question, schema)

            st.subheader("Generated SQL")

            st.code(sql, language="sql")

            with st.spinner("Executing SQL query..."):

                columns, rows = execute_sql(sql)

            st.subheader("Query Results")

            if rows:
                st.dataframe(
                    [dict(zip(columns, row)) for row in rows],
                    use_container_width=True
                )

                st.success(f"Returned {len(rows)} rows.")

            else:
                st.info("The query returned no results.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

# with st.expander("View database schema"):
#     st.code(schema)
