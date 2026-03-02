import random



counts=0
while counts<10:
  answer=random.randint(1,100)

  a,b=map(int,input('给我两个数,记作a,b').split(','))
  sum_ab=a+b
  if sum_ab==answer:
      print('正正好好')
      counts=counts+5

  else:
      if answer+15>=sum_ab>=answer-15:
          print('稍微偏一点点')
          counts=counts+1

      else:
          print('差太多啦')
          counts=counts+0

print('自己查查多少轮才完成')


