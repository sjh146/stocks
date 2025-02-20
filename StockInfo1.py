# matplotlib rebuild
import matplotlib as mpl
# mpl.font_manager._rebuild()

# matplotlib 환경 설정
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Nanum Pen Script" 
plt.rcParams["font.size"] = 15 
plt.rcParams["axes.grid"] = True
plt.rcParams["figure.figsize"] = (12,6)
# plt.rcParams["axes.formatter.useoffset"] = False
# plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams["axes.formatter.limits"] = -10000, 10000
import numpy as np
import FinanceDataReader as fdr
import pandas as pd

stock_list = [
  ["삼성전자", "005930"],
  ["SK하이닉스", "000660"],
  ["현대차", "005380"],
  ["셀트리온", "068270"],
  ["LG화학", "051910"],
  ["POSCO", "005490"],
  ["삼성물산", "028260"],
  ["NAVER", "035420"],
]


df_list = [fdr.DataReader(code, '2024-01-01', '2024-02-04')['Close'] for name, code in stock_list]
# print(len(df_list))
# print(df_list)

# pd.concat()로 합치기

df = pd.concat(df_list, axis=1)
# print(df.head(10))

df.columns = [name for name, code in stock_list] 
# print(df.head(10))

df.plot()
plt.show()

# # https://umaking.tistory.com/101 차트 그리기전 설치

# 싸인곡선그리기
# x = np.linspace(0, 20, 100)
# plt.plot(x, np.sin(x))
# plt.show()

print ('설정파일 위치: ', mpl.matplotlib_fname())
# 설정파일 위치:  C:\Python39\lib\site-packages\matplotlib\mpl-data\matplotlibrc
# https://geniekj.blogspot.com/2019/11/vscode-python.html   폰트 설정
#font.family:  sans-serif
# https://codedragon.tistory.com/7748 폰트 바꾸기
