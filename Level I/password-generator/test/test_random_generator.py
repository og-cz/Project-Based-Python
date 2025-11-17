def linear_random_generator(x0, a, b, m, n):
    results = []
    for _ in range(n):
        x0 = (a * x0 + b) % m
        results.append(x0)
    return results

#### TODO: NOT YET DONE...
def generate(length, seed=1234):
    import src.mesenne_twister as random
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbol = "!@#$%^&*()"
    
    random = random.Random()
    x0 = random.randint(1, 60)
    a = 151612
    b = 1231
    m = len(charset)
    n = length

    x = linear_random_generator(x0,a,b,m,n)
    result_string=''.join(charset[_] for _ in x)
    print(result_string)

generate(10)