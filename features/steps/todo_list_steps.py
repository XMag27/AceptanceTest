from behave import *
from todo_list import *

@given('the To-Do list is empty')
def step_impl(context):
    context.todo_list = []

@when('the user adds a task "{task}"')
def step_impl(context, task):
    add_item(context.todo_list, task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    assert task in context.todo_list

@given('the To-Do list contains "{task}"')
def step_impl(context, task):
    add_item(context.todo_list, task)

@when('the user asks for the list of items')
def step_impl(context):
    context.list = list_items(context.todo_list)

@when('the user marks "{task}" as completed')
def step_impl(context, task):
    mark_completed(context.todo_list, task)
@then('the to-do list should not contain "{task}"')
def step_impl(context, task):
    assert task not in context.todo_list

@when('the user clears the list')
def step_impl(context):
    clear_list(context.todo_list)
@then('the to-do list should be empty')
def step_impl(context):
    assert context.todo_list == []


@given('the To-Do list is not empty')
def step_impl(context):
    context.todo_list != []
@then('the email should be sent')
def step_impl(context):
    pass