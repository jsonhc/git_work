def consumer():
  r = ''
  while True:
    n = yield r
    print(r)
    if not n:
      print(n)
      return 
    print('[CONSUMER] Consuming %s...' % n)
    r = '200 OK'


def produce(c):
  f = c.send(None)
  print('[PRODUCER] Consumer first return: %s' % f)
  n = 0
  while n < 2:
    n = n + 1
    print('[PRODUCER] Producing %s...' % n)
    r = c.send(n)
    print('[PRODUCER] Consumer return: %s' % r)
  c.close()

c = consumer()
produce(c)
