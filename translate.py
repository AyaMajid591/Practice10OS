PAGE_SIZE = 1024
table = {0: 5, 1: 2, 2: 7, 3: 0}

def translate(addr):
    page = addr // PAGE_SIZE
    offset = addr % PAGE_SIZE  


    if page not in table:
         return f"{addr}: стр. {page}, смещ. {offset} -> страница отсутствует"

    phys = table[page] * PAGE_SIZE + offset
    return f"{addr}: стр. {page}, смещ. {offset} -> кадр {table[page]} -> {phys}"

for a in (1200, 3100, 5000):
    print(translate(a))

