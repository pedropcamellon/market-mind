# MarketMind

MarketMind is a small demo Django-based web application that integrates with a language model agent to handle search queries about companies. The application provides the latest news and stock prices for a given company using tools and services.

## Table of Contents

- [MarketMind](#marketmind)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
    - [Screenshot](#screenshot)
  - [Tech Stack](#tech-stack)
  - [Project Structure](#project-structure)
  - [Setup](#setup)
  - [Usage](#usage)
  - [Best Practices](#best-practices)
    - [Code Organization](#code-organization)
    - [Environment Management](#environment-management)
    - [Logging](#logging)
    - [Dependency Management](#dependency-management)
    - [Security](#security)
    - [Documentation](#documentation)
    - [Version Control](#version-control)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- Search for the latest news and stock prices of companies.
- Integration with Google Search for fetching news.
- Utilizes language models for generating responses.

### Screenshot

![MarketMind Screenshot](home_screenshot.png)

## Tech Stack

- **Backend Framework**: Django
- **Language Model**: LangChain with Google Vertex AI
- **Database**: SQLite (for development)
- **Templating Engine**: Django Templates
- **Environment Management**: Python `dotenv`
- **Search Integration**: Google Search API

## Project Structure

```plaintext
market-mind/
├── .env
├── .gitignore
├── .vault/
│   └── application_default_credentials.json
├── db.sqlite3
├── manage.py
├── requirements.txt
└── src/
    ├── __init__.py
    ├── agent_tools/
    │   ├── company_info_tool.py
    │   └── stock_price_tool.py
    ├── asgi.py
    ├── services/
    │   ├── agent.py
    │   └── google_search.py
    ├── settings.py
    ├── templates/
    │   ├── base.html
    │   └── search.html
    ├── urls.py
    ├── views.py
    └── wsgi.py
```

## Setup

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/market-mind.git
    cd market-mind
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Rename the example environment file `.env.example` to `.env` in the root directory and add the necessary environment variables:

    ```env
    GCP_PROJECT_ID=your-google-cloud-project-id
    GCP_PROJECT_LOCATION=your-google-cloud-project-location
    ```

5. **Start the development server**:

    ```sh
    python manage.py runserver
    ```

## Usage

- Open your web browser and navigate to `http://127.0.0.1:8000/`.
- Enter the name of the company you are interested in and click "Search".
- The application will display the latest news and stock price for the company.

## Best Practices

### Code Organization

- **Modular Structure**: The project is organized into different directories for tools, services, and templates. This helps in maintaining a clean and modular codebase.
- **Separation of Concerns**: The agent-related logic is encapsulated in a dedicated service and its tools are defined in the `agent_tools` directory.

### Environment Management

- **Environment Variables**: Sensitive information and configuration settings are managed using environment variables. The  file is used to store these variables securely.

### Logging

- **Logging**: The application uses Python's built-in  module to log important events and errors. This helps in debugging and monitoring the application.

### Dependency Management

- **Requirements File**: All dependencies are listed in the  file. This ensures that the application can be set up consistently across different environments.

### Security

- **Secret Key**: The Django secret key is stored securely and should not be exposed in the codebase.
- **CSRF Protection**: Django's built-in CSRF protection is used to secure forms.

### Documentation

- **Docstrings**: Functions and classes are documented using docstrings to provide clear explanations of their purpose and usage.

### Version Control

- **.gitignore**: The  file is used to exclude unnecessary files and directories from version control, including sensitive files that should not be stored in Git.

## Contributing

This is a small demo project. Suggestions are welcomed, but I'm not accepting pull requests. Feel free to fork and use it as a head start.

## License

This project is licensed under the MIT License.
