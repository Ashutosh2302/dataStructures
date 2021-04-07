#competitive coding problem
def minRewards(scores):
    rewards = [1 for _ in scores]
    index = scores.index(min(scores))
    c = 0
    while c == 0:
        z = 0
        for i in range(len(scores) - 1, index, -1):
            if scores[i] < scores[i - 1]:
                if rewards[i] >= rewards[i - 1]:
                    rewards[i - 1] += 1
                    z += 1
            else:
                if rewards[i] <= rewards[i - 1]:
                    rewards[i] += 1
                    z += 1
        if z == 0:
            c = 1

    c = 0
    while c == 0:
        z = 0
        for i in range(index):
            if scores[i] > scores[i + 1]:
                if rewards[i] <= rewards[i + 1]:
                    rewards[i] += 1
                    z += 1
            else:
                if rewards[i] >= rewards[i + 1]:
                    rewards[i + 1] += 1
                    z += 1
        if z == 0:
            c = 1
    return sum(rewards)

