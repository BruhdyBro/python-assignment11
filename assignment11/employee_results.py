# Task 1

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


try:
    with sqlite3.connect("../db/lesson.db") as conn:
        print("Database connected sucessfully.")

        sql_statement = """
        SELECT last_name, SUM(price * quantity) AS revenue 
        FROM employees e 
        JOIN orders o 
            ON e.employee_id = o.employee_id 
        JOIN line_items l 
            ON o.order_id = l.order_id 
        JOIN products p 
            ON l.product_id = p.product_id 
        GROUP BY e.employee_id;
        """

        df = pd.read_sql_query(sql_statement, conn)

        df.plot.bar('last_name', 'revenue', color=['green','orange'])
        plt.xlabel("Employee Last Name")
        plt.ylabel("Revenue")
        plt.title("Revenue by Employee")
        plt.grid(True)
        plt.show()

except Exception as e:
    print("Error: ", e)

