# -*- coding: utf-8 -*-
"""
Script to build the full enriched database with translations and explanations for all 260 questions.
"""
import json
import re

with open("questions_base.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} base questions.")
