from collections import Counter
import random

# 試行回数
num_iterations = 100000
# カードを引く枚数
cards_seen = 9
# デッキリスト
decklist = {
    'C':9,# 基本土地 その1
    'D':8,# 基本土地 その2
    'X':0,# CD 2色土地
    'S':23# その他のカード
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
    # CCDD の色と必要土地枚数が揃うかどうか、引けたらカウントを増やす
    count += (min(draw['C'], c_need) + min(draw['D'], d_need) + draw['X'] >= need_land)
    # 必要な土地を引けてるかどうか、引けたらカウントを増やす
    count_four_plus += (draw['C'] + draw['D'] + draw['X'] >= need_land)

# デッキリストを出力
print(decklist)
# CCDDクリーチャーを唱えられる確率
print('fraction of draws with CCDD:\t' + str(round(count / num_iterations,3)))
# 土地を4枚引く確率
print('4 if more lands:            \t' + str(round(count_four_plus / num_iterations,3)))
# 土地が4枚揃ったときにCCDDが唱えられる確率
print('CCDD giben 4 or more lands: \t' + str(round(count / count_four_plus,3)))

