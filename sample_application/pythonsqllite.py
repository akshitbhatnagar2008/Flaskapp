import sqlite3
from sqlite3 import Error
import pandas as pd


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid

def create_table(conn, name):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """

    try:
        sql = 'drop table ' + name
        cur = conn.cursor()
        cur.execute(sql)
    except:
        pass

    sql = 'Create table ' + name + '(State,country,latitude,longitude)'
    cur = conn.cursor()
    cur.execute(sql)
    #return cur.lastrowid


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def create_row(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO usa_locs(State,country,latitude,longitude)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def read_data(conn):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' Select * from usa_locs'''
    cur = conn.cursor()
    df = cur.execute(sql)
    return df

def main():
    database = r"/Users/bhatnagarakshit10/Documents/flask-bootstrap/pythonsqlite.db"

    df = pd.read_csv('/Users/bhatnagarakshit10/Documents/flask-bootstrap/usa_lat_long.csv')
    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        create_table(conn, 'usa_locs')

        # tasks
        #task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        #task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

        # create tasks
        #create_task(conn, task_1)
        #create_task(conn, task_2)
        df.apply(lambda x: create_row(conn, x), axis=1)

if __name__ == '__main__':
    main()