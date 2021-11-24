import os

def print_file_in_dir(root_dir, prefix):
    files = os.listdir(root_dir)
    for file in files:
        path = os.path.join(root_dir, file)
        print(prefix + path)
        if os.path.isdir(path):
            print_file_in_dir(path,"")



if __name__=="__main__":
    root_dir ="C:/Users/LDCC/Documents/javaProject"
    print("--------------------------------")
    print_file_in_dir(root_dir, "")
