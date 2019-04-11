from boom.boom import load, calc_stats

url='http://192.168.56.30'
min_concurrency=1
max_concurrency=1501
step = 100

concurrency=min_concurrency
requests=0

print("Concurrency, avg, rps")

while(concurrency<max_concurrency):
    r=load(url, 5000, concurrency,0, 'GET', None, 'text/plain', None, quiet=True)
    s=calc_stats(r)
    print("{}, {}, {}".format(concurrency, s.avg, s.rps))
    concurrency = concurrency + step
    requests +=s.count

print(requests)
