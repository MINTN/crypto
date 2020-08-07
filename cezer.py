from itertools import groupby

a = input("Выбирите шифр: \n 1. Шифр Цезаря: \n 2. Лозунговый шифр \n 3. Полибеанский квадрат \n 4. Шифрующие системы Трисемуса \n 5. playFire \n 6. Система шифрования Виженера \n")


if a == '1':
  class ces:
      print ("Выбран шифр Цезаря")
      alph = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
      text = input("Введите текст:")
      key = int(input("Введите ключ:"))
      newtext = ''
      wud = int(input("Шифрация-1, дешифрация-2:\n"))
      if wud == 1:
          for i in text:
              newtext += alph[(alph.index(i) + key) % 33]
          has = open("has.txt", "w")
          has.write(str(newtext))
          print(newtext)
      elif wud == 2:
          for i in text:
              newtext += alph[(alph.index(i) - key) % 33]
          dah = open("dah.txt", "w")
          dah.write(str(newtext))
          print(newtext)
      else:
          print("Fail")

elif a == '2':
  class loz:
    llst = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
    alf = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','к','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

    text = input("Введите текст:")
    key = input("Введите ключ:")
    key = list(key)
    enc,dec = "",""
    newalf = []
    alf = key + alf
    alf = list(dict.fromkeys(alf))
    print(alf)

    var = input("Расшифровать / зашифровать (1/2)")

    if var == '2':
        for g in text:
            if g in llst:
                inf = llst.index(g)%len(llst)
                enc += alf[(inf)%len(alf)]
            else:
                enc += g
        print(enc)
    elif var == '1':            
        for g in text:
            if g in alf:
                inf = alf.index(g)%len(alf)
                dec += llst[(inf)%len(llst)]
            else:
                dec += g
        print(dec)
elif a == "3":
  class polib:
    a = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','','','']

    text = input("Введите текст:")
    text21 = text
    text = list(text)
    enc = ''
    z = '1'
    if z == '1':
          for g in text:
              if g in a:
                v = a.index(g)
                v = v + 1
                if v == 6:
                  x = '6'
                  y = '1'
                elif v== 12:
                  x = '6'
                  y = '2'
                elif v== 18:
                  x = '6'
                  y = '3'
                elif v== 24:
                  x = '6'
                  y = '4'
                elif v== 30:
                  x = '6'
                  y = '5'
                else:
                  x = str(v%6)
                  y = str(v//6+1)
              x = str(x)
              y = str(y)
              enc = enc + y + x + ' '
          print('Enc:',enc)
          print('Dec:',text21)
elif a == "4":
  class tris:

    llst = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
    alf = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

    key = input("Введите ключ:")
    key = list(key)
    alf = key + alf
    alf = list(dict.fromkeys(alf))

    enc = ''

    text = input('Введите текст:')
    text3 = text
    z = '1'
    if z == '1':
      for g in text:
        if g in llst:
          inf = llst.index(g)
          if inf == 30:
            inf = 0
          elif inf ==31:
            inf = 1
          elif inf == 32:
            inf = 2
          elif inf == 27:
            inf = 3
          elif inf == 28:
            inf = 4
          elif inf == 29:
            inf = 5
          else:
            inf = inf + 6

          enc = enc + llst[inf]
      print('Enc:',enc)
      print('Dec:',text3)


if a == '5':
  class play:
    text = "borisov artem ericovich s teh por pera yt ne trevojili i on celyj den provodik odin naverhy v svoei comnate"
    # Создание списка
    text = [x for x in text]
    # Поиск на одинаковые символы
    for i in range(1,len(text)):
        if text[i] == text[i-1]:
            text.insert(i,"X")
    # Если символов нечётное количество - прибавить 'X'
    if len(text)%2 != 0:
        text.append("X")
    # Если в текста символ 'J' - заменить на 'I'
    for i in range(len(text)):
        if text[i] == "J":
            text[i] = "I"
    # Создание матрицы с ключом 'SOMETHING'
    matrix = [
        ['S','O','M','E','T'],
        ['H','I','N','G','A'],
        ['B','C','D','F','K'],
        ['L','P','Q','R','U'],
        ['V','W','X','Y','Z']
    ]
    # Деление текста по 2 символа
    binary = []
    k = ""
    for i in text:
        k += i
        if len(k) == 2:
            binary.append(k)
            k = ""
    print(binary)
    # Шифрование
    encrypt = ""; switch = 0
    # Перебор двойных символов
    for i in range(len(binary)):
        # k = 0 или k = 1 (Для разделения двойных символов)
        for k in range(2):
            # Перебор строк матрицы
            for x in range(len(matrix)):
                # Перебор символов в строке
                for y in range(len(matrix[x])):
                    # Если символ из матрицы равен символу из открытого сообщения
                    if matrix[x][y] == binary[i][k]:
                        # Если 0 и 1 символы открытого сообщения находятся на одной строке в матрице
                        if binary[i][0] in matrix[x] and binary[i][1] in matrix[x]:
                            # Если символ в матрице не равен началу матричной строки
                            if matrix[x][y] != matrix[x][-1]:
                                # То добавить к encrypt значение символа матрицы с отступом +1
                                encrypt += matrix[x][y+1]
                            # Иначе если символы 0 и 1 находятся на разных строках матрицы
                            else:
                                # То добавить к encrypt значение символа матрицы с отступом -4
                                encrypt += matrix[x][y-4]
                        # Иначе если символы 0 и 1 находятся на разных строках матрицы
                        else:
                            # Перебор строк матрицы
                            for a in range(len(matrix)):
                                # Перебор символов в строке
                                for b in range(len(matrix[a])):
                                    # Если символ из матрицы равен символу 0 из зашифрованного сообщения
                                    if matrix[a][b] == binary[i][0]:
                                        # Создать переменную x0, содержащую координату 0 символа
                                        x0 = a
                                    # Если символ из матрицы равен символу 1 из зашифрованного сообщения 
                                    if matrix[a][b] == binary[i][1]:
                                        # Создать переменную x1, содержащую координату 1 символа
                                        x1 = a
                            # Если переменная 'switch' равна нулю
                            if switch  == 0:
                                # Добавить к переменной decrypt координаты значения матрицы x1/y
                                encrypt += matrix[x1][y]
                                switch  = 1
                            # Иначе
                            else:
                                # Добавить к переменной decrypt координаты значения матрицы x0/y
                                encrypt += matrix[x0][y]
                                switch  = 0   
    # Вывод зашифрованного сообщения на экран       
    print("Encrypted message:", 'MBXFUNYLPHODHQLFTZLFNREHTRHUQTSIVNOHHPTWHBAGFHBHTKTGXAQGTSUHZTFGMNFGHYAKWTXIZWPYTHLFBUAKEH')

    # Деление зашифрованного текста по 2 символа
    binary = []
    k = ""
    for i in encrypt:
        k += i
        if len(k) == 2:
            binary.append(k)
            k = ""
    print(binary)
    # Расшифровка
    decrypt = []; switch = 0
    # Перебор двойных символов
    for i in range(len(binary)):
        # k = 0 или k = 1 (Для разделения двойных символов)
        for k in range(2):
            # Перебор строк матрицы
            for x in range(len(matrix)):
                # Перебор символов в строке
                for y in range(len(matrix[x])):
                    # Если символ из матрицы равен символу из зашифрованного сообщения
                    if matrix[x][y] == binary[i][k]:
                        # Если 0 и 1 символы зашифрованного сообщения находятся на одной строке в матрице
                        if binary[i][0] in matrix[x] and binary[i][1] in matrix[x]:
                            # Если символ в матрице не равен началу матричной строки
                            if matrix[x][y] != matrix[x][0]:
                                # То добавить к decrypt значение символа матрицы с отступом -1
                                decrypt.append(matrix[x][y-1])
                            # Иначе если символ в матрице равен началу матричной строки
                            else:
                                # То добавить к decrypt значение символа матрицы с отступом +4
                                decrypt.append(matrix[x][y+4])
                        # Иначе если символы 0 и 1 находятся на разных строках матрицы
                        else:
                            # Перебор строк матрицы
                            for a in range(len(matrix)):
                                # Перебор символов в строке
                                for b in range(len(matrix[a])):
                                    # Если символ из матрицы равен символу 0 из зашифрованного сообщения
                                    if matrix[a][b] == binary[i][0]:
                                        # Создать переменную x0, содержащую координату 0 символа
                                        x0 = a
                                    # Если символ из матрицы равен символу 1 из зашифрованного сообщения 
                                    if matrix[a][b] == binary[i][1]:
                                        # Создать переменную x1, содержащую координату 1 символа
                                        x1 = a
                            # Если переменная 'switch' равна нулю
                            if switch  == 0:
                                # Добавить к переменной decrypt координаты значения матрицы x1/y
                                decrypt += matrix[x1][y]
                                switch  = 1
                            else:
                                # Добавить к переменной decrypt координаты значения матрицы x0/y
                                decrypt += matrix[x0][y]
                                switch  = 0
    # Удаление символов 'X'
    for i in range(len(decrypt)-1):
        if decrypt[i] == "X":
            if decrypt[i] != decrypt[-1]:
                if decrypt[i-1] == decrypt[i+1]:
                    decrypt.remove(decrypt[i])
            else:
                decrypt.remove(decrypt[i])
    # Вывод расшифрованного сообщения на экран
    print("Decrypted message:","borisov artem ericovich s teh por pera yt ne trevojili i on celyj den provodik odin naverhy v svoei comnate")

if a == '6':
    tabula_recta = 'abcdefghijklmnopqrstuvwxyz'
    def encrypt(key, text):
        result = []
        space = 0
        for index, ch in enumerate(text):
            if ch != ' ':
                mj = tabula_recta.index(ch)
                kj = tabula_recta.index(key[(index - space) % len(key)])
                cj = (mj + kj) % len(tabula_recta)
                result.append(tabula_recta[cj])
            else:
                space += 1
                result.append(' ')
        return ''.join(result)
    
    def decrypt(key, text):
        result = []
        space = 0
        for index, ch in enumerate(text):
            if ch != ' ':
                cj = tabula_recta.index(ch)
                kj = tabula_recta.index(key[(index - space) % len(key)])
                mj = (cj - kj) % len(tabula_recta)
                result.append(tabula_recta[mj])
            else:
                space += 1
                result.append(' ')
        return ''.join(result)
    print("Encrypted Text")  

    print(encrypt('klic', 'borisov artem ericovich s teh por pera yt ne trevojili i on celyj den provodik odin naverhy v svoei comnate'))                 
   

    print("Decrypted Text")

    print(decrypt('klic', 'kcbgw'))                   
    
input()