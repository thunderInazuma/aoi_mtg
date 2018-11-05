from collections import Counter
import random
# 試行回数
num_iterations = 100000
# カードを引く枚数
cards_seen = 9
# デッキリスト
decklist = {
    'C':2, # 基本土地 その1
    'D':2, # 基本土地 その2
    'E':1, # 基本土地 その3
    'CD':8,# CD 2色土地
    'CE':8,# CE 2色土地
    'DE':4,# DE 2色土地
    'X':0, # 無色土地
    'S':35 # その他のカード 
    }
# デッキを作成する
deck = []
for card in decklist.keys():
    deck += [card] * decklist[card]
 
count = 0 
count_four_plus = 0
# 必要なカード枚数
need_land = 4 # 土地は最低でも4枚必要
c_need = 2 # 土地色その1は2枚必要
d_need = 2 # 土地色その2は2枚必要
for _ in range(num_iterations):
    # cards_seen枚のドローカードの中身
    draw = Counter(random.sample(deck, cards_seen))
    # 必要な土地を引けてるかどうか、引けたらカウントを増やす
    land = draw['C'] + draw['D'] + draw['E'] + draw['CD'] + draw['CE'] + draw['DE'] + draw['X']
    land_keep = need_land <= land
    count_four_plus += land_keep
    # CCDD の色と必要土地枚数が揃うかどうか、引けたらカウントを増やす
    c_color_keep = c_need <= (draw['C'] + draw['CD'] + draw['CE'])
    d_color_keep = d_need <= (draw['D'] + draw['CD'] + draw['DE'])
    count += (c_color_keep and d_color_keep and land_keep)

# デッキリストを出力
print('decklist:'+str(decklist))
# CCDDクリーチャーを唱えられる確率
print('fraction of draws with CCDD:\t' + str(round(count / num_iterations,3)))
# 土地を4枚引く確率
print('4 if more lands:            \t' + str(round(count_four_plus / num_iterations,3)))
# 土地が4枚揃ったときにCCDDが唱えられる確率
print('CCDD giben 4 or more lands: \t' + str(round(count / count_four_plus,3)))

