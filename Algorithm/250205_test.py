from datetime import datetime

start = datetime.now()
x = 0
for i in range(10**8):
    x += i
end = datetime.now()
print((end-start))