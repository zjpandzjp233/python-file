import timeit
import re
def count_keyword_in_file(file_path, keyword):
    keyword_regex = re.compile(re.escape(keyword))
    count = 0
    with open(file_path, "r", encoding="UTF-8") as file:
        for line in file:
            count += len(keyword_regex.findall(line))
    return count

def main():
    path = input("请先输入你需要统计关键词出现次数的文本路径:").strip()
    path =path.strip('"')
    
    target = input("请先输入你需要查找的文字，我将告诉其在文本出现的次数:").strip()

    start_time = timeit.default_timer()
    result = count_keyword_in_file(path, target)
    elapsed_time = timeit.default_timer() - start_time

    print(f"关键字: {target}")
    print(f"一共出现 {target} 关键字 {result} 次。")
    print(f"查找关键字的平均耗时：{elapsed_time:.10f} 秒")

if __name__ == "__main__":
    main()