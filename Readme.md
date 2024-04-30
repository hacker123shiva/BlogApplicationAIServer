# Flask Server Setup for AI

This project provides a Flask server setup for hosting AI models and generating blog content.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/hacker123shiva/BlogApplicationAIServer.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd BlogApplicationAIServer
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Setting Up Environment Variables

1. **Create a .env file:**

   Create a file named `.env` in the project root directory.

2. **Add the following environment variables to .env:**

   - **OPEN_AI_KEY**: Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys).
   - **API_KEY**: Get your API key from [Gemini](https://aistudio.google.com/app/apikey).

## Server Configuration

1. **Open open.py:**

   Edit the `opean.py` file to set up OpenAI.

2. **Edit app.py:**

   Configure the routes and start the application.

3. **Start the Flask server:**

   Run the following command to start the server:

   ```bash
   python app.py
   ```

## Usage

The server provides the following routes:

1. **/filterblog**: Provides a prompt for filtering vulgar content.
2. **/generate**: Provides a prompt to generate a blog article.
3. **/analyze**: Shows the result of both filtering and generating content, depending on the condition.

```markdown

```
