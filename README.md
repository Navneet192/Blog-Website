<<<<<<< HEAD
# Blog-Website
=======
# Django Blog Project

A feature-rich blog application built with Django.

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv env
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

3. Install all dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Visit http://127.0.0.1:8000/ in your web browser

## Features

- User authentication with django-allauth
- Rich text editing with CKEditor
- Image handling with django-imagekit
- Tagging system with django-taggit
- Hit counting for posts
- REST API support
- Bootstrap 5 styling
- Crispy forms for form rendering

## Project Structure

The project uses the following main Django apps:
- blog: Main blog functionality
- allauth: User authentication
- imagekit: Image processing
- taggit: Tagging system
- hitcount: View counting
- rest_framework: API functionality

## Dependencies

All project dependencies are listed in `requirements.txt`. The main packages include:
- Django
- django-allauth
- django-imagekit
- django-taggit
- django-ckeditor
- django-crispy-forms
- django-hitcount
- djangorestframework
- and more...

To update dependencies in the future, run:
```bash
pip freeze > requirements.txt
``` 
>>>>>>> 8c2b69a (initial)
