def consumer():
  r = ''
  while True:
    n = yield r
    if not n:
      return 
    print('[CONSUMER] Consuming %s.... ' % n)
    r = '200 OK'

def produce(c):
  f = c.send(None)
  print('f is %s' % f)
  n = 0
  while n < 2:
    n = n + 1
    print('[PRODUCE] Producing %s ....' % n)
    r = c.send(n)
    print('[PRODUCE] Consumer return %s ...' % r)
  c.close()


c = consumer()
produce(c)
