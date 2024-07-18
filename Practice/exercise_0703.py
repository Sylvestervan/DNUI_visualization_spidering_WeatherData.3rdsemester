# import os
#
# def rename_html_files(dir_path):
#     for file_name in os.listdir(dir_path):
#         file_path = os.path.join(dir_path, file_name)
#         if file_name.endswith('.html'):
#             new_file_name = file_name.replace('.html', '.htm')
#             new_file_path = os.path.join(dir_path, new_file_name)
#             os.rename(file_path, new_file_path)
#             print(f'Renamed {file_name} to {new_file_name}')
#
# # 目录路径
# rename_html_files('/Users/fanjindong/Desktop/Python Lecture/homework4')

# f1 = open('file1.txt', 'r')
# res = f1.readlines()
# print(res)
# f1.close()

# s = 'Hello, world.\n文本文件的读取方法\n文本文件的写入方法\n'
#
# with open('sample.txt', 'w') as fp:
#     fp.write(s)
#
# with open('sample.txt') as fp:
#     print(fp.read())
#
# with open('sample.txt') as fp:
#     for line in fp:
#         print(line)

# with open("test_01.txt", "r") as file:
#     for line in file:
#         cleaned_line = line.strip()
#         if not cleaned_line.startswith("#"):
#             print(cleaned_line)
#
# var = [fname for fname in os.listdir(os.getcwd()) if os.path.isfile(fname) and fname.endswith('.dll')]
# print(var)