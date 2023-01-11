def maior(* num):
    mai = count = 0
    for v in num:
        count += 1
        if count == 0:
            mai = v
        else:
            if v > mai:
                mai = v
    print('¬' * 70)
    print(f'O maior número entre os {num} valores foi {mai}')
    print(f'No total foram {count} valores')
    print('¬' * 70)


#__main__:
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
