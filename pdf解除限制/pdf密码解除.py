import subprocess
import os
def hello():
    path = r"D:\python练习\qpdf"
    pre = r"C:\Users\Administrator\Desktop\09面试题"  # 初始pdf文件夹
    files = get_file_list(pre)
    print(files)
    for j in files:
        out_file = j + "2"
        cmd = ["qpdf", "--decrypt", j, out_file]  # 命令行终端命令
        sub = subprocess.Popen(args=cmd, cwd=path, shell=True)  # 不要忘记cwd
        sub.wait()  # 最好加上，否则可能由于多个进程同时执行带来机器瘫痪
    for j in files:
        out_file = j + "2"
        os.remove(j)  # 删除源文件
        portion = os.path.splitext(out_file)  # 分离文件名与扩展名
        if portion[1] == '.pdf2':
            # 重新组合文件名和后缀名
            newname = portion[0] + '.pdf'
            os.rename(out_file, newname)

def get_file_list(dir_path):
    filelists = list()
    for home, dirs, files in os.walk(dir_path):
        if len(files):
            for file in files:
                if str(file).endswith(r".pdf"):
                    # filelists.append(file)
                    realpath = os.path.join(home, file) # 获取绝对路径
                    filelists.append(realpath)
    return filelists

if __name__ == '__main__':
    hello()
