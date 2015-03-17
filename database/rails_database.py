import sqlite3
import os
import sys

RAILS_DB = os.path.join(os.environ['HOME'], 'RoR', 'blog', 'db', 'development.sqlite3')

def get_post_id(title, body):
    db = sqlite3.connect(RAILS_DB)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM posts where title=? and body=? order by created_at DESC', (title,body))
    all_rows = cursor.fetchall()
    if len(all_rows) > 1:
        created = all_rows[0][3]
        post_id = all_rows[0][0]
        for row in all_rows:
            if row[4] > created:
                post_id = row[0]
                created = row[0]
        return post_id
    elif len(all_rows) == 0:
        return False
    else:
        return all_rows[0][0]
def get_comment_id(comment, post_id):
    db = sqlite3.connect(RAILS_DB)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM comments where post_id=? and body=?', (post_id,comment))
    all_rows = cursor.fetchall()
    if len(all_rows) > 1:
        created = all_rows[0][3]
        comment_id = all_rows[0][0]
        for row in all_rows:
            if row[4] > created:
                comment_id = row[0]
                created = row[0]
        return comment_id
    elif len(all_rows) == 0:
        return False
    else:
        return all_rows[0][0]
    

def main():
    title = sys.argv[1]
    body = sys.argv[2]
    comment = sys.argv[3]
    post_id = get_post_id(title, body)
    print post_id
    comment_id = get_comment_id(comment, post_id)
    print comment_id

if __name__ == '__main__':
  main()

