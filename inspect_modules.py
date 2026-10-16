import json

with open("questions_base.json", "r", encoding="utf-8") as f:
    qs = json.load(f)

for m in range(1, 14):
    m_qs = [q for q in qs if q['module_id'] == m]
    print(f"\n--- Module {m}: {len(m_qs)} questions ---")
    for q in m_qs[:2]:
        print(f"Q{q['id']}: {q['prompt'][:80]}... Ans: {q['answer']}")
