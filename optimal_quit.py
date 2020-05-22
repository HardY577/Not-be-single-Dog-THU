# -*- coding: utf-8 -*-
'''
@Author  :  HardY
@Date    : 2020/5/22
'''

import random
import matplotlib.pyplot as plt
import numpy as np

N = 21


def optimal_quit(n) -> float:
	"""
	利用毕导给出的P(k)的公式求出每个不同的k对应的P，再返回最大值P
	:param n: 候选者人数
	:return: 最大概率P
	"""
	p = []
	for k in range(1, n+1):
		temp = (k * sum([(1 / i) for i in range(k, n)])) / n
		p.append(temp)
	return max(p)


def main():
	p = [1.0]  # 最佳概率
	num = [0]  # 最佳策略k
	print('候选者人数\t', '最佳策略k\t', '最佳概率\n')
	# 对不同的候选者人数分别求取最佳策略和最佳概率
	for n in range(2, N):
		p.append(optimal_quit(n))
		temp = (int)(p[n - 3] * n) + 1
		num.append(temp)
		print(n, '\t\t\t', num[n - 3], '\t\t\t', p[n - 3])

	# li = random.sample(range(0, 100), 100)  # 在0-100内随机生成一个序列，表示100个候选人和位置信息
	# print(li)

	ranchoose_p = []  # 随机选择选到最优者的概率
	for i in range(1, N):
		a = 1 / i
		ranchoose_p.append(a)

	# 画图
	x = np.arange(0, len(p)) + 1
	x[0] = 1
	my_x_ticks = np.arange(1, N, 1)
	plt.xticks(my_x_ticks)
	plt.plot(x, p, color='red')
	plt.plot(x, ranchoose_p, color='green')
	plt.xlabel('Candidates')
	plt.ylabel('Optimal probability')
	plt.legend(['37%', 'random'], loc='best')
	plt.show()


if __name__ == '__main__':
	main()