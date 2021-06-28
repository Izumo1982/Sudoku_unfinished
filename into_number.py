# データを入力するメソッド
def in_number_input(confirm_num):
    for i in range(9):
        print(str(i + 1) + "行目は？")
        inp = input()
        if inp == "":
            inp = str(i + 1) + "00000000"

        for j in range(9):
            confirm_num[i * 9 + j] = int(inp[j:(j + 1)])
    return confirm_num
