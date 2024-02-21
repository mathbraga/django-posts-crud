# Simple CRUD with Django

This is just a simple CRUD using Django.

Live deployment (first load might take a few seconds): https://matheusbraga59.pythonanywhere.com/careers/

To run locally run the following commands in the `root` directory:
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py makemigrations careers
python manage.py migrate
python manage.py runserver
```

## API usage

### List all posts
`GET` - /careers/

Request body:
```
{}
```

### Create new post
`POST` - /careers/

Request body:
```json
{
    "username": "string",
    "title": "string",
    "content": "string"
}
```

### Update a post
`PATCH` - /careers/{post_id}/

Only `title` and `content` can be updated.

Request body:
```json
{
    "title": "string",
    "content": "string"
}
```

### Delete a post
`DELETE` - /careers/{post_id}/

Request body:
```json
{}
```
