#!/usr/bin/python3

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

mySocket.bind((socket.gethostname(), 1235))


mySocket.listen(5)

estado = 0

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('HTTP request received:')
        peticion = recvSocket.recv(2048).decode('utf-8')
        peticion = peticion.split()
        print ('Answering back...')
        if estado == 0:
            estado = 1
            operando= peticion[1][1:]
            recvSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n' +
                '<html><body><h1>Primer operando= ' +
                str(operando) +
                '. Introduzca segundo operando</h1>' +
                '</body></html>' +
                '\r\n', 'utf-8'))

        else:
            operando2= peticion[1][1:]
            suma= int(operando) + int(operando2)
            print ('Answering back...')

            recvSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n' +
            '<html><body><h1>El resultado de ' +
            str(operando) + '+' + str(operando2) + '=' + str(suma) + '</h1>' +
            '</body></html>' +
            '\r\n', 'utf-8'))
            recvSocket.close()

except KeyboardInterrupt:
    print ("Closing binded socket")
    mySocket.close()
