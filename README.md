An app template for large Flask applications with Flask-SQLAlchemy integration. The application has the following structure:

## Add secret

- DATABASE_URI=postgresql://postgres:postgres@db/postgres

## Install dependencies

### codespace

already installed

### others

```pip install -r requirements.txt```

## run

```flask run --debug```

```
.
├── app
│   ├── extensions.py
│   ├── __init__.py
│   ├── models
│   │   ├── post.py
│   │   └── question.py
│   ├── posts
│   │   ├── __init__.py
│   │   └── routes.py
│   └── questions
│   │   ├── __init__.py
│   │   └── routes.py
├── config.py
```
