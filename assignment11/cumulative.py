# Task 2

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def cumulative(row):
    totals_above = df['total_price'][0:row.name+1]
    return totals_above.sum()

try:
    with sqlite3.connect("../db/lesson.db") as conn:
        print("Database connected sucessfully.")

        # Get total price per order
        sql_statement = """
        SELECT order_id, sum(price * quantity) AS total_price
        FROM line_items l
        JOIN products p
            ON l.product_id = p.product_id
        GROUP BY order_id
        """

        df = pd.read_sql_query(sql_statement, conn)
        df['cumulative'] = df['total_price'].cumsum()

        print(df)
        print()
        df.info()
        
        plt.plot(df['order_id'], df['cumulative'])
        plt.xlabel("Order ID")
        plt.ylabel("Cumulative Revenue")
        plt.title("Cumulative Revenue vs. Order ID")
        plt.grid(True)
        plt.show()

except Exception as e:
    print("Error: ", e)

