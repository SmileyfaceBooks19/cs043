def http_get(link, page):
    import socket
    sock = socket.create_connection((link, 80))
    sock.sendall(('GET ' + page + ' HTTP/1.1\r\nHost:' + link + '\r\n\r\n').encode())
    print(sock.recv(1000).decode())
    sock.close()


#http_get('50.87.178.13', '/CScourses/nonexistent.html')
#http_get('www.google.com','/')

def http_head(link,page):
    import socket
    sock = socket.create_connection((link, 80))
    sock.sendall(('HEAD ' + page + ' HTTP/1.1\r\nHost:' + link + '\r\n\r\n').encode())
    print(sock.recv(1000).decode())
    sock.close()

http_head('50.87.178.13', '/CScourses/03b2_minimal-meta.html')