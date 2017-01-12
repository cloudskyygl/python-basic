# -*- coding: utf-8 -*-

# 将下面 dict 显示在表格中
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }

def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
trs = [generate_tr(name, score) for name, score in d.items()]
print '<table>'
print '<tr><td>name</td><td>score</td></tr>'
print '\n'.join(trs)
print '</table>'

# 请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，
# 非字符串元素将被忽略。
def toUppers(L):
    return [s.upper() for s in L if isinstance(s, str)]

print toUppers(['Hello', 'world', 101])
