def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    have_deli = 0
    have_pick = 0

    for i in range(n):
        have_deli += deliveries[i]
        have_pick += pickups[i]

        while have_deli > 0 or have_pick > 0:
            have_deli -= cap
            have_pick -= cap
            answer += (n - i) * 2
    return answer