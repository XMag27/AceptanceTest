
Feature: To-Do list

    Scenario: Adding a task
        Given the To-Do list is empty
        When the user adds a task "Buy groceries"
        Then the to-do list should contain "Buy groceries"

    Scenario: List items
        Given the To-Do list contains "Buy groceries"
        When the user asks for the list of items
        Then the to-do list should contain "Buy groceries"

    Scenario: Mark completed
        Given the To-Do list contains "Buy groceries"
        When the user marks "Buy groceries" as completed
        Then the to-do list should not contain "Buy groceries"

    Scenario: Clear list
        Given the To-Do list contains "Buy groceries"
        When the user clears the list
        Then the to-do list should be empty
