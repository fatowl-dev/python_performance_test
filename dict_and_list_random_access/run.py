# list、dict ランダムアクセス速度比較
import random
import string
import gc

N = 100             # 試行回数
REF_COUNT = 100000  # 1回の試行で参照する回数 
ITEM_COUNT = 100    # アイテム数
KEY_LENGTH = 32     # 辞書のキーの長さ 
SLEEP_TIME = 0.1    # 試行前の待ち時間（なぜかこれを入れないとおかしな値になる)

list_results = []
dict_results = []

# 辞書のキーを作成する
keys = []
for i in range(ITEM_COUNT):
    while True:
        randlist = [random.choice(string.ascii_letters + string.digits) for i in range(KEY_LENGTH)]
        key = ''.join(randlist)
        if key not in keys:
            keys.append(key)
            break 

# リストを作成
item_list = [ i for i in range(ITEM_COUNT)]

# 辞書を作成
item_dict = {keys[i]: i for i in range(ITEM_COUNT)}

print('--------------------------------------')
print('テスト開始')
print('--------------------------------------')
print(f'試行回数: {N}回')
print(f'参照回数: {REF_COUNT}回')
print(f'辞書のキーの長さ: {KEY_LENGTH}文字')
print(f'要素数: {ITEM_COUNT}個')

for count in range(N):
    print('\n--------------------------------------')
    print(f'{count+1}回目')
    print('--------------------------------------')

    # ゴミ掃除
    gc.collect()

    # 何故かこのスリープを入れないとおかしな値になる
    time.sleep(SLEEP_TIME)
    
    # ランダムアクセスのインデックスリストを作成
    rand_indexes = [random.randrange(0, ITEM_COUNT) for i in range(REF_COUNT)]

    # ランダムアクセスのキーリストを作成
    rand_keys = [keys[n] for n in rand_indexes]

    # list
    start_time = time.time() 
    for i in rand_indexes:
        x = item_list[i] 
    end_time = time.time()
    elapsed_time = end_time - start_time
    list_results.append(elapsed_time)
    print(f'list: {elapsed_time}')

    # dict
    start_time = time.time() 
    for key in rand_keys:
        x = item_dict[key] 
    end_time = time.time()
    elapsed_time = end_time - start_time
    dict_results.append(elapsed_time)
    print(f'dict: {elapsed_time}')


print('\n--------------------------------------')
print('条件')
print('--------------------------------------')
print(f'試行回数: {N}回')
print(f'参照回数: {REF_COUNT}回')
print(f'辞書のキーの長さ: {KEY_LENGTH}文字')
print(f'要素数: {ITEM_COUNT}個')
print('\n--------------------------------------')
print('結果')
print('--------------------------------------')
print(f'list average: {sum(list_results) / len(list_results)}')
print(f'dict average: {sum(dict_results) / len(dict_results)}')


