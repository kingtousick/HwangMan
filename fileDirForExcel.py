#지정한 폴더트리구조로 뽑은다음 엑셀로 저장한다.
import os
import pandas as pd
import openpyxl

def print_file_in_dir(root_dir, prefix):  #파일경로 목록
    files = os.listdir(root_dir)
    for file in files:
        path = os.path.join(root_dir, file)
        print(prefix + path[24:])
        if os.path.isdir(path):
            print_file_in_dir(path,"")
if __name__=="__main__":
    # root_dir ="C:/Users/LDCC/Documents/javaProject"
    root_dir = input("경로를 입력하세요 : ")
    print("input address : ", root_dir)
    root_dir.replace(f"\\", "/")
    print("convert address : ", root_dir)
    print("--------------------------------")
    print_file_in_dir(root_dir, "")
