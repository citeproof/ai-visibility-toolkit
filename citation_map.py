import csv
import sys
from collections import Counter, defaultdict
from urllib.parse import urlparse

def domain(url):
    host = urlparse(url).netloc.lower()
    return host[4:] if host.startswith("www.") else host

counts = Counter()
by_engine = defaultdict(Counter)
questions = defaultdict(set)

with open(sys.argv[1], newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        d = domain(row["cited_url"])
        counts[d] += 1
        by_engine[row["engine"]][d] += 1
        questions[d].add(row["question"])

print(f"{'domain':35} {'cites':>5} {'questions':>9}  engines")
for d, n in counts.most_common(25):
    engines = ", ".join(e for e in by_engine if by_engine[e][d])
    print(f"{d:35} {n:>5} {len(questions[d]):>9}  {engines}")
