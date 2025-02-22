import sqlite3
#import tkinter

def get_blog_list():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("INSERT INTO blog VALUES (1, '첫 번째 블로그', '첫 번째 블로그입니다.', '20190827')")
    c.execute("SELECT * FROM blog")
    result = c.fetchall()
    print(result)
    conn.close()
    return result
#get_blog_list()
#root=Tk()
#root.mainloop()