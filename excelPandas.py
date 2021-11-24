import pandas as pd
import openpyxl

raw_data = {'col0' : [1, 2, 3, 4],
              'col1' : [10, 20, 30, 40],
              'col2' : [100, 200, 300, 400]} #리스트 자료형으로 생성
raw_data = pd.DataFrame(raw_data) #데이터 프레임으로 전환
print(raw_data)
raw_data.to_excel("C:/Users/LDCC/Documents/testExcel/sample.xlsx") #엑셀로 저장