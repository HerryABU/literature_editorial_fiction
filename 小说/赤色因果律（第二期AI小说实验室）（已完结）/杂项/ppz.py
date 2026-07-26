import re

# ===== 在这里修改你的文件路径 =====
INPUT_FILE = 'csygl2.md'      # 输入文件
OUTPUT_FILE = 'output.md'    # 输出文件
# =================================

# 读取文件
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# 删除 ==== 包裹的内容
result = re.sub(r'====\n.*?\n====\n?', '', content, flags=re.DOTALL)

# 写入文件
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(result)

print(f"处理完成！{INPUT_FILE} -> {OUTPUT_FILE}")