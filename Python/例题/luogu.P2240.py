n = int(input())
t = float(input())
lism = []
lisv = []
for i in range(n):
    m, v = float(input()), float(input())
    lism.append(m)
    lisv.append(v)

class P2240:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def calculate_weights(self):
        
        self.num = list(range(len(self.value)))
        self.weights = [self.value[i] / self.weight[i] for i in range(len(self.value))]
        for m in range(len(self.num) - 1):
            for j in range(len(self.num) - m - 1):
                if self.weights[j] < self.weights[j + 1]:
                    self.weights[j], self.weights[j + 1] = self.weights[j + 1], self.weights[j]
                    self.num[j], self.num[j + 1] = self.num[j + 1], self.num[j]

    def get_parcel(self):
        self.calculate_weights()
        total_weight = 0
        total_value = 0.00
        number = 0
        while number < len(self.num) and total_weight + self.weight[self.num[number]] <= t:
            total_weight += self.weight[self.num[number]]
            total_value += self.value[self.num[number]]
            number += 1
        
        if number < len(self.num) and total_weight < t:
            rest_space = t - total_weight
            total_value += self.value[self.num[number]] / self.weight[self.num[number]] * rest_space

        return round(total_value, 2)

p2240 = P2240(lism, lisv)
print(p2240.get_parcel())
