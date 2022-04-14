# 匯入 matplotlib 的 pyplot 類別，並設定為 plt
import matplotlib.pyplot as plt
import numpy as np
import xlrd
import xlwt

"""
test 20220414
"""


# 要顯示中文 需要打這兩行還行
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False      # （解決座標軸負數的負號顯示問題）

# 圖表樣式
style = ["r--", "b--", "g--", "y--"]
styleColor = ["red", "blue", "green", "yellow"]
styleStem = ["ro", "bo", "go", "yo"]


# 初始設定
read = xlrd.open_workbook("covid19.xls")
sheet = read.sheets()[0]


# 取得資料裡的城市姓名
def dataNameRead(n, sheet):
    list1 = []
    for y in range(1, sheet.ncols):     # 第一筆的資料 略過日期那行
        data = sheet.cell(n, y).value
        list1.append(data)
    return list1


cityName = dataNameRead(0, sheet)   # (看要取第幾筆的變數,資料的分頁)


# 取得資料裡的日期
def dayRead(sheet, n):
    list1 = []
    for x in range(1, sheet.nrows):     # 取得 第一欄的資料 略過 最上面的日期名稱
        data = sheet.cell(x, n).value
        list1.append(data)
    return list1


day = dayRead(sheet, 0)             # (資料的分頁,看要 取哪欄 的變數)


# 取得資料裡的各縣市確診人數
def cityNumRead(sheet):         # 取得所有的城市資料
    list1 = {}      # 空字典變數
    for n in range(1, sheet.ncols):     # 略過 第一欄的日期 從1開始 不能從0
        list2 = []      # 空list變數
        for x in range(1, sheet.nrows):     # 略過第一行的各縣市名稱 從1開始 不能從0
            data = sheet.cell(x, n).value
            list2.append(data)

        list1[n-1] = list2     # 把取出來的資料 存入 字典DIC 裡 n-1 是因為我們從1開始跑 所以要-1

    return list1


cityNum = cityNumRead(sheet)    # (資料分頁)


def event1():
    print("NOTHING")




# ----------------------------------------------
fig, pic = plt.subplots(2, 3)       # 設置上下各三個圖
# 圖1 plot
for x in range(0, len(cityName)):
    # x y 名稱
    pic[0, 0].plot(day, cityNum[x], style[x], label=cityName[x])
pic[0, 0].legend()

# plt.legend(loc="upper left")            # 改變顯示名稱位置
# 'upper left', 'upper right', 'lower left', 'lower right

# 2.柱狀圖
x = np.arange(len(day))  # label 位置
width = 1  # 柱體寬度
for i in range(0, len(cityName)):
    # x y 寬 名稱    x 部分 是要讓柱體不要重疊,利用所有的 cityName 來平均x位置
    pic[0, 1].bar(x + i/len(cityName), cityNum[i], width/len(cityName), label=cityName[i])

pic[0, 1].set_xticks(x, day)
pic[0, 1].legend(loc="upper left")

# 3.躺的柱狀圖
x = np.arange(len(day))     # label 位置
width = 1       # 柱體寬度
for i in range(0, len(cityName)):
    # y x 寬 名稱    y 部分 是要讓柱體不要重疊,利用所有的 cityName 來平均y位置
    pic[0, 2].barh(x + i/len(cityName), cityNum[i], width/len(cityName), label=cityName[i])
pic[0, 2].set_yticks(x, labels=day)
pic[0, 2].legend()


# 4.階梯圖
x = np.arange(len(day))     # label 位置
for i in range(0, len(cityName)):
    #  x y 名字 x 部分 是要讓柱體不要重疊,利用所有的 cityName 來平均x位置
    pic[1, 0].step(x+(i/len(day)), cityNum[i], label=cityName[i])
pic[1, 0].set_xticks(x, labels=day)
pic[1, 0].legend()

# 5.填充多邊形
for i in range(0, len(cityName)):
    # x y 名稱
    pic[1, 1].fill(day, cityNum[i], label=cityName[i])
pic[1, 1].legend(loc="upper left")

# 6.stem plot
x = np.arange(len(day))
for i in range(0, len(cityName)):
    # x y 線的顏色 頭頂樣式 名稱    x 部分 是要讓柱體不要重疊,利用所有的 cityName 來平均x位置
    pic[1, 2].stem(x+i/len(cityName), cityNum[i], linefmt=styleColor[i], markerfmt=styleStem[i], label=cityName[i])
pic[1, 2].legend()
pic[1, 2].set_xticks(x, labels=day)

plt.show()                  # 繪製
