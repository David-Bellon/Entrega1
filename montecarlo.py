from random import randrange as rd

variables = ["salary", "location", "conditions", "travels", "schedule"]
weight = [0.6, 0.7, 0.4, 0.4, 0.7]
grade1 = [[4,9],[8,10],[5,9],[8,9],[3,7]]

final_results = []

def montecarlo(grades):
    for i in range(10000):
        results = []
        for j in range(4):
            value = weight[j] * rd(grades[j][0], grades[j][1])
            results.append(value)

        final_results.append(sum(results))

if __name__ == "__main__":
    montecarlo(grade1)
    for i in range(len(final_results)):
        print(final_results[i])