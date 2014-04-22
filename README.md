# Django Background Tasker

Django Background Tasker is a simple pluggable Django application that allows for background working of tasks. It is heavily inspired by [django-ztask](https://github.com/dmgctrl/django-ztask)

# Usage

Download and install [ØMQ](http://zeromq.org/intro:get-the-software)

Install django-background-tasker using pip:

    pip install django-background-tasker

Add `background_tasker` to your `INSTALLED_APPS` setting in `settings.py`

    INSTALLED_APPS = (
        ...
        'background_tasker',
    )

## Running the background tasker process

Run the background tasker process using the manage.py command:

    ./manage.py background_tasker

Your background tasker will listen to the ØMQ url and process tasks as they appear on the socket

## Settings

There are two currently only two settings to configure `background_tasker`

    BACKGROUND_TASKER_URL = 'tcp://127.0.0.1:5555'

By default, the worker will run over TCP, listening on 127.0.0.1 port 5555.

    BACKGROUND_TASKER_ALWAYS_EAGER = False

If set to `True`, all `.async` and tasks will be run in-process and
not sent to the que. Good for task debugging.


## Running in production

A recommended way to run in production would be to use a process manager like
supervisor with the following config file

    [program:background-tasker]
    command = /var/www/path/to/site/manage.py background_tasker
    stderr_logfile = /var/log/supervisord/background-tasker-stderr.log
    stdout_logfile = /var/log/supervisord/background-tasker-stdout.log
    autostart = true
    autorestart = true
    user = www-data
    group = www-data


## Making functions in to background tasks

Decorators and function extensions make tasks able to run. 
Unlike some solutions, tasks can be in any file anywhere. 

It is a recommended best practice that instead of passing a Django model object to a task, you instead pass along the model's ID or primary key, and re-get the object in the task function.

## The @task Decorator

    from django_zero_task.decorators import task

The `@task` decorator will turn any normal function in to a background task if called using the `.async` function

## Function extensions

Any function can be called in one of two ways:

`func(*args, *kwargs)`

Calling a function normally will bypass the decorator and call the function directly

`func.async(*args, **kwargs)`

Calling a function with `.async` will cause the function task to be called asyncronously on a worker.


## Example

```python
from background_tasker.decorators import task

@task
def print_this(what_to_print):
    print what_to_print

if __name__ == '__main__':

    # Call the function directly
    print_this('Hello world!')

    # Call the function asynchronously
    print_this.async('This will print to the background_tasker worker log')
```

## Test echo command

A management command is provided for a simple eaco test. Anything you provide on the command line will be echoed out by the background tasker

```bash
./manage.py background_tasker
```