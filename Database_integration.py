import datetime
import os
import re
import sys
import sqlite3
from Info_messages import *


if getattr(sys, 'frozen', False):
    current_directory = os.path.dirname(sys.executable)
else:
    current_directory = os.path.dirname(os.path.abspath(__file__))


class DB:
    # class constractor
    def __init__(self):
        # connect with db
        self.conn = sqlite3.connect('jobhunt.db')

        # create cursor
        self.cur = self.conn.cursor()

        # create table in database
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS buy '
            '(id INTEGER PRIMARY KEY, company_name TEXT, status TEXT, where_find TEXT, times TEXT, comment TEXT)'
        )
        self.conn.commit()

    # create backup
    def create_backup(self):
        # connect to main database
        main_conn = sqlite3.connect('jobhunt.db')
        main_cur = main_conn.cursor()

        backup_files = [filename for filename in os.listdir(current_directory)
                        if re.match(r'backup_\d+\.db', filename)]
        if backup_files:
            backup_file_check = max(backup_files)
            backup_file_check_conn = sqlite3.connect(backup_file_check)
            backup_file_check_cur = backup_file_check_conn.cursor()
            main_cur.execute('SELECT * FROM buy')
            data_main = main_cur.fetchall()
            backup_file_check_cur.execute('SELECT * FROM buy_backup')
            data_backup = backup_file_check_cur.fetchall()
            if data_main == data_backup:
                return

        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        # create backup database
        backup_file = f'backup_{timestamp}.db'

        # connect to backup database
        backup_conn = sqlite3.connect(backup_file)
        backup_cur = backup_conn.cursor()

        # create table into backup database if it's not exist
        backup_cur.execute(
            'CREATE TABLE IF NOT EXISTS buy_backup '
            '(id INTEGER PRIMARY KEY, company_name TEXT, status TEXT, where_find TEXT, times TEXT, comment TEXT)'
        )
        backup_conn.commit()

        # select all data from main database
        main_cur.execute('SELECT * FROM buy')
        rows = main_cur.fetchall()

        # insert selected data from main database to backup database
        for row in rows:
            backup_cur.execute('INSERT OR REPLACE INTO buy_backup VALUES (?,?,?,?,?,?)', row)
        backup_conn.commit()

        # disconect both database
        backup_conn.close()
        main_conn.close()

    # destractor
    def __del__(self):
        # disconnect from db
        self.conn.close()

    # view all data
    def view_and_search(self, data):
        if data == 'all':
            self.cur.execute('SELECT * FROM buy')
            rows_search = self.cur.fetchall()
        elif data == 'Отказ' or data == 'Написали, жду':
            self.cur.execute('SELECT * FROM buy WHERE status=?', (data,))
            rows_search = self.cur.fetchall()
            if not rows_search:
                rows_search = 'Don\'t find'
        elif data == 'number':
            self.cur.execute('SELECT * FROM buy WHERE times>1')
            rows_search = self.cur.fetchall()
        else:
            rows_search = 'Don\'t find'

        if rows_search == 'Don\'t find':
            result = rows_search
        else:
            result = []
            for row in rows_search:
                row_str = str(row).strip('{}')
                result.append(row_str)
            long = f'\nTotal number: {str(len(result))}'
            result.append(long)

            result = '\n'.join(result)

        return result

    # add data
    def insert(self, company_name, status, where_find, times, comment):
        self.cur.execute('SELECT * FROM buy WHERE company_name=?', (company_name,))
        check_data = self.cur.fetchall()
        if check_data:
            error_message('This company already exists.')
            return
        else:
            self.cur.execute('INSERT INTO buy VALUES (NULL,?,?,?,?,?)',
                             (company_name, status, where_find, times, comment))
            self.conn.commit()
        info_message('The company was successfully added.')

    # update info
    def update(self, company_name, status, where_find, times, comment):
        self.cur.execute('UPDATE buy SET status=?, where_find=?, times=?, comment=? WHERE company_name=?',
                         (status, where_find, times, comment, company_name))
        self.conn.commit()
        info_message('Information about the company was successfully updated.')

    # delete data
    def delete_data(self, company_name):
        self.cur.execute('DELETE FROM buy WHERE company_name=?', (company_name,))
        self.conn.commit()
        info_message('This company was successfully deleted.')

    # find by company name
    def search_by_companyname(self, company_name):
        self.cur.execute('SELECT * FROM buy WHERE company_name=?', (company_name,))
        rows_search = self.cur.fetchall()
        result = []
        if rows_search:
            for row in rows_search:
                row_str = str(row).strip('{}')
                result.append(row_str)
            result = '\n'.join(result)
        else:

            result = 'Don\'t find'

        return result

    def total_number_rows(self):
        self.cur.execute('SELECT COUNT(*) FROM buy')
        total_rows = self.cur.fetchone()[0]
        return total_rows
