import re

pattern = re.compile(r'[ㄱ-ㅣ가-힣]')
results = re.findall(pattern, '')

print(results)