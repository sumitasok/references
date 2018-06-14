# -*- coding: utf-8 -*-
print('python printer')
from sqlalchemy import create_engine

# import time
# time.sleep(12)

mysql_conn_string = 'mysql+pymysql://root:P09L123cedS@mydb:3306/iam'
db = create_engine(mysql_conn_string)

import pandas as pd

df_verses = pd.read_sql('SELECT LEAST(3, 12, 34, 8, 25)', db)
print(df_verses)


import SimpleHTTPServer
import SocketServer

PORT = 2000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(('', PORT), Handler)

print('serving at port', PORT)
httpd.serve_forever()
