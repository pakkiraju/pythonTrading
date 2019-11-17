# -*- coding: utf-8 -*-

import click
import datetime

from file_handler import read_file, write_file


MSG = '{color}{content}{nc}'

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"

REVERSE = "\033[;7m"
NC = '\033[0m'  # No Color

now = lambda: datetime.datetime.now()


def alert(content, color=RED):
    return MSG.format(color=color, content=content, nc=NC)

def not_completed_todos():
    todos = read_file()
    return [todo for todo in todos if todo['status'] == 0]

def completed_todos():
    todos = read_file()
    return [todo for todo in todos if todo['status'] == 1]

def last_week_completed_todos():
    result = list()
    todos = completed_todos()
    for todo in todos:
        if (now() - todo['time']) < datetime.timedelta(days=7):
            result.append(todo)
    return result

def show():
    print alert('\n=========================== TODO ================================', BLUE)
    for index, todo in enumerate(not_completed_todos()):
        msg = '{}. {}'.format(index+1, todo['task_detail'].encode('utf-8'))
        print alert(msg, RED)

    print alert('\n=========================== DONE ================================', BLUE)
    for index, todo in enumerate(last_week_completed_todos()):
        msg = '{}. {}'.format(index+1, todo['task_detail'].encode('utf-8'))
        print alert(msg, GREEN)
    print '\n'

def showall():
    print alert('\n=========================== TODO ================================', BLUE)
    for index, todo in enumerate(not_completed_todos()):
        msg = '{}. {}'.format(index+1, todo['task_detail'].encode('utf-8'))
        print alert(msg, RED)

    print alert('\n=========================== DONE ================================', BLUE)
    for index, todo in enumerate(completed_todos()):
        msg = '{}. {}'.format(index+1, todo['task_detail'].encode('utf-8'))
        print alert(msg, GREEN)
    print '\n'

@click.command()
@click.argument('task_detail')
def add(task_detail):
    todos = read_file()
    todos.append(
        {
            'task_detail': task_detail,
            'status': 0,
            'time': now()
        }
    )
    write_file(todos)
    print 'got it.'

@click.command()
def _list():
    show()

@click.command()
def listall():
    showall()

@click.command()
@click.argument('task_id')
def kill(task_id):
    todos = not_completed_todos()
    todos[int(task_id)-1]['status'] = 1
    write_file(todos + completed_todos())
    print 'cool!\nTasks left:'
    show()
