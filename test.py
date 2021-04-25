import pyupbit

access = "kB58cLN7xUXQuquyFDaac6l6gxwxLSmftuvRjGwS"          # 본인 값으로 변경
secret = "JGrlD1TV6KnVHNzR9nmIthIq3GOWGvD6xxjUgbqG"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회