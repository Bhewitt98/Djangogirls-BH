#Compilation of all the cmd prompts I ran

Microsoft Windows [Version 10.0.26200.7171]
(c) Microsoft Corporation. All rights reserved.

C:\Users\baker>mkdir djangogirls
A subdirectory or file djangogirls already exists.

C:\Users\baker>cd djangogirls

C:\Users\baker\djangogirls>python -m venv lizardenv
Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

C:\Users\baker\djangogirls> python -m venv lizardenv
Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

C:\Users\baker\djangogirls>pip install virtualenv
'pip' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\baker\djangogirls>py -m venv lizardenv

C:\Users\baker\djangogirls>lizardenv\Scripts\activate

(lizardenv) C:\Users\baker\djangogirls>lizardenv ~$ py -m pip install --upgrade pip
'lizardenv' is not recognized as an internal or external command,
operable program or batch file.

(lizardenv) C:\Users\baker\djangogirls>py -m pip install --upgrade pip
Requirement already satisfied: pip in c:\users\baker\djangogirls\lizardenv\lib\site-packages (24.3.1)
Collecting pip
  Downloading pip-25.3-py3-none-any.whl.metadata (4.7 kB)
Downloading pip-25.3-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 2.7 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.3.1
    Uninstalling pip-24.3.1:
      Successfully uninstalled pip-24.3.1
Successfully installed pip-25.3

(lizardenv) C:\Users\baker\djangogirls>pip install -r requirements.txt
ERROR: Invalid requirement: 'Django~5.1.2': Expected end or semicolon (after name and no valid version specifier)
    Django~5.1.2
          ^ (from line 1 of requirements.txt)

(lizardenv) C:\Users\baker\djangogirls>pip install -r requirements.txt
Collecting Django~=5.1.2 (from -r requirements.txt (line 1))
  Downloading django-5.1.14-py3-none-any.whl.metadata (4.1 kB)
Collecting asgiref<4,>=3.8.1 (from Django~=5.1.2->-r requirements.txt (line 1))
  Downloading asgiref-3.11.0-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.3.1 (from Django~=5.1.2->-r requirements.txt (line 1))
  Downloading sqlparse-0.5.3-py3-none-any.whl.metadata (3.9 kB)
Collecting tzdata (from Django~=5.1.2->-r requirements.txt (line 1))
  Downloading tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Downloading django-5.1.14-py3-none-any.whl (8.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.3/8.3 MB 7.5 MB/s  0:00:01
Downloading asgiref-3.11.0-py3-none-any.whl (24 kB)
Downloading sqlparse-0.5.3-py3-none-any.whl (44 kB)
Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Installing collected packages: tzdata, sqlparse, asgiref, Django
Successfully installed Django-5.1.14 asgiref-3.11.0 sqlparse-0.5.3 tzdata-2025.2

(lizardenv) C:\Users\baker\djangogirls>django-admin.exe startproject mysite .

(lizardenv) C:\Users\baker\djangogirls>py manage.py migrate
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

(lizardenv) C:\Users\baker\djangogirls>python manage.py runserver
Traceback (most recent call last):
  File "C:\Users\baker\djangogirls\manage.py", line 22, in <module>
    main()
    ~~~~^^
  File "C:\Users\baker\djangogirls\manage.py", line 18, in main
    execute_from_command_line(sys.argv)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Users\baker\djangogirls\lizardenv\Lib\site-packages\django\core\management\__init__.py", line 442, in execute_from_command_line
    utility.execute()
    ~~~~~~~~~~~~~~~^^
  File "C:\Users\baker\djangogirls\lizardenv\Lib\site-packages\django\core\management\__init__.py", line 382, in execute
    settings.INSTALLED_APPS
  File "C:\Users\baker\djangogirls\lizardenv\Lib\site-packages\django\conf\__init__.py", line 81, in __getattr__
    self._setup(name)
    ~~~~~~~~~~~^^^^^^
  File "C:\Users\baker\djangogirls\lizardenv\Lib\site-packages\django\conf\__init__.py", line 68, in _setup
    self._wrapped = Settings(settings_module)
                    ~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\baker\djangogirls\lizardenv\Lib\site-packages\django\conf\__init__.py", line 166, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
  File "C:\Users\baker\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1022, in exec_module
  File "<frozen importlib._bootstrap_external>", line 1160, in get_code
  File "<frozen importlib._bootstrap_external>", line 1090, in source_to_code
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\Users\baker\djangogirls\mysite\settings.py", line 28
    ALLOWED_HOSTS = ['localhost', '127.0.0.1'. 'pythonanywhere.com']
                                               ^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax

(lizardenv) C:\Users\baker\djangogirls>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 20, 2025 - 19:51:20
Django version 5.1.14, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[20/Nov/2025 19:55:14] "GET / HTTP/1.1" 200 12068
Not Found: /favicon.ico
[20/Nov/2025 19:55:15] "GET /favicon.ico HTTP/1.1" 404 2208

(lizardenv) C:\Users\baker\djangogirls>
(lizardenv) C:\Users\baker\djangogirls>py manage.py startapp blog

(lizardenv) C:\Users\baker\djangogirls>python manage.py makemigrations blog
Migrations for 'blog':
  blog\migrations\0001_initial.py
    + Create model Post

(lizardenv) C:\Users\baker\djangogirls>python manage.py migrate blog
Operations to perform:
  Apply all migrations: blog
Running migrations:
  Applying blog.0001_initial... OK

(lizardenv) C:\Users\baker\djangogirls>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 20, 2025 - 20:04:03
Django version 5.1.14, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[20/Nov/2025 20:04:12] "GET /admin/ HTTP/1.1" 302 0
[20/Nov/2025 20:04:12] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4165
[20/Nov/2025 20:04:12] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 200 2810
[20/Nov/2025 20:04:12] "GET /static/admin/css/login.css HTTP/1.1" 200 951
[20/Nov/2025 20:04:12] "GET /static/admin/css/dark_mode.css HTTP/1.1" 200 2804
[20/Nov/2025 20:04:12] "GET /static/admin/css/responsive.css HTTP/1.1" 200 17972
[20/Nov/2025 20:04:12] "GET /static/admin/css/base.css HTTP/1.1" 200 22092
[20/Nov/2025 20:04:12] "GET /static/admin/js/theme.js HTTP/1.1" 200 1653
[20/Nov/2025 20:04:12] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 200 3063
[20/Nov/2025 20:09:42] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[20/Nov/2025 20:09:42] "GET /admin/ HTTP/1.1" 200 6640
[20/Nov/2025 20:09:42] "GET /static/admin/css/base.css HTTP/1.1" 304 0
[20/Nov/2025 20:09:42] "GET /static/admin/css/dark_mode.css HTTP/1.1" 304 0
[20/Nov/2025 20:09:42] "GET /static/admin/js/theme.js HTTP/1.1" 304 0
[20/Nov/2025 20:09:42] "GET /static/admin/css/responsive.css HTTP/1.1" 304 0
[20/Nov/2025 20:09:42] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 304 0
[20/Nov/2025 20:09:42] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 441
[20/Nov/2025 20:09:42] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 304 0
[20/Nov/2025 20:09:42] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
[20/Nov/2025 20:09:42] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
[20/Nov/2025 20:09:59] "GET /admin/blog/post/ HTTP/1.1" 200 7751
[20/Nov/2025 20:09:59] "GET /static/admin/css/changelists.css HTTP/1.1" 200 6878
[20/Nov/2025 20:09:59] "GET /static/admin/js/jquery.init.js HTTP/1.1" 200 347
[20/Nov/2025 20:09:59] "GET /static/admin/js/core.js HTTP/1.1" 200 6208
[20/Nov/2025 20:09:59] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 200 9097
[20/Nov/2025 20:09:59] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[20/Nov/2025 20:09:59] "GET /static/admin/js/urlify.js HTTP/1.1" 200 7887
[20/Nov/2025 20:09:59] "GET /static/admin/js/actions.js HTTP/1.1" 200 8076
[20/Nov/2025 20:09:59] "GET /static/admin/js/prepopulate.js HTTP/1.1" 200 1531
[20/Nov/2025 20:09:59] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 200 285314
[20/Nov/2025 20:09:59] "GET /static/admin/js/filters.js HTTP/1.1" 200 978
[20/Nov/2025 20:09:59] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 200 325171
[20/Nov/2025 20:09:59] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 200 331
[20/Nov/2025 20:10:01] "GET /admin/blog/post/add/ HTTP/1.1" 200 12731
[20/Nov/2025 20:10:01] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[20/Nov/2025 20:10:01] "GET /static/admin/css/forms.css HTTP/1.1" 200 8794
[20/Nov/2025 20:10:01] "GET /static/admin/js/prepopulate_init.js HTTP/1.1" 200 586
[20/Nov/2025 20:10:01] "GET /static/admin/js/calendar.js HTTP/1.1" 200 9141
[20/Nov/2025 20:10:01] "GET /static/admin/js/admin/DateTimeShortcuts.js HTTP/1.1" 200 19319
[20/Nov/2025 20:10:01] "GET /static/admin/css/widgets.css HTTP/1.1" 200 11564
[20/Nov/2025 20:10:01] "GET /static/admin/img/icon-viewlink.svg HTTP/1.1" 200 581
[20/Nov/2025 20:10:01] "GET /static/admin/js/change_form.js HTTP/1.1" 200 606
[20/Nov/2025 20:10:01] "GET /static/admin/img/icon-clock.svg HTTP/1.1" 200 677
[20/Nov/2025 20:10:01] "GET /static/admin/img/icon-calendar.svg HTTP/1.1" 200 1086
[20/Nov/2025 20:10:18] "POST /admin/blog/post/add/ HTTP/1.1" 302 0
[20/Nov/2025 20:10:18] "GET /admin/blog/post/add/ HTTP/1.1" 200 12957
[20/Nov/2025 20:10:18] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[20/Nov/2025 20:10:18] "GET /static/admin/img/icon-yes.svg HTTP/1.1" 200 436
[20/Nov/2025 20:10:29] "POST /admin/blog/post/add/ HTTP/1.1" 302 0
[20/Nov/2025 20:10:29] "GET /admin/blog/post/ HTTP/1.1" 200 9478
[20/Nov/2025 20:10:29] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[20/Nov/2025 20:10:36] "GET /admin/blog/post/add/ HTTP/1.1" 200 12731
[20/Nov/2025 20:10:36] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[20/Nov/2025 20:10:54] "POST /admin/blog/post/add/ HTTP/1.1" 302 0
[20/Nov/2025 20:10:54] "GET /admin/blog/post/add/ HTTP/1.1" 200 12978
[20/Nov/2025 20:10:54] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[20/Nov/2025 20:11:05] "POST /admin/blog/post/add/ HTTP/1.1" 302 0
[20/Nov/2025 20:11:05] "GET /admin/blog/post/ HTTP/1.1" 200 10066
[20/Nov/2025 20:11:05] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[20/Nov/2025 20:11:20] "GET /admin/blog/post/add/ HTTP/1.1" 200 12731
[20/Nov/2025 20:11:20] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[20/Nov/2025 20:11:32] "POST /admin/blog/post/add/ HTTP/1.1" 302 0
[20/Nov/2025 20:11:32] "GET /admin/blog/post/add/ HTTP/1.1" 200 12958
[20/Nov/2025 20:11:32] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[20/Nov/2025 20:11:45] "POST /admin/blog/post/add/ HTTP/1.1" 302 0
[20/Nov/2025 20:11:45] "GET /admin/blog/post/ HTTP/1.1" 200 10615
[20/Nov/2025 20:11:45] "GET /admin/jsi18n/ HTTP/1.1" 200 3342

#CMD prompts to create my user account 

Microsoft Windows [Version 10.0.26200.7171]
(c) Microsoft Corporation. All rights reserved.

C:\Users\baker>cd djangogirls

C:\Users\baker\djangogirls>lizardenv\Scripts
'lizardenv\Scripts' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\baker\djangogirls>lizardenv\Scripts\activate

(lizardenv) C:\Users\baker\djangogirls>python manage.py createsuperuser
Username (leave blank to use 'baker'): bhewitt
Email address: baker.hewitt1@gmail.com
Password:
Password (again):
Superuser created successfully.

(lizardenv) C:\Users\baker\djangogirls>

#