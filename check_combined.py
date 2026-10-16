# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

from mod1_3 import DATA_MOD_1_3
from mod4_6 import DATA_MOD_4_6
from mod7_9 import DATA_MOD_7_9
from mod10_13 import DATA_MOD_10_13

combined = {}
combined.update(DATA_MOD_1_3)
combined.update(DATA_MOD_4_6)
combined.update(DATA_MOD_7_9)
combined.update(DATA_MOD_10_13)

print(f"Total defined questions in modules: {len(combined)}")

missing = [i for i in range(1, 261) if i not in combined]
print("Missing questions:", missing)
