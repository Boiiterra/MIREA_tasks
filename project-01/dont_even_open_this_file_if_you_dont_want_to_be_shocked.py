import string

# +----------------------------+
# |                            |
# | Тут коментарии не нужны :P |
# |                            |
# +----------------------------+


def dead_zone():
    """НЕ НАДО ЭТО ЧИТАТЬ"""

    while True:
        print("Введите значение один")
        znach1 = input()
        if znach1 == "A16-KARPOV":  # Мы его очень любим <3
            return True
        print("Введите значение два")
        znach2 = str(input())
        print(
            "Введите тип операции\n"
            "1 - Сложение\n"
            "2 - Вычитание\n"
            "3 - Деление\n"
            "4 - Умножение\n"
            "5 - Косинус значения 1\n"
            "6 - Синус значения 1\n"
            "7 - Возведение в стпень число один, что будет возводить, два в какую степень\n"
            "8 - Корень числа"
        )
        operation = int(input())
        print("Введите начальньную СС")
        nach_ss = int(input())
        print("Введите финальную СС")
        fin_ss = int(input())
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabet = alphabet.strip()
        OTR_ZN_1 = 0
        OTR_ZN_2 = 0
        perch_1 = ""
        perch_2 = ""
        back_1 = ""
        back_2 = ""
        str(back_1)
        str(back_2)
        ADRESS_TCHK_1 = 0
        ADRESS_TCHK_2 = 0
        ADR_C1 = 0
        ADR_C2 = 0
        nr1 = ""
        nr1 = znach1
        nr2 = ""
        nr2 = znach2
        if znach1[0] == "-":
            znach1 = znach1[1:]
            OTR_ZN_1 += 1
            print(znach1)
        if znach2[0] == "-":
            znach2 = znach2[1:]
            OTR_ZN_2 += 1
            print(znach2)
        if znach1.find(".") == True:
            ADRESS_TCHK_1 = znach1.find(".")
            ADR_C1 += 1
        if znach2.find(".") == True:
            ADRESS_TCHK_2 = znach1.find(".")
            ADR_C2 += 1
        dli_1 = len(znach1) // 2
        znach1.split(".")
        perch_1 = znach1[:dli_1]
        back_1 = znach1[dli_1:]
        back_1 = back_1.translate(str.maketrans("", "", string.punctuation))

        ADRESS_TCHK_2 = znach2.find(".")
        dli_2 = len(znach2) // 2
        znach2.split(".")
        perch_2 = znach2[:dli_2]
        back_2 = znach2[dli_2:]
        back_2 = back_2.translate(str.maketrans("", "", string.punctuation))

        GG = 0  # Это для теста
        if operation < 9:
            GG += 1
        else:
            print("OPERATION NOT FOUND | Давай по новой")

        if ADR_C1 == 1:
            CONT1 = 0
            for i in range(0, len(perch_1)):
                if perch_1[i] in alphabet[0:nach_ss]:
                    CONT1 += 1
            for i in range(0, len(back_1)):
                if back_1[i] in alphabet[0:nach_ss]:
                    CONT1 += 1
        else:
            CONT1 = 0
            if nr1 in alphabet[0:nach_ss]:
                CONT1 += 2
        #                print('CONT1 =', CONT1)
        if operation != 5 or operation != 6 or operation != 7 or operation != 8:
            if ADR_C2 == 1:
                CONT2 = 0
                for i in range(0, len(perch_2)):
                    if perch_2[i] in alphabet[0:nach_ss]:
                        CONT2 += 1
                for i in range(0, len(back_2)):
                    if back_2[i] in alphabet[0:nach_ss]:
                        CONT2 += 1
            else:
                CONT2 = 0
                if nr2 in alphabet[0:nach_ss]:
                    CONT2 += 2
        if operation == 5 or operation == 6 or operation == 7 or operation == 8:
            #            print('Зашли в недопутимый иф')
            if CONT1 == 2:
                CHEK1 = True
            else:
                CHEK1 = False
                print("CC Числа 1 не соответсвует числу")
                dead_zone()
        else:
            if CONT1 == 2:
                CHEK1 = True
            else:
                CHEK1 = False
                print("CC Числа 1 не соответсвует числу")
                dead_zone()
            if CONT2 == 2:
                CHEK = True
            else:
                CHEK = False
                print("CC Числа 2 не соответсвует числу")
                dead_zone()
        if CHEK1 == True or CHEK1 == True and CHEK == True:
            # Преобразователь в нормальное значение
            if ADR_C1 == 1:
                znach1 = perch_1 + "." + back_1
            else:
                znach1 = nr1
            if ADR_C2 == 1:
                znach2 = perch_2 + "." + back_2
            else:
                znach2 = nr2
                print(znach1, znach2)
            if operation == 1:
                GG += 1
                # Вызов сложения
            elif operation == 2:
                GG += 1
                # Вызов вычитания
            elif operation == 3:
                GG += 1
                # Вызов деления
            elif operation == 4:
                GG += 1
                # Вызов умножения
            elif operation == 5:
                GG += 1
                # Вызов косинус занчения 1
            elif operation == 6:
                GG += 1
                # Вызов синус занчения 1
            elif operation == 7:
                GG += 1
                # Вызов возведение в степень
            elif operation == 8:
                GG += 1
                # Вызов корня
            # Кусок кода с вычислениями и переводом в финальныую СС
            # Ну или можно под элифы запихать все манипуляции
            # от разработчик номер два

            # Лень, разработчик номер один
