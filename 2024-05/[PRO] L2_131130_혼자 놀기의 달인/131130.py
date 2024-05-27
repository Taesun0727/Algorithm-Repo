global_cards = []
global_check = []
global_count = []

def find_box(cur, arr):
    global global_count
    if len(arr) > 0 and cur == arr[0]:
        global_count.append(len(arr))
        return
    if global_check[global_cards[cur]]:
        tmp = global_cards[cur]
        global_check[tmp] = False
        find_box(global_cards[cur], arr + [cur])

def solution(cards):
    global global_cards, global_check, global_count
    global_cards = [0] + cards
    global_check = [True] * len(global_cards)

    for i in range(1, len(global_cards)):
        if global_check[i]:
            find_box(i, [])
    global_count.sort(reverse=True)

    if len(global_count) < 2:
        answer = 0
    else:
        answer = global_count[0] * global_count[1]

    return answer