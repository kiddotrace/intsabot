from re import I


targets = []
port = 7951

with open('targets.txt') as file:
    data = file.read().splitlines()

with open('proxies.txt') as file:
    proxy = file.read().splitlines()

with open('accounts.txt') as file:
    accounts = file.read().splitlines()


data_len = len(data)

for i in range(5):
    st = data[i].split(':')
    targets.append([st[0], f'http://{proxy[i]}'])


with open('targproxy.txt', 'w') as file:
    for i in targets:
        file.writelines(f'{i[0]} {i[1]}\n')
