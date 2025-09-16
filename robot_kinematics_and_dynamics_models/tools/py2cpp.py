#!/usr/bin/env python3
import re, sys, textwrap

PY = open(sys.argv[1]).read()
FUNC = sys.argv[2]
OUT  = sys.argv[3]

# 1. 提取函数体
body = re.search(rf'def {FUNC}.*?\n(.*?)return', PY, re.S).group(1)

# 2. 简单替换
cpp = re.sub(r'np\.sin', 'std::sin', body)
cpp = re.sub(r'np\.cos', 'std::cos', cpp)
cpp = re.sub(r'np\.sign', 'sign', cpp)
cpp = re.sub(r'([xyz]\d+)\s*=\s*(.+)', r'double \1 = \2;', cpp)
cpp = re.sub(r'H\[(\d+)\]\s*=\s*(.+)', r'H[\1] = \2;', cpp)

# 3. 保存
open(OUT, 'w').write(cpp)