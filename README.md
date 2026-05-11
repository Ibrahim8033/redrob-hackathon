# Redrob AI Campus Hackathon — Resume Matching Engine

A Python-based Resume Matching Engine built for the Redrob AI Campus Hackathon.

## Features

* Skill normalization using predefined aliases
* Resume skill deduplication
* TF-IDF vector generation
* Binary vector generation for Job Descriptions
* Cosine similarity calculation
* Top 3 candidate ranking per JD
* Alphabetical tie-breaking
* Pure Python implementation (No external libraries)

---

## Tech Stack

* Python 3
* Standard Python Libraries

  * math

---

## Project Workflow

1. Normalize noisy resume skills
2. Deduplicate normalized skills
3. Build shared vocabulary
4. Compute TF-IDF vectors manually
5. Create binary JD vectors
6. Compute cosine similarity
7. Rank top matching candidates

---

## Dataset

### Resumes

* 10 Candidate Resume Skill Datasets

### Job Descriptions

* Kakao — ML Engineer
* Naver — Backend Engineer
* Line — Frontend Engineer

---

## How to Run

```bash
python3 hackathon.py
```

---

## Output Format

```text
JD-1 — Kakao (ML Engineer)
Candidate Name (score)

JD-2 — Naver (Backend Engineer)
Candidate Name (score)

JD-3 — Line (Frontend Engineer)
Candidate Name (score)
```

---

## Hackathon Rules Followed

* No external libraries used
* Manual TF-IDF implementation
* Manual cosine similarity implementation
* Exact SKILL_ALIASES mapping used
* Vocabulary generated only from resumes

---

## Author

MD Ibrahim Khan

Built using Redrob AI-assisted workflow with manual validation and debugging.
