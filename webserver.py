import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

print('Запущен')
webdir = 'E:/СредыРазработки/(sem)pyCharm/htmlProj/MySite' # место, где находится наш сайтик и cgi-bin
port = 80                                     # по умолчанию http://localhost

os.chdir(webdir)                                    # перейти в корневой каталог html
srvaddr = ("", port)                                # имя хоста и номер порта
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.serve_forever()                              # Запускаем сервер, как бесконечный процесс
