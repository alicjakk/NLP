from sqlalchemy import create_engine, text, inspect

DATABASE_URL = (
    "postgresql+psycopg2://postgres:77ccb8d93484437a97b105c71c4f07d4"
    "@localhost:5432/nortwind"
)

engine = create_engine(DATABASE_URL)

def get_database_schema():
    inspector = inspect(engine)
    schema = []

    for table in inspector.get_table_names(schema="public"):
        columns = inspector.get_columns(table, schema="public")

        schema.append(f"\nTable: {table}")

        for column in columns:
            schema.append(
                f"  {column['name']} ({column['type']})"
            )

    return "\n".join(schema)


def execute_sql(sql):
    with engine.connect() as connection:
        result = connection.execute(text(sql))

        columns = result.keys()
        rows = result.fetchall()

        return columns, rows