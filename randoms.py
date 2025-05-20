import random

random_float = random.random()
print(f"Random float between 0.0 and 1.0: {random_float}")


# Simple float 0.0 <= x < 1.0: random.random()
# Float in a specific range a <= x <= b: random.uniform(a, b)
# Integer in a specific range a <= x <= b (inclusive): random.randint(a, b)
# Integer from a range(start, stop, step): random.randrange(start, stop, step)
# Random item from a sequence: random.choice(sequence)
# Multiple items with replacement (possibly weighted): random.choices(population, k, weights)
# Multiple unique items without replacement: random.sample(population, k)
# Shuffle a list in place: random.shuffle(my_list)
# Reproducibility: random.seed()