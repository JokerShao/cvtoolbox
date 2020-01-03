import sys

sys.path.append('b')
from b import b#.b import funb
sys.path.pop(-1)
after_b = sys.modules.copy()


before_a = sys.modules.copy()
sys.path.append('a')
from a import a#.a import funa
sys.path.pop(-1)
after_a = sys.modules.copy()


differ_beforeaaftera = set(before_a.items()) ^ set(after_a.items())
print('\nafter import a:')
for diff in differ_beforeaaftera: print(diff)

differ_afteraafterb = set(after_a.items()) ^ set(after_b.items())
print('\nafter import b:')
for diff in differ_afteraafterb: print(diff)

differ_beforeaafterb = set(before_a.items()) ^ set(after_b.items())
print('\nafter import ab:')
for diff in differ_beforeaafterb: print(diff)


if __name__ == '__main__':
    a.funa()
    b.funb()

