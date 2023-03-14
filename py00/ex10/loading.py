from time import sleep
import datetime

def ft_progress(lst):
	eta = 0
	total = 0
	start = datetime.datetime.now();
	per = 0
	prog = 0
	for elem in lst:
		now = datetime.datetime.now();
		print (f'\rETA: {eta:0.2f} [{per:0.2f}%][', '=' * (int)(prog),
        '>',  ' ' * (int)(30 - prog),f']{total}/{len(lst)} | elapsed time {(now - start).total_seconds():0.2f}', flush=True, end='', sep='')
		prog = (total / len(lst)) * 30
		per = (total / len(lst)) * 100
		eta = (len(lst) - total) * (total / (now - start).total_seconds()) / 10000
		total += 1
		yield (int)(prog)
	print('\n...')

if __name__ == "__main__":
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.005)
    print(ret)