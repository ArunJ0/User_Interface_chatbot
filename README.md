chatbot

├── _pycache_

├── migrations

│   ├── __init__.py

│   ├── admin.py

│   ├── apps.py

│   ├── models.py

│   ├── tests.py

│   ├── urls.py

│   └── views.py

├── django_chatbot

│   ├── _pycache_

│   ├── __init__.py

│   ├── asgi.py

│   ├── settings.py

│   ├── urls.py

│   ├── wsgi.py

│   └── templates

│       ├── base.html

│       └── chatbot.html

├── db.sqlite3

├── manage.py

└── README.md


1. HTML Templates:
templates/base.html:

    Defines the basic structure of an HTML document with Bootstrap styling.
    Contains several {% block %} tags to allow for content customization in child templates.
    Links Bootstrap CSS and JavaScript.

templates/chatbot.html:

    Extends base.html.
    Overrides the {% block styles %} and {% block content %} to add custom styles and content for the chatbot interface.
    Implements a chat interface with a sidebar, message display area, and a message input form.
    Provides a JavaScript script to handle user messages, send them to the server, and display responses.

2. CSS Styles:

    Custom styles are defined in the {% block styles %} section of chatbot.html. These styles are specific to the chat interface, including sidebar, message display, and input form.

3. JavaScript:

    The JavaScript script in chatbot.html handles user interactions, such as submitting messages and updating the chat interface dynamically.
    Utilizes the Fetch API to send user messages to the server asynchronously.
    Updates the chat interface with user-sent and bot-received messages.

4. Django Application (chatbot):
chatbot/apps.py:

    Configuration for the Django app.

chatbot/urls.py:

    Defines URL patterns for the app.

chatbot/views.py:

    Defines a view function (chatbot) that renders the chatbot interface.
    Handles POST requests to the chatbot, sending user messages to an OpenAI GPT-3.5 Turbo model and returning the bot's response as JSON.

chatbot/settings.py:

    Django settings for the project, including app configuration, middleware, database settings, and static file configurations.

5. ASGI, WSGI, and Project Configuration:

    django_chatbot/asgi.py and django_chatbot/wsgi.py are ASGI and WSGI configurations for the Django project, respectively.
    django_chatbot/settings.py contains project-wide settings, including the database configuration and static file settings.
    django_chatbot/urls.py defines the project-level URL patterns.

6. OpenAI GPT-3.5 Turbo Integration:

    The ask_openai function in chatbot/views.py sends user messages to an OpenAI GPT-3.5 Turbo model using the OpenAI API.

7. Frontend and Backend Integration:

    The frontend (HTML, CSS, and JavaScript) interacts with the Django backend to send and receive messages, updating the chat interface dynamically.

8. Django Administration:

    Django admin is configured in django_chatbot/urls.py.

9. Project-wide Settings:

    Project-wide settings, such as the secret key, debugging mode, and database configuration, are defined in django_chatbot/settings.py.

10. Deployment:

    The project includes configurations for ASGI and WSGI for deployment.

This application allows users to interact with a chatbot, leveraging OpenAI's GPT-3.5 Turbo for natural language understanding and response generation. The Django framework is used to handle server-side logic and serve the web interface.

11. Manage.py

The manage.py script in a Django project is a command-line utility provided by Django for various administrative tasks.

to run the user interface just run the manage.py script with "python manage.py runserver"
