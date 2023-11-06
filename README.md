# Gallery
if you want to use django version, stay on branch "master"<br>
To use html+js version, switch to branch "gallery-js"

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [After installation](#post_install)
## About <a name = "about"></a>

Site with paintings

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Before starting project

Clone repo
```
git clone https://github.com/darkimpulsepoint/gallery
```

```
cd gallery
```

Now need to install virtualenv to install dependencies
```
pip install virtualenv 
```

create virtual environment
```
virtualenv venv
```
or you can choose another name for your env directory
### Installing

Activate virtual env

Linux / OS X
```
source venv/bin/activate
```

Windows
```
venv\Scripts\activate
```

Now we need to install necessary dependencies

```
pip install -r requirements.txt
```

create migrations
```
python manage.py makemigrations 
```

apply migrations
```
python manage.py migrate
```


End with an example of getting some data out of the system or using it for a little demo.

## Usage <a name = "usage"></a>

Create superuser

```
python manage.py createsuperuser
```

Run server
```
python manage.py runserver
```

## After installation <a name="post_install"></a>

If you want you can add default pictures with command
```
python manage.py load_data
```
