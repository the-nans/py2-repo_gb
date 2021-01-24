s = input("Введите последовательность натуральных чисел")
buf = 0
prev_buf = 0
buf_num = ""
pb_num = ""
for i in s:
    if i.isdigit():
        buf += int(i)
        buf_num = f"{buf_num}{i}"
    else:
        if prev_buf < buf:
            prev_buf = buf
            pb_num = buf_num
        buf = 0
        buf_num = ''

if buf > prev_buf:
    print(f"{buf} сумма цифр числа {buf_num}")
else:
    print(f"{prev_buf} сумма цифр числа {pb_num}")