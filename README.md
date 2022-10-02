run:

```console
./manage.py test
```

Get the following output:

```
Found 1 test(s).
Creating test database for alias 'default'...
System check identified some issues:

WARNINGS:
?: (admin.W411) 'django.template.context_processors.request' must be enabled in DjangoTemplates (TEMPLATES) in order to use the admin navigation sidebar.

System check identified 1 issue (0 silenced).
E
======================================================================
ERROR: test_command_output (polls.tests.ClosepollTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/fjm/code/django-stuff/tutorial/polls/tests.py", line 10, in test_command_output
    call_command("closepoll", poll_ids=1, stdout=out)
  File "/home/fjm/.local/share/virtualenvs/tutorial/lib/python3.10/site-packages/django/core/management/__init__.py", line 168, in call_command
    parse_args.append(min(opt.option_strings))
ValueError: min() arg is an empty sequence

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
Destroying test database for alias 'default'...
```

Instead, if run from the terminal using manage.py:

```console
./manage.py closepoll 1
```

There's no output (as expected as the command does nothing)
