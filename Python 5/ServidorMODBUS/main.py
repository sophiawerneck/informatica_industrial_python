from servidormodbus import ServidorMODBUS


s = ServidorMODBUS('localhost',502) # 502 é a porta padrão do protocolo Modbus
s.run()