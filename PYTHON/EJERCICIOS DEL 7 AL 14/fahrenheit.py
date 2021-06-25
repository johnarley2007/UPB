temperatura=0
print("ºF           ºC")
while temperatura < 21:
    celsius =((temperatura-32)*(5/9))
    print(temperatura,"           ", celsius)
    temperatura=temperatura+1

temperatura=0
print("ºF           ºC")
for temperatura in range(0,21):
    celsius =((temperatura-32)*(5/9))
    print(temperatura,"           ", celsius)