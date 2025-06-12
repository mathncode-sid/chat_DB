import sqlite3
import chainlit as cl
from openai import OpenAI

client = OpenAI()

DB_PATH = "chinook.sqlite"  # Ensure it's in your project folder


def get_schema_and_sample_data(limit=20):
    """Fetch schema and preview rows from all tables."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
    except Exception as e:
        conn.close()
        return f"Error fetching table names: {e}", ""

    schema = ""
    data_preview = ""

    for table in tables:
        try:
            # Get schema
            cursor.execute(f"PRAGMA table_info({table});")
            columns = [col[1] for col in cursor.fetchall()]
            schema += f"\n📄 Table: {table}\nColumns: {columns}\n"

            # Get data
            cursor.execute(f"SELECT * FROM {table} LIMIT {limit};")
            rows = cursor.fetchall()
            data_preview += f"\n📊 Data from {table} (limit {limit}):\n"
            data_preview += " | ".join(columns) + "\n"
            data_preview += "-" * 60 + "\n"
            for row in rows:
                data_preview += " | ".join(str(x) for x in row) + "\n"
        except Exception as e:
            data_preview += f"\n⚠️ Could not fetch data from table '{table}': {e}\n"

    conn.close()
    return schema, data_preview


async def get_ai_response(schema, sample_data, user_question):
    prompt = (
        "You are a helpful AI assistant with access to a music store database.\n\n"
        f"Here is the database schema:\n{schema}\n\n"
        f"And here is a sample of the data:\n{sample_data}\n\n"
        f"Answer the following question based on the above:\n\n"
        f"{user_question}"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.7
    )

    return response.choices[0].message.content


@cl.on_message
async def main(message: cl.Message):
    user_question = message.content.strip()

    if not user_question:
        await cl.Message(content="Please enter a question to ask about the database.").send()
        return

    schema, sample_data = get_schema_and_sample_data(limit=5)
    ai_answer = await get_ai_response(schema, sample_data, user_question)

    await cl.Message(content=ai_answer).send()
