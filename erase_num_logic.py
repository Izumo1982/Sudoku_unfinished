# 理論上数字が入らないマスから候補数字を消すメソッド
def erase_num(confirm_num,block_group_num,block_group,in_num):

    for index,con_num in enumerate(confirm_num):
        if not con_num == 0:
            for ind,bl in enumerate(block_group_num[index]):
                for block_num in block_group[ind][bl]:
                        in_num[block_num][con_num - 1] = False
            for ind, num in enumerate(in_num[index]):
                in_num[index][ind] = False
            in_num[index][con_num - 1] = True
    return in_num

