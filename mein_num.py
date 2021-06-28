import num_print_list
import numpy as np
import erase_num_logic
import into_number
import copy

confirm_num = [0 for i in range(81)]
in_num = [[True for i in range(9)] for j in range(81)]
block_group =[
[[0,9,18,27,36,45,54,63,72],[1,10,19,28,37,46,55,64,73],[2,11,20,29,38,47,56,65,74],[3,12,21,30,39,48,57,66,75],[4,13,22,31,40,49,58,67,76],[5,14,23,32,41,50,59,68,77],[6,15,24,33,42,51,60,69,78],[7,16,25,34,43,52,61,70,79],[8,17,26,35,44,53,62,71,80]],
[[0,1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16,17],[18,19,20,21,22,23,24,25,26],[27,28,29,30,31,32,33,34,35],[36,37,38,39,40,41,42,43,44],[45,46,47,48,49,50,51,52,53],[54,55,56,57,58,59,60,61,62],[63,64,65,66,67,68,69,70,71],[72,73,74,75,76,77,78,79,80]],
[[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]
]

# 入力フォーム
confirm_num = into_number.in_number_input(confirm_num)

# 確認用の配列作成
block_group_num = [[0 for i in range(3)] for j in range(81)]
for index1,num1 in enumerate(block_group):
    for index2,num2 in enumerate(num1):
        for index3,data in enumerate(num2):
            block_group_num[data][index1] = index2

a = 0 
#loop作って繰り返し確認して、前回と同じ内容だったら終わり、もしくは全て確定した終わり、を作る
while True:
    a += 1
    print(str(a) + "回目\n" + "候補数字") 
    in_num_copy = copy.deepcopy(in_num)
    in_num = erase_num_logic.erase_num(confirm_num,block_group_num,block_group,in_num)

    num_print_list.pr_list(in_num)
    print("\n\n確定数字\n↓")
    num_print_list.pr_con_list(confirm_num)
    print(str(a) + "回目終了　enterを押すと再度検証を開始します。") 
    input()

    #ここで、入る数字があと一つだったら確定に入れる処理
    for index,i_num in enumerate(in_num):
        if i_num.count(True) == 1:
            for i, x in enumerate(i_num):
                if x == True:
                    confirm_num[index] = i + 1

    #ここで、in_numの数字がグループ内で単独かどうか確認
    for index1,num1 in enumerate(block_group):
        for index2,num2 in enumerate(num1):
            check_num = [0 for i in range(9)]
            kari_con_num = [0 for i in range(9)]
            for index3,data in enumerate(num2):
                for i in range(9):
                    if in_num[data][i] == True:
                        check_num[i] += 1
                        kari_con_num[i] = data

            for i in range(9):
                if (check_num[i] == 1) & (not  confirm_num[kari_con_num[i]] == i + 1):
                    confirm_num[kari_con_num[i]] = i + 1
# ここに、高等テクニックをコード化して入れるとクリアできる確率が上がりますが、
# 未完成です・・・。
    if in_num_copy ==  in_num:
        break

print("これ以上消せないので終了です。")