import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("questions_base.json", "r", encoding="utf-8") as f:
    qs = json.load(f)

print(f"Total questions loaded: {len(qs)}")
# Let's verify each module's range
for m_id in range(1, 14):
    m_qs = [q for q in qs if q['module_id'] == m_id]
    print(f"Module {m_id}: questions {m_qs[0]['id']} -> {m_qs[-1]['id']} (count: {len(m_qs)})")
