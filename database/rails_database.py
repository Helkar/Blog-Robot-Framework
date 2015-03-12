import sqlite3
import os
import sys

RAILS_DB = os.path.join(os.environ['HOME'], 'RoR', 'blog', 'db', 'development.sqlite3')

def get_post_id(title, body):
    db = sqlite3.connect(RAILS_DB)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM posts')
    all_rows = cursor.fetchall()
    for row in all_rows:
        post_id = row[0]
        post_title = row[1]
        post_body = row[2]
        if post_title == title and post_body == body:
            return post_id
    return None

def main():
    title = sys.argv[1]
    body = sys.argv[2]
    post_id = get_post_id(title, body)
    print post_id

if __name__ == '__main__':
  main()

