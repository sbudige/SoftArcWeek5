

# HelloWorld Django Project

A simple Hello World Django app which returns a JSON object with Hello World message.



## Installation
Need to install some pre-requirements to run this Django Hello World project.
 
To use virtual environments run below code in terminal.

```bash
  pip install virtualenv
```
To create a new virtual environments run below code. In place of myenv give any name.
```bash
  virtualenv myenv
```
To activate virtual environments run following command:
```bash
  .\myenv\Scripts\activate.ps1
```
To run Django Hello World need to install Django framework, run below command:
```bash
  pip install -r .\requirements.txt
```
Now run:
```bash
  python manage.py migrate
```
After running above command you will see:
```bash
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```
Change the directory to helloworld_project, run below code:
```bash
  cd .\helloworld_project\
```

## Run Django Application
Now run below code:
```bash
  python manage.py runserver
```
After running the above command you will see like below:
```bash
  Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    November 24, 2022 - 11:21:39
    Django version 4.1.3, using settings 'helloworld_project.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
```
Now go to your browser and open http://127.0.0.1:8000/ now you can see:
```bash
  {"Message": "Hello World!"}
```