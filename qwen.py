
import ollama
import re

MODEL = "qwen2.5:7b"


def clean_sql(response):
    response = response.strip()

    # Remove Markdown code blocks
    response = re.sub(
        r"^```(?:sql)?\s*",
        "",
        response,
        flags=re.IGNORECASE
    )

    response = re.sub(r"\s*```$", "", response)

    # Remove SQL: prefix
    response = re.sub(
        r"^SQL:\s*",
        "",
        response,
        flags=re.IGNORECASE
    )

    return response.strip()


def generate_sql(question, schema):

    system_prompt = """
    You are an expert PostgreSQL query generator.

    Generate valid PostgreSQL SQL queries.

    STRICT RULES:
    1. Return ONLY raw SQL text.
    2. Never use Markdown or code blocks.
    3. Never include explanations.
    4. Use ONLY tables and columns from the schema.
    5. Never invent column names.
    6. Use correct JOIN conditions.
    7. Use PostgreSQL syntax.
    8. If the question cannot be answered,
       return exactly:
       ERROR: Cannot generate query from provided schema.

    Output ONLY the SQL query.
    """

    user_prompt = f"""
    Database schema:

    {schema}

    User question:

    {question}

    Generate the PostgreSQL query.
    """

    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        options={
            "temperature": 0
        }
    )

    sql = clean_sql(response["message"]["content"])

    return sql
