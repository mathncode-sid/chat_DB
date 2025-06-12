# ChatDB: AI-Powered SQLite Database Q&A

ChatDB is a Python application that lets you ask natural language questions about a SQLite music store database. It uses OpenAI's GPT-4o model to interpret your questions and provide answers based on the database schema and sample data.

## Features

- Connects to a local SQLite database (`chinook.sqlite`)
- Automatically fetches schema and sample data from all tables
- Uses OpenAI GPT-4o for natural language Q&A
- Interactive chat interface powered by [Chainlit](https://github.com/Chainlit/chainlit)

## Requirements

- Python 3.8+
- [Chainlit](https://github.com/Chainlit/chainlit)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- `chinook.sqlite` database file in the project folder

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mathncode-sid/chat_DB.git
   cd chat_DB
   ```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Place your chinook.sqlite file in the project directory.

4. Set your OpenAI API key as an environment variable:
```
export OPENAI_API_KEY=your-api-key
```

## Usage
1. Start the Chainlit app:
```
chainlit run app.py
```
2. Open the provided URL in your browser and start asking questions about the database, such as:
"List the top 5 artists by album count."
"What genres are available in the store?"
The AI is tailored to only answer questions from the Database

## Project Structure
app.py — Main application logic
chinook.sqlite — SQLite database file
requirements.txt — Python dependencies
