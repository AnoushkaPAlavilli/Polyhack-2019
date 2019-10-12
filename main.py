#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:41:41 2019

@author: benpradko, anoushkaalavilli, ryangayhour
"""
import sqlite3
conn = sqlite3.connect('todo.db')
query = "<SQLite Query goes here>"
result = conn.execute(query)

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
          id INTEGER PRIMARY KEY,
          Title TEXT,
          Description TEXT,
          _is_done boolean,
          _is_deleted boolean,
          CreatedOn Date DEFAULT CURRENT_DATE,
          DueDate Date,
          UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query)
    def create_user_table(self):
        # create user table in similar fashion
        # come on give it a try it's okay if you make mistakes
        pass

        if __name__ == "__main__":
            Schema()
            app.run(debug=True)

    class ToDoModel:
        TABLENAME = "TODO"

        def __init__(self):
            self.conn = sqlite3.connect('todo.db')
    
        def create(self, text, description):
            query = f'insert into {TABLENAME} ' \
                    f'(Title, Description) ' \
                    f'values ("{text}","{description}")'
    
            result = self.conn.execute(query)
            return result
   # Similarly add functions to select, delete and update todo

   # Service.py
class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        self.model.create(params["text"], params["Description"])

# app.py

    @app.route("/todo", method=["POST"])
    def create_todo():
        return ToDoService().create(request.get_json())
