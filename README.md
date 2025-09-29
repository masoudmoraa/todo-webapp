# Todo App

##  Installation Guide

Follow these steps to run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/masoudmoraa/todo-webapp.git
```

### 2. Create a Django project
Inside the repo folder, create a Django project named **project**:
```bash
django-admin startproject project
```

### 3. Copy project files
Copy the provided files from this repository into the newly created `project/` folder, overwriting if necessary.

### 4. Install dependencies
Make sure you have Python and pip installed.  
It’s recommended to use a virtual environment.  
install Django:
```bash
pip install django
```

### 5. Apply migrations
Run the following to set up the database:
```bash
python manage.py migrate
```

### 6. Start the server
```bash
python manage.py runserver
```

Now open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to access the app.

---

##  Features
- Add new tasks  
- Edit tasks  
- Delete tasks  


