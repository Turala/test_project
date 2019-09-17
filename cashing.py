def cashing(check):
    results = []
    def check_out(*args, **kwargs):
        if args not in result:
            results[args] = check(*args)
        if kwargs not in result:
            results[kwargs] = check(**kwargs)
        results = results.add[results[args]]
        results = results.add[results[kwargs]]
    return results

@cashing
def print_params(*args, **kwargs):
    if kwargs:
        for k, v in kwargs.items():
            print(k, v)
    if args:
        for a in args:
            print(a)

print_params(12, 13, a = 14, b = 15, c = 4000)
