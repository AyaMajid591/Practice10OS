
import os
import platform
import mmap

PAGE = mmap.PAGESIZE
x = bytearray(100)
addr = id(x)

print("ОС:", platform.system(), platform.machine())
print("PID:", os.getpid())
print("Размер страницы:", PAGE, "байт")
print("Бит на смещение:", PAGE.bit_length() - 1)
print("Виртуальный адрес:", hex(addr))
print("Номер страницы:", hex(addr // PAGE))
print("Смещение:", hex(addr % PAGE), "=", addr % PAGE)
