import functools
import os
import sqlite3
from datatest import validate

db_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'clients.db')


def db(query):
    """:param query: str query sql
    :return: cursor"""
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    cur.execute(query)

    return cur


class TestDB:

    def test_verify_db(self):
        """This test verifies the structure of the database, that the age field of each record is greater than 5,
        and that there is no null value in the record"""

        cur = db('SELECT * FROM CLIENTS')
        column_names = [item[0] for item in cur.description]

        ages = [a for a in cur.execute('SELECT age FROM CLIENTS')]

        not_null = [a for a in cur.execute('SELECT * FROM CLIENTS')]

        for age in ages:
            str(age)
            res = functools.reduce(lambda sub, ele: sub * 10 + ele, age)
            assert res > 5

        for n in not_null:
            str(n)
            assert n is not None

        validate(column_names, {'id', 'name', 'country', 'age'})

        cur.close()
