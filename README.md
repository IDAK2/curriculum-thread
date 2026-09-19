# Curriculum Thread

Curriculum Thread is a credit-transfer primitive that treats equivalence as an auditable mapping rather than an opaque yes/no decision.

## What is frozen

At request time, the contract stores the applicant, receiving institution, course, declared learning outcomes, and two syllabus URLs from different origins. The receiving institution—not the applicant—triggers mapping.

## What consensus produces

Validators fetch both syllabi and independently return three bounded collections:

1. matched outcome indexes;
2. missing outcome indexes;
3. prerequisite statements.

The source bytes are hashed and retained. The seven-day objection window begins at `mapped_at`, never at request creation. The applicant may attach an HTTPS objection record; otherwise anyone may finalize only after the window expires.

## Verification

`pytest -q` exercises the successful map, role separation, and objection path. `ruff check contracts tests` checks the source surface. Deployment receipts and live transaction hashes are recorded in `deployment.json`.

The illustrated website deliberately follows a woven-outcome metaphor. It is a public explainer and read path; contract state remains the authority.
