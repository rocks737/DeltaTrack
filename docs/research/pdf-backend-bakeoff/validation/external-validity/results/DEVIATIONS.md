# Deviations

`PRE-REGISTRATION.md` section 11 register. Rows are appended **when they happen** and carry:
what changed old to new; when and at what stage; **whether results were already visible, and
which**; why; and which scores, rankings or gates it could move.

Section 4.7 governs the consequence: a change made after execution starts is a deviation, and
**every affected score is re-labelled non-confirmatory**. "Affected" means *value-dependent*,
not merely *enabled*. Labelling every result non-confirmatory because a repair made the
pipeline runnable at all would destroy the distinction the register exists to record.

The machine-readable form of this ruling is [`CONTINUATION.json`](CONTINUATION.json), which is
what the apparatus reads. This document is the reasoning; that file is the authority.

---

## A47 — POST-BOUNDARY CONTINUATION / DEVIATION RULING

```json
{"id": "A47", "kind": "POST-BOUNDARY CONTINUATION",
 "commits": ["9ce9b6e", "cc69fc5", "381c2f6", "abbe780", "8f28719", "5a33e19"],
 "prior_boundary_commit": "89360b30de480231efdc89157443779d45b37db2",
 "population_status": "EXPOSED",
 "results_already_visible": {
  "d_frame_census_regions": 13992,
  "s1_documents_firing": "17/17",
  "p_head_documents": 12,
  "p_head_pages": 2864,
  "frames": "17/17 members, 4190 pages"
 },
 "affects_membership": false,
 "affects_scoring_rule": false,
 "affects_metric_values": false,
 "affects_architecture_decision": false,
 "non_confirmatory_paths": ["cross-engine qualification channel (A45-dependent)"],
 "files_touched": ["probes/continuation_provenance.py", "probes/x04_freeze_check.py",
                   "probes/cross_engine_control.py", "probes/score_metrics.py",
                   "probes/x27_score_metrics.py", "probes/x30_continuation_boundary.py",
                   "probes/x30_labelling_fixture.py"],
 "also_touched_outside_study_tree": ["pyproject.toml", "uv.lock"],
 "why_not_an_amendment": "PRE-EXECUTION-AMENDMENTS.md requires confirmatory_output_at_time == 'none' on every record; a truthful post-boundary record cannot assert that without misleading a reader. Sections 4.7 and 11 already designate this register."}
```


**This is not a pre-execution amendment, and it is deliberately not recorded as one.**
`PRE-EXECUTION-AMENDMENTS.md` is the pre-execution ledger: `x04.parse_amendments` requires
every record in it to carry `confirmatory_output_at_time == "none"`, and rejects the file
otherwise. A truthful post-boundary record cannot meet that condition without asserting
something false. Sections 4.7 and 11 already designate this register for changes made after
execution starts, and `F9_IGNORE` already exempts it from the ledger's own accounting, so the
frozen protocol's existing structure is the correct home. No new register was invented.

### A47.1 — the inaugural execution and its boundary

The inaugural confirmatory execution of this frozen study crossed its one-way boundary at

    89360b30de480231efdc89157443779d45b37db2

on branch `worktree-pdf-study-confirmatory-run`. That branch was archived externally and is
**not present on `origin`**, and the boundary commit is **not a reachable git object on
`develop`**. Its absence from the current branch is an artifact of archival and branch
deletion. **It is not evidence that the boundary was never crossed**, and the population is
not restored to a pre-execution state by it.

Corroboration is the archive bundle
`pdf-external-validity-run1.bundle`, SHA-256
`1ced656958c056ddc98bc4c2d1e53a91b4846e1f9e2ddabdf2e9ae1674ac4bb1`, containing
`refs/heads/worktree-pdf-study-confirmatory-run`, together with the closure report at SHA-256
`fcc0e171e157a61a1483798570d09d98308f3d82f835155010ba5e7a194a8277`.

### A47.2 — the population is EXPOSED

**All 17 frozen holdout members underwent H/X extraction during Run 1.** This is not an
inference from the run's ambition; it is the canonical code path.
`execute_study.build_document_frame_for` calls `run_hybrid.run(...)` for the H arm and
`run_extended.run(...)` for the X arm, once per descriptor, and `write_frames` ran it over the
complete frozen population: **17 of 17 members, 4,190 pages**, `PAGE_LIMIT = None`.

### A47.3 — results already visible, and which

Section 11 requires this list explicitly. At the time of writing, these result-bearing facts
about the frozen population are known to anyone amending the study:

| quantity | value |
|---|---|
| D-frame region census | **13,992** (budget 60, so Rule 1 **cannot** choose corrected extended glyph; `INSUFFICIENT_COMPARATIVE_EVIDENCE`) |
| S1 liveness control | **17 / 17 documents firing** |
| P-head | **12 documents / 2,864 pages** |
| Canonical frames | 17/17 frames, 4,190 pages, SHA-256 `e33d9f79…1706` |

Everything after that point is **absent**. Run 1 stopped before the canonical
`cross_engine_control.json`, before `score_metrics`, before the oracle key, before any
adjudication by any human or AI, before `scores.json`, and before `decide_architecture`. **No
architecture decision was reached or may be drawn**, including `HYBRID_BY_PRIOR`.

### A47.4 — what a continuation may claim

**Permitted:** the same 17 members may be used to **complete the inaugural execution** as a
transparently qualified continuation following a post-boundary apparatus deviation.

**Forbidden:** representing that work as a fresh, pristine, or independent confirmatory
execution. The holdout has been measured; a second measurement of it is a continuation of the
first, not a replication of it.

A genuinely fresh confirmatory claim would require a **new study and a new freeze over a new
unseen population**. That is out of scope here and is not authorized by this ruling.

The invariant the pre-execution ledger protects is that no change *"can have been selected for
the answer it produces"*. That guarantee no longer holds at full strength for any change made
from Run 1 onward, because the amender has seen the quantities in A47.3. This ruling does not
repair that; it discloses it, which is the only available remedy.

### A47.5 — A45 is a post-boundary result-bearing repair

A45 (PR #637) repaired the canonical cross-engine handoff **after** the boundary at
`89360b30` had been crossed and after the holdout had been opened. It is recorded in the
pre-execution ledger as a `SUBSTANTIVE` amendment carrying `confirmatory_output_at_time:
"none"`. Under that file's own definition, where "confirmatory output" means the canonical
score artifact, that classification is **literally defensible**: Run 1 never produced
`scores.json`.

It is nonetheless **chronologically misleading on its own**, and this ruling supplies the
missing context rather than rewriting the ledger. The ledger is append-only, and editing a
past entry to make the history read better would be the defect, not the fix. A45's entry
stands; **read it as qualified by this section.** A45 is not reopened: the tuple-authority
repair is correct on its own merits and remains closed.

**Consequence under 4.7:** every result **value-dependent** on A45 is
**NON-CONFIRMATORY**. That is the qualification channel, enumerated in A47.6.

### A47.6 — the A45-affected surface, traced rather than assumed

The dependency was traced through the real code, not taken from the expected shape:

    cross_engine_control._control_record        document_sha256 from the authority-checked descriptor
      -> cross_engine_result                    verified_sha256, then
      -> methodology_contracts.cross_engine_pages(sha, pages)
                                                ranks the sample over (document_sha256, page_number)
      -> sampled_pages                          WHICH PAGES ARE MEASURED
      -> x09 gate verdict -> row["passed"]
      -> row["qualification"]                   PDFIUM-CONDITIONED FRAME, or None
      -> score_metrics.qualification()          per_document, both_headlines_qualified,
                                                headline_qualifications RQ1 / RQ2
      -> attached to every per-document surface  qualification, M0, M7, M9,
                                                headings_by_frame, paired_differences,
                                                section 8 event rows
      -> decide_architecture                    REPORTING BLOCK ONLY

The path is **wider than the four-step summary** it is usually described by, because
`score_metrics` deliberately attaches the label to every applicable result surface rather than
to one parent block. It is nonetheless confined to the **qualification channel**.

**Verified NOT affected**, each checked at the source:

| surface | why it is unaffected |
|---|---|
| metric **values** | the qualification is an additive sibling key (`{**block, "qualification": …}`); no metric value is derived from it |
| the **architecture decision** | A27.6 keeps cross-engine out of the Rule 3 gate vector; `decide_architecture` carries it in a reporting block and `decision_blocking` is `False` |
| **denominators** | the artifact is exact-set-equality checked against the scored frames; it does not move the frames denominator |
| **population** | membership unchanged at 17 |

**Availability is not value-dependence.** Without A45, `score_metrics` cannot run at all, so
every score is *enabled* by A45. Only the qualification channel is *valued* by it. Section
4.7 labelling follows value dependence. This is exactly the distinction that stops a single
apparatus repair from voiding an entire run.

### A47.7 — A46 is disclosed, with no result consequence assigned

A46 (PR #640) retired design-era working material after the boundary was crossed. It is
disclosed here chronologically for the same reason A45 is.

**No non-confirmatory consequence is assigned**, because no causal path was found from the
cleanup to any reported quantity, gate, population, architecture decision, or reproducibility
property. The two removed probes own no live invariant: `x06_m6_feasibility` measured M6,
which **A20 STRUCK**, and `x19_raster_edge_diagnostic` states no pass threshold by
construction. Every removed evidence artifact was re-run and rewrote byte-identically before
deletion. G5's result-bearing surface remains 15 files with no member touched.

If a causal path is later demonstrated, this section is the place to append it.

### A47.8 — which gates this could move

| gate | effect |
|---|---|
| `x04` F1–F11 | none; freeze integrity is unchanged and still COMPLETE |
| `x04` **F12** (new) | the continuation record must exist, be committed, and describe **this** frozen population |
| `x04` **G7** (new) | result-bearing toolchain versions must match those Run 1's reproducibility claim is scoped to |
| `x04 --authorize-execution` | **REFUSED** while the population is EXPOSED; a pristine boundary can no longer be created for these 17 members |
| metrics / scores | no value moves; the qualification channel additionally carries `confirmatory_status` |
| architecture decision | none (A27.6) |

### A47.9 — toolchain drift, recorded as part of this ruling

Run 1's byte-identical rebuild claim is scoped to macOS/arm64, Python 3.12.12, pypdfium2
5.12.1 and PyMuPDF 1.28.2. Investigation found that scoping **was not enforced**:

- `pypdfium2` is pinned exactly at 5.12.1 in `uv.lock`, and floored at `>=5.12.1` in
  `pyproject.toml`. The floor alone would admit a newer engine; the lock is what binds.
- **`pymupdf` appears in neither `pyproject.toml` nor `uv.lock`**, while being imported by
  nine study probes, two of which are on the G5 result-bearing surface
  (`cross_engine_control.py`, `control_fixtures.py`). It was an **ambient, unpinned,
  result-bearing dependency**.

  This is stronger than "unpinned", and it was verified rather than inferred. A clean
  `uv sync` in this repository does **not** install PyMuPDF, and the documented invocation
  form fails outright:

      $ uv run python probes/x27_score_metrics.py
      File "probes/build_oracle.py", line 41, in <module>
          import pymupdf
      ModuleNotFoundError: No module named 'pymupdf'

  So the study's own result-bearing probes are **not runnable in the project's declared
  environment at all**. Run 1 was executed against an interpreter carrying PyMuPDF from
  outside the project's dependency management, at a version nothing recorded except the
  closure report's prose. Whoever runs the continuation must do the same, and the version
  they happen to have is what decides the oracle stimuli and the cross-engine qualification.

PyMuPDF is not incidental here: it renders the oracle stimuli that adjudication reads, and the
cross-engine control re-measures through it to decide the PDFIUM-CONDITIONED FRAME
qualification. A silent version change is therefore result-bearing on both surfaces. G7 makes
the drift detectable at gate time instead of invisible.

### A47.10 — the continuation record was certifying itself, and now does not

**Found by trying to falsify the authority rather than to confirm it.** F12 checked that the
record was committed, well-formed, and described the frozen population. Two of its three
historical identity fields were anchored to facts outside the record:

| field | independent fact it is checked against |
|---|---|
| `population.population_freeze_commit` | `POPULATION_FREEZE_COMMIT`, pinned in `x04` |
| `population.membership_blob` | the live blob of the committed manifest |
| `prior_execution.boundary_commit` | **nothing** |

The third is the one the whole ruling rests on, and it was the one nothing checked. Because
Run 1's branch was archived and deleted, the boundary commit is **not a reachable git object
on `develop`**, so no other repository fact contradicts a rewrite of it. **Measured**: an
otherwise valid, committed, internally consistent record with `boundary_commit` replaced left
F12 **GREEN** and the population still reported EXPOSED under a fabricated boundary.

**Repair, deliberately the smallest one.** The commit is now **pinned in `x04`** as
`PRIOR_EXECUTION_BOUNDARY`, exactly as `POPULATION_FREEZE_COMMIT` is pinned and for the reason
that constant's own comment already gives: a historical fact must not be derived from the
thing it is supposed to constrain. No registry, no signing, no provenance framework.

**Isolation proof.** With the pin in place the mutation is refused; with *only* the pin
neutralised and every other check left standing, the identical record is **accepted**. The pin
is therefore the sole reason for the refusal.

**What would make the repaired check fail.** A single commit editing **both** `x04`'s pinned
constant **and** the record. That is no longer an ordinary artifact mutation: it edits a
protected file, so F9 requires it to be declared commit-by-commit in a register, and it
appears in review as a change to gate code rather than to data. The check is not proof against
a determined coordinated edit, and does not claim to be; it removes the *single-artifact*
rewrite, which is what self-certification meant here.

### A47.11 — the PyMuPDF defect is fixed, not only detected

A47.9 recorded that PyMuPDF was undeclared and that G7 could detect the wrong version but
could not supply the right one. That is now closed at the source:

- `pymupdf==1.28.2` is declared in `[dependency-groups].dev` and locked.
- It is **not** added to the published engine dependencies: shipping DeltaTrack to diff two
  bill versions must not install a second PDF engine (#367).
- G7's exact-version assertion is unchanged.

**Verified from the declared environment**, not argued: a clean `uv sync` installs it,
distribution metadata reports `1.28.2`, and `uv run python probes/x27_score_metrics.py` — the
exact invocation that previously died on `ModuleNotFoundError` — now runs to **194/194**.

The 193/194 previously reported for that suite was an artifact of an ad-hoc interpreter that
lacked the declared environment; the failing control is the renderer-free child-interpreter
probe, which cannot be meaningful in an environment that was never constituted correctly. No
x27 control was edited to achieve this.

### A47.12 — the §4.7 status was self-supplied, and is now an invariant

**The defect.** §4.7 makes NON-CONFIRMATORY a **requirement** that A45-dependent results are
validated against. The machinery instead treated it as a **value the study supplied**:
`CONTINUATION.json` carried the status, `a45_status()` returned that field verbatim, the
cross-engine producer stamped whatever came back, the scorer required only that the field
**exist**, and x30 took its expected value from the same record. Authority, result and oracle
could therefore move together.

**Measured before repair**, with the record's status changed to `"CONFIRMATORY"` and treated
as committed. All five steps failed open:

| step | as found |
|---|---|
| A `continuation_state()` / F12 | **GREEN** |
| B `a45_status()` | returned **`CONFIRMATORY`** |
| C real cross-engine producer | **stamped `CONFIRMATORY`** into an artifact |
| D `score_metrics` | **accepted it**; the scored row carried `qualification_status='CONFIRMATORY'` |
| E x30 oracle | **would have moved with the record** |

A post-boundary deviation would have been reported as confirmatory with every gate green.

**Repair, at four boundaries, each independent of the record.**

| boundary | what now holds |
|---|---|
| accessor | `a45_status()` **validates** the claim against `NON_CONFIRMATORY` and returns the **constant**, raising `A45_STATUS_MISMATCH` otherwise |
| authority | `continuation_state()` calls it, so a record claiming another status **fails F12** |
| producer | stamps through the accessor, so it **cannot emit** a fabricated status |
| scorer | `WRONG_CONFIRMATORY_STATUS` refuses a **present but incorrect** value, not only a missing one |

The scorer holds its own constant, `REQUIRED_CONFIRMATORY_STATUS`, because its frozen consumer
allowlist forbids importing the provenance module, and an expectation imported from the thing
under test is not an expectation. x30 asserts the two constants agree so they cannot drift.

**Post-repair, the same mutation is closed at every step:** F12 fails, the accessor raises, the
producer writes no artifact, and the scorer refuses. The record may still carry the
human-readable status; it may no longer decide it.

**Redundancy removed.** The presence-only scorer control was replaced rather than kept
alongside the new one: it proved only that `_require` fires, while the mutation that actually
produced a mislabelled result was a nonempty wrong value. One control now covers both shapes.

---

## A48 — POST-BOUNDARY APPARATUS DEVIATION

```json
{"id": "A48", "kind": "DEVIATION",
 "commits": ["55c35c04", "090716f8", "8a201a6f", "f17cd4e4"],
 "classification": "POST-BOUNDARY APPARATUS DEVIATION",
 "made_after_boundary": "de60dddf906bc4b01e5ffbe9af4d3e833a9a2be7 (continuation boundary)",
 "results_already_visible": {
  "d_frame_census": 13992,
  "oracle_route_composition": "ai_route 122 / human_route 15417 / c_audit 25 / controls 20",
  "cross_engine": "17/17 measured, n_qualified 0, qualification_applies false",
  "s1_documents_firing": "17/17",
  "p_head_documents": 12,
  "p_head_pages": 2864
 },
 "affects_membership": false,
 "affects_scoring_rule": false,
 "affects_metric_values": true,
 "affects_architecture_decision": true,
 "affects_architecture_outcome_enum": false,
 "narrowing": "affects_scoring_rule is FALSE because no frozen rule changed; A48 repairs the implementation of A27.3. affects_metric_values is TRUE because A48 changes R1's required-route population and therefore its value can move. affects_architecture_decision is TRUE only because decided_by / attribution can move; the architecture outcome ENUM is invariant to A48 at D>60, and A48 cannot move a Rule 0 outcome or its attribution.",
 "files_touched": ["probes/methodology_contracts.py", "probes/build_oracle.py",
                   "probes/score_metrics.py", "probes/decide_architecture.py",
                   "probes/x21_build_oracle.py", "probes/x28_decide_architecture.py",
                   "probes/x31_dframe_budget_routes.py",
                   "probes/x27_score_metrics.py"],
 "why_not_an_amendment": "Made after the continuation boundary was committed, with the realized census and route composition already visible. PRE-EXECUTION-AMENDMENTS.md requires confirmatory_output_at_time == 'none' on every record and is the PRE-execution ledger."}
```

**This repair was made with the realized result in view, and says so.** The D census of
13,992 and the full oracle route composition were already committed and visible when it was
written. It is not a pre-execution amendment and is not recorded as one. A47 is unchanged.

### A48.1 — the defect

A27.3 fixes the D-frame budget: **≤ 60 regions** → human-adjudicate the complete census and
Rule 1 may be evaluated; **> 60 regions** → **Rule 1 cannot choose X**, the outcome is
`INSUFFICIENT_COMPARATIVE_EVIDENCE`, and a 60-region sample is permitted for **descriptive
diagnosis only**.

The budget had exactly one owner, `decide_architecture.D_FRAME_REGION_BUDGET`, applied at
**decision step 4**. Every upstream component derived "required route" from **raw frame
membership** instead:

| site | behaviour |
|---|---|
| `build_oracle.StimulusSpec.frame_routes` | `D in frames` → human, unconditionally |
| `human_answer_purposes` | `D in frames` → `PURPOSE_D_DECISION`, unconditionally |
| `build_oracle.validate_adjudicated` | every route named in the key must have an answer |
| `score_metrics.validate_inputs` | calls that validator **before any metric exists** |
| `score_metrics._required_r1_routes` | a second frame→route implementation, same defect |

So a census of 13,992 made **15,372** human answers a hard prerequisite for producing *any*
metric, for a route A27.3 had already made non-decision-bearing. The evidence gate sat
upstream of the rule that excused the evidence.

**Measured before repair**, on real machinery with synthetic material at D = 61: dropping only
the human answers whose sole purpose was the Rule 1 D decision produced
`ADJUDICATION_ROUTE_MISSING`.

### A48.2 — the reading, and the one owner

Read with A36.6: a repeat inherits its primary's **required** routes, and "required" means
**result-bearing**. A route A27.3 has made non-decision-bearing is therefore not required, it
creates no human R1 arm, and it is **absent rather than `NOT_EVALUABLE`**.

The budget and its predicate now have a single executable owner,
`methodology_contracts.d_decision_route_required`, and the frame→route map has a single owner,
`build_oracle.frame_required_routes`, which `score_metrics` calls rather than restating.
`decide_architecture` **re-exports** the constant instead of redefining it. `build_oracle`
reads the realized census from the same committed `counts["d_frame_census"]` the decider reads,
so the two cannot be looking at different censuses.

**Nothing else moves.** The numeric budget, D membership, the full census and its reporting, C
membership and selection, C/D overlap, truth-source semantics, R1 selection identities and
thresholds, C-audit selection, controls, metric definitions, Rule 0, Rule 1, Rule 3 and the
decision ordering are untouched. The optional 60-region descriptive sample remains omitted.

### A48.3 — realized consequence

Derived from the already-committed real key, without opening any image:

| | before | after |
|---|---|---|
| AI route | 122 | **122** |
| human route | 15,417 | **45** (25 C-audit + 20 human-route controls) |
| R1 required-route population | ai + human | **AI only, 6 pairs**; 1,395 D-only repeats require no route |

### A48.4 — section 4.7 status

A48 changes **which adjudication inputs are consumed**, so it is value-bearing for anything
computed from that set. It takes the same §4.7 status **class** as A45/A47 but its **own
literal**, because the A45 label names A45 and this is a different deviation:

    NON-CONFIRMATORY (PRE-REGISTRATION 4.7 -- A48 post-boundary deviation)

Held as a constant in `score_metrics` and in `decide_architecture`, never read from this
document or any other mutable record, so nothing under test supplies its own expected
provenance. Applied to `r1_reliability` only where A48 actually moved it (census over budget)
and to the decision artifact's **attribution** only where `decided_by` turns on that R1 gate.

**The final architecture outcome enum is invariant to A48.** Demonstrated executably over the
real decider across all four Rule 0 states at D > 60: with R1 forced to PASS and to FAIL the
outcome is identical in every state (`EXTENDED_BY_RULE_0_M9`, `HYBRID_BY_RULE_0_M9`, or
`INSUFFICIENT_COMPARATIVE_EVIDENCE`). At D > 60 Rule 1 cannot choose X, so the enum is fixed by
the committed M9 facts and the census alone. The decider was **not** reordered and no rule was
changed to obtain this; it is a property of the frozen ordering.

### A48.5 — the committed oracle key

The key committed at `7afbc344` is semantically wrong in **private route metadata only**:
`adjudication_routes`, `human_answer_purposes`, `n_human_tasks`, and the key-level
`human_route` / `human_tasks` counts.

**Proven by executable control**, building the same synthetic population twice with only the
predicate differing: blind ID set, presentation order, canonical and base identities, R1 base
identities, C/D membership, C-audit selection, repeat flags, bboxes, DPI, `png_sha256`,
region–line bijection, image names, control kind and variant, `prompt_sha256`, **every PNG
byte**, and the **entire blind artifact byte-for-byte** are identical. Only the three
per-stimulus route fields and the two human counts differ.

The real key was **not** regenerated and **not** hand-edited in this round.

### A48.6 — an A47.12 regression found and fixed

`x28_decide_architecture` could not run at all on `develop`: A47.12 made
`confirmatory_status` a required, value-checked field on the cross-engine artifact, and x28's
own fixture predated it, so the entire architecture-decider suite failed at input validation.
Reproduced on clean `86e48de`. The fixture now carries the scorer's own constant. No decider
rule was touched.

### A48.7 — closure review: the first repair had only reached validation and R1

**Chronology, recorded exactly.** The first A48 pass conditioned route *derivation*
(`frame_routes`, `human_answer_purposes`, `_required_r1_routes`) and its control asserted
through a helper that ran `validate_adjudicated` plus `r1_reliability`. That helper was named
`full_path`, and it was not: `score_metrics.score` went on walking
`(D_FRAME, PURPOSE_D_DECISION)` in `heading_metrics` and demanding a human answer for **every**
D primary. So the 45-item workload had never traversed the result-bearing scorer, and the
control read green because it never called it.

Closure review caught this before merge. **Execution was still blocked throughout and no
adjudication had occurred**, so nothing was scored on the false-green.

**Measured before the second repair**, through the real `SM.score` at D=61 with exactly the
A48-required adjudication (all required AI, 25 C-audit human, 20 control human, no D-only
human): `ADJUDICATION_ROUTE_MISSING {route: 'human'}`.

**Repairs.**

1. `heading_metrics` consumes the D estimand only while the D route is result-bearing. The D
   rows are **omitted, not zeroed**: a zero M1–M5 block would assert the arms were measured and
   agreed on nothing, which this run never gathered. The payload states which it is, in
   `d_estimand_status`.
2. **The key may no longer self-certify its A27.3 state.** `validate_inputs` re-derives the
   census by summing each committed frame's producer-declared `counts["d_frame_census"]`,
   requires exact equality with `oracle_key["d_frame_census"]`, and requires the key's
   `d_decision_route_required` to equal `MC.d_decision_route_required(committed census)`.
   D membership is not re-derived from region contents; the committed counts remain the
   producer's census. A coordinated key claiming 61 over a real 60-region census is refused
   (`D_CENSUS_MISMATCH` / `D_BUDGET_CLAIM_MISMATCH`) before any metric is produced. This
   matters because a true census of 60 is exactly where Rule 1 **may** select X.
3. `build_oracle` **fails closed** on a frame with no declared `d_frame_census`. Absent is not
   0: 0 is within budget and would silently excuse Rule 1's evidence.

The helper is renamed `validation_and_r1` and kept only where validation and R1 really are the
semantics under test. The end-to-end arms call the real scorer and the real decider.

**`decided_by` is not invariant, and the enum-invariance claim needed this qualification.**
Re-measured across all Rule 0 states at D>60: the outcome **enum** is identical under R1 PASS
and R1 FAIL, as previously reported, but the **attribution** is not. Where Rule 0 decides,
`decided_by` is `RULE_0_M9` either way. Where Rule 0 does not decide, the enum is
`INSUFFICIENT_COMPARATIVE_EVIDENCE` either way while `decided_by` flips between
`BUDGET_A10_A27_3` (R1 PASS) and `RULE_3_GATE` (R1 FAIL). A48 changes R1's required-route
composition, so it can move that attribution. Reported rather than smoothed over.

---

## A49 — POST-BOUNDARY APPARATUS DEVIATION

```json
{"id": "A49", "kind": "DEVIATION",
 "commits": ["eea4fc40"],
 "classification": "POST-BOUNDARY APPARATUS DEVIATION",
 "made_after_boundary": "de60dddf906bc4b01e5ffbe9af4d3e833a9a2be7 (continuation boundary)",
 "results_already_visible": {
  "d_frame_census": 13992,
  "s1_documents_firing": "17/17",
  "p_head_documents": 12,
  "p_head_pages": 2864,
  "cross_engine": "17/17 measured, n_qualified 0"
 },
 "affects_membership": false,
 "affects_scoring_rule": false,
 "affects_metric_values": false,
 "affects_architecture_decision": false,
 "affects_execution_authorization": true,
 "narrowing": "A49 changes only how x04 establishes the CHRONOLOGY of already-declared pre-execution amendments. It reads no holdout byte, produces no metric, and touches no scoring rule, threshold, route, selection or architecture rule. affects_execution_authorization is TRUE because the gate's verdict changes: a lawful integration that x04 refused is no longer refused on this ground.",
 "files_touched": ["probes/x04_freeze_check.py"]}
```

**State when the defect became observable.** The continuation boundary had already been
crossed at `de60dddf`. The population was EXPOSED, and these results were already visible:
D census 13,992; S1 17/17; P-head 12 documents / 2,864 pages; cross-engine 17/17 measured
with `n_qualified` 0. The reviewed A48 apparatus had already been integrated into the
preserved continuation execution branch by a history-preserving merge. x04 refused at that
point, BEFORE oracle regeneration, before any adjudication, before any scoring, and before
any new holdout exposure. No result-bearing stage was rerun and no holdout byte was read.

**The defect.** `amendment_commits` dated an amendment by the CURRENT last-modifying commit
of every path in its `files_touched`, and the one-way-boundary rule then required that
commit to be an ancestor of the marker. The derived date therefore tracked whoever edited
the file most recently rather than when the amendment was made. A48 lawfully modified four
files that twelve pre-boundary amendments had also touched, and x04 reported A28, A29, A30,
A35, A36, A37, A38, A39, A40, A41, A42 and A43 as landing after the marker. Measured on the
real history: 0 violations at the pre-A48 execution HEAD `7afbc344`, 12 at `30a92586`, with
every newly selected commit an A48 commit. A28 is the clearest case: it declares `0cf7daf`,
which is an ancestor of the marker, so the ledger was correct and the derivation disagreed
with it.

**The invariant now enforced.** A pre-execution amendment's chronology is anchored to that
amendment's own historical implementation. A later declared deviation touching the same path
must never retroactively move the earlier amendment across the execution boundary. A genuine
post-boundary methodological commit must still be independently declared, and must never be
accepted as a pre-execution SUBSTANTIVE amendment.

Chronology is taken from the amendment's own declared `commits` wherever present, and every
declared commit is checked rather than a single latest one, so a post-boundary commit cannot
be hidden behind a pre-boundary sibling. Of the 40 SUBSTANTIVE records, 24 carry explicit
commits and 16 are legacy; all twelve formerly-flagged amendments are in the explicit set.
Legacy records fall back to the last modification of their touched files AS VISIBLE AT THE
MARKER, which later history cannot move.

**What is deliberately not claimed.** On the legacy path every candidate is by construction
reachable from the marker, so that path cannot by itself convict an amendment of being
post-boundary. That is honest rather than lax: a post-boundary SUBSTANTIVE record has to be
written into the ledger to exist, and the seal already forbids any committed ledger edit
after the marker. Per-commit accounting, bidirectional file naming and that seal are
unchanged.

**Controls.** F9 is extracted into `f9_result()` so its properties can be driven on a
synthetic history with a real marker. Nine controls were added, including the mutation that
restores the pre-A49 HEAD-sensitive dating and must turn the primary control red. Bidirectional
file accounting is left to the existing decisive self-test rather than duplicated.

**A second blocker remains, and A49 does not address it.** Once F9 stopped failing first,
x04 refused the same integration again on METHODOLOGY DRIFT: the marker pins 18 frozen blobs,
and A48 lawfully changed three of them (`probes/build_oracle.py`, `probes/decide_architecture.py`,
`probes/score_metrics.py`). Measured independently of A49: 0 drifted at `7afbc344`, 3 at
`30a92586`. This is a consequence of integrating A48 under a marker that pins the pre-A48
blobs, it is outside A49's authorized scope, and it is recorded here so that A49 is not read
as having restored execution authorization on its own.

---

## A50 — POST-BOUNDARY APPARATUS DEVIATION

```json
{"id": "A50", "kind": "DEVIATION",
 "commits": ["4518998a", "97cead5a", "0474b950", "42c1b95f", "53b55846"],
 "classification": "POST-BOUNDARY APPARATUS DEVIATION",
 "made_after_boundary": "de60dddf906bc4b01e5ffbe9af4d3e833a9a2be7 (continuation boundary)",
 "results_already_visible": {
  "members": 17,
  "pages": 4190,
  "d_frame_census": 13992,
  "s1_documents_firing": "17/17",
  "p_head_documents": 12,
  "p_head_pages": 2864,
  "cross_engine": "17/17 measured, n_qualified 0"
 },
 "affects_membership": false,
 "affects_scoring_rule": false,
 "affects_metric_values": false,
 "affects_architecture_decision": false,
 "affects_execution_authorization": true,
 "affects_reproducibility_surface": true,
 "narrowing": "A50 changes the authorization and reproducibility machinery, not a scientific rule. It adds a state to x04's execution state machine and widens the manifest of files whose change the gate can see. It reads no holdout byte, produces no metric, and changes no threshold, route, selection rule or architecture rule. D_FRAME_REGION_BUDGET is unchanged at 60. affects_execution_authorization is TRUE because a reviewed post-boundary apparatus can now authorize continuation, which was previously unreachable; affects_reproducibility_surface is TRUE because METHODOLOGY_SURFACE goes from 15 files to 27.",
 "files_touched": ["probes/x04_freeze_check.py"]}
```

**State when this was written.** The continuation boundary had already been crossed at
`de60dddf`. The population was EXPOSED and these results were already visible: 17 members /
4,190 pages; D census 13,992; S1 17/17; P-head 12 documents / 2,864 pages; cross-engine 17/17
measured with `n_qualified` 0. A48 had been reviewed and merged (`b47141d7`, PR #660) and
integrated into the preserved continuation execution branch by a history-preserving merge at
`30a92586`. A49 had been reviewed and merged (`648f8612`, PR #665). Execution remained
stopped: no oracle had been regenerated under A48, no adjudication had occurred, no score
existed, and no architecture decision existed. Canonical frames SHA-256
`e33d9f79…0ec91706` was unchanged. No result-bearing stage was rerun and no holdout byte was
read.

**The first defect: there was no state for a reviewed post-boundary apparatus.** Once the
marker was VALID, x04 compared the marker's `frozen_blobs` against the tree and had exactly
two outcomes — unchanged, or `METHODOLOGY DRIFT … EXECUTION INTEGRITY FAILS`. That warning
was correct and must not be suppressed: the immutable marker at `de60dddf` pins the exact
result-bearing blobs authorized then, and A48 lawfully changed three of them
(`probes/build_oracle.py`, `probes/decide_architecture.py`, `probes/score_metrics.py`).
Measured on the real integrated history at `30a92586`: 3 drifted of 18 manifest entries.

But section 4.7 explicitly permits a necessary post-boundary change as a DEVIATION, with
every value-dependent affected result labelled NON-CONFIRMATORY. A45 and A48 already use that
mechanism. What did not exist was the transition from *immutable original authorization* to
*reviewed post-boundary deviation* to *explicit authorization to continue under the reviewed
current apparatus*. Without it the only routes back to a runnable gate were to rewrite the
historical marker or to silence the check, and both destroy the evidence the marker exists to
preserve.

**The second defect: the authorization surface was not truthful.** A48 moved the
authoritative A27.3 budget predicate into `probes/methodology_contracts.py`. That module now
holds `D_FRAME_REGION_BUDGET = 60` and `d_decision_route_required(...)`, which decide whether
the full D-human route is required — a `60 -> 60000` mutation would move the real required
human population from 45 back toward 15,417 — and it also owns `SELECTION_SEED`,
`select`/`order`/`blind_id` (blind stimulus identity and presentation order), `required_dpi`,
`m5_agreement`, the bootstrap and `adequacy`. No authorization manifest named the file at all.
A manifest cannot drift on a key it does not have, so this was invisible to the gate by
construction rather than by oversight.

**What A50 adds.** A separate write-once artifact,
[`EXECUTION-CONTINUATION-AUTHORIZATION.json`](EXECUTION-CONTINUATION-AUTHORIZATION.json),
generated by `x04 --authorize-apparatus-continuation`. `EXECUTION-START.json` is **not**
modified, re-dated, replaced or reinterpreted: it remains historical evidence of the exact
apparatus authorized at `de60dddf`, and rewriting it to describe A48's apparatus would make it
testify that code which did not exist then had already been reviewed. Two different facts, two
files, neither pretending to be the other.

The new artifact binds, and the gate re-checks against independent facts rather than the
artifact's own say-so: the original marker's commit **and** blob; the pinned population freeze
commit **and** the committed membership blob; `population_status: EXPOSED`; the HEAD at
authorization; the **complete** current `METHODOLOGY_SURFACE` blob manifest; the
`DEVIATIONS.md` blob; the reviewed deviation ids acknowledged; and the truthful statements
that this is a continuation of the inaugural execution rather than a fresh pristine run, which
results were already visible, and that section 4.7 remains in force.

**A deviation does not authorize itself.** A changed result-bearing file plus a matching
`DEVIATIONS.md` row is disclosure and provenance, not authority to execute changed
methodology. That combination remains `EXECUTION FORBIDDEN`. It is the mandatory control on
this repair: if it ever goes green, A50 is wrong.

**Nothing chains.** The authorization pins the `DEVIATIONS.md` blob, so a further
post-boundary change necessarily moves that blob and closes the gate again, and both artifacts
are write-once by the same test (exactly one modifying commit, and the current blob equal to
the blob that commit introduced). A future deviation therefore fails closed and requires a new
explicit review and ruling. There is deliberately no automatic rolling authorization chain.

**The authorization records REVIEWED current methodology; it cannot legalize an undeclared
change by snapshotting it.** This is the rule the first draft of A50 was missing, and the
omission mattered: every other clause asks whether the artifact agrees with the tree, and
none asked whether the tree's differences had ever been declared for review. A committed
change to a result-bearing file could therefore be written into a fresh authorization and
thereby legalized, with no deviation record ever existing. F9 did not close it either — F9
scans only paths under EV, so a change to result-bearing code outside the study directory
was green there by construction.

So for every current authorization-surface path, each commit that modified it after the
boundary must be declared in the deviation register, and that declaration must name that
exact path. The correspondence is derived from git history and the register, never from the
authorization's own account of what changed: an artifact that inventories its own drift is
describing itself. `acknowledged_deviations` is checked the same way — the deviations that
matter are those declaring the commits that actually changed the surface, so naming some
other record while the relevant one is absent acknowledges nothing.

A file with **no** post-boundary commit needs no declaration. It is unchanged since the
boundary, and the only reason it is missing from the original manifest is that the manifest
was incomplete. Requiring a deviation record for it would mean inventing a fiction about a
change that never happened. Measured on the integrated history: eight post-boundary commits
touch surface paths, all eight are declared in the A48 register and name the exact path, and
the five files outside the study directory have no post-boundary commit at all.

**Merges are attributed too, because a merge can be the only commit that ever carried a
byte.** `git log --name-only` prints no file list for a merge, which is correct for an
ordinary integration — the commit that made the change is the one that must declare it — but
a merge's tree is not obliged to match any parent. Content written while resolving a
conflict, or staged between `git merge --no-commit` and the commit, belongs to the merge
alone, and was therefore attributed to nothing. So for every post-boundary merge, the merge's
blob for each surface path is compared against every parent's blob, with **absence treated as
a value** so a path the merge deletes while every parent has it is caught like a rewritten
one. Equality with any parent means the merge introduced nothing novel and demands no
duplicate record; difference from all of them requires the exact merge SHA and the exact path
in this register. Swept across the marker to `30a92586`, to `origin/develop`, and to the
repair head: **0 merge-introduced surface paths**, so the rule adds no demand the real
history cannot meet.

**The surface reaches further than it did, and its coverage is now executable.** A bounded
one-hop dependency audit over the
result-bearing components asked of each direct import whether mutating it could change C/D
membership or selection, a route requirement, R1 selection or status, blind stimulus identity
or presentation order, what an adjudicator sees, a metric value, or the architecture outcome
or `decided_by`. Twelve answered yes and were added, taking `METHODOLOGY_SURFACE` from 15
files to 27: `methodology_contracts.py`, `neutral_identity.py`, `anchor_provenance.py`,
`oracle_geometry.py`, `xml_sources.py`, `x09_skeleton_cross_engine.py`,
`continuation_provenance.py`, and — through a new `repo:`-namespaced manifest key, because
result-bearing code does not stop at the study directory — `src/deltatrack/parsers/pdf_text.py`,
`src/deltatrack/parsers/pdf_anchors.py`, and the H arm's `contract_hybrid.py`,
`reconstruct_hybrid.py` and `backends/pdfium_hybrid.py`. The rest of the import graph was not
recursively frozen.

One **data** input was added under the same criterion, kept in its own list so the category
stays auditable: `results/control_fixtures.json`. `build_oracle.control_specs` builds every
field of the N-A/N-B/N-C stimuli from that committed manifest — "nothing is re-derived,
nothing is searched for" — and those expected truths are what Rule 3 is evaluated against.
G6 and this pin are different claims and neither substitutes for the other: G6 proves the
manifest is COHERENT, the authorization proves it is the manifest that was AUTHORIZED, and a
coherent replacement set would satisfy G6 while changing what Rule 3 is scored against. The
audit was bounded to data the listed methodology READS; the study's own outputs
(`frames.json`, `oracle_*.json`, `metrics.json`, `scores.json`) and gate evidence such as
`x26_control_oracle.json`, which `validate_manifest` consumes rather than the result-bearing
path, are deliberately excluded. The authorization manifest is therefore 31 entries: 27 code,
1 data, and the protocol, ledger and population.

Coverage is enforced rather than assumed: an authorization whose manifest does not name the
whole current surface cannot authorize, which is why the pre-A50 marker cannot silently speak
for A48's apparatus.

**`D_FRAME_REGION_BUDGET` is unchanged at 60.** A50 changes only whether a change to it would
be *seen*.

**Controls.** They run on a synthetic history carrying every failure mode at once — a file
that drifted from the marker, a result-bearing file the marker never named, and a committed
change to result-bearing code outside EV that nothing declares. That last one is asserted to
leave F9 GREEN, so the hole the provenance rule closes is demonstrated rather than assumed.
The controls drive the real generator rather than a hand-written lookalike, and the
provenance pair is red-then-green on a single mutation: with the change undeclared,
generation is refused and no authorization file is written; once its exact commit and its
`repo:`-namespaced path are declared, the same generator writes the artifact and the
committed result permits continuation. They also cover: a declared
deviation with no authorization (forbidden); a valid committed authorization (permitted as
continuation); a foreign original marker commit and a foreign marker blob; a foreign
population freeze and a foreign membership blob; an incomplete surface manifest; an
authorization claiming a pristine execution; an acknowledged deviation absent from the
register; acknowledging a real but irrelevant deviation while omitting the relied-on one;
undeclared post-authorization drift; drift in the previously-uncovered budget
predicate; drift in a `repo:`-namespaced file; drift in the committed control manifest; an
edited or recommitted authorization; an
edited or recommitted original marker; and a further change that is properly declared but not
re-authorized. Every red state is followed by a restore and a re-assertion that the good state
is green again, so a failure is attributable to the mutation rather than to leftover state.

**What A50 does not do.** It does not create the real continuation authorization, regenerate
the oracle, adjudicate, or score. It does not touch the preserved execution branch. It does not
withdraw or alter the section 4.7 NON-CONFIRMATORY status of any A45- or A48-dependent result,
and it does not change any semantics A48 established: the real D census remains 13,992, the
required adjudication workload remains AI 122 / human 45 with 6 R1 AI pairs, and the D-human
Rule 1 route remains not result-bearing.

## A51 — POST-BOUNDARY TEST-ISOLATION DEVIATION

```json
{"id": "A51", "kind": "DEVIATION",
 "commits": ["fc9287b5"],
 "classification": "POST-BOUNDARY TEST-ISOLATION DEVIATION (TOOLING)",
 "made_after_boundary": "de60dddf906bc4b01e5ffbe9af4d3e833a9a2be7 (continuation boundary)",
 "results_already_visible": {
  "members": 17,
  "pages": 4190,
  "d_frame_census": 13992,
  "s1_documents_firing": "17/17",
  "p_head_documents": 12,
  "p_head_pages": 2864,
  "cross_engine": "17/17 measured, n_qualified 0"
 },
 "affects_membership": false,
 "affects_scoring_rule": false,
 "affects_metric_values": false,
 "affects_architecture_decision": false,
 "affects_execution_authorization": false,
 "affects_reproducibility_surface": false,
 "narrowing": "A51 changes the LIFETIME of an existing self-test control group and nothing else. The absent-marker controls now construct the absent state they assert and hold it for the whole group, restoring the ambient marker byte-for-byte at the end. It adds no control, removes none, and leaves the 100 count unchanged. It reads no holdout byte, produces no metric, and changes no threshold, route, selection rule, scoring rule or architecture rule. affects_execution_authorization is FALSE: the state machine, its states, its refusals and every authorization artifact are untouched -- only the test's own setup and teardown moved.",
 "files_touched": ["probes/x04_freeze_check.py"]}
```

**The defect.** The absent-marker controls inherited their precondition from the working
tree rather than constructing it. `saved_marker` was restored inside the first `finally`,
so the ambient marker was back on disk before the group asserted `marker_state() ==
"ABSENT"` and before the stubbed `main([])` was checked for READY TO AUTHORIZE.

**Why it stayed invisible.** On a branch that never carried a marker, `saved_marker` is
None, nothing is restored, and both assertions hold. On a branch carrying a valid committed
marker the restore puts it back, `marker_state()` returns VALID, and `main([])` never
reaches the ABSENT arm of the state machine. A continuation is only ever authorized on the
second kind of branch, so the controls were silent precisely where they had to hold.

**Evidence.** On a clean tree with a committed valid marker the unrepaired self-test returns
98/100, failing exactly `absent marker reports ABSENT, not VALID` and `...and says READY TO
AUTHORIZE`. On a clean tree with no marker the same code returns 100/100. After the repair
both environments return 100/100, and neutralizing the isolation reproduces exactly those
two failures and no others.

**What A51 does not do.** It does not create the continuation authorization, regenerate the
oracle, adjudicate, score, or produce an architecture decision. It does not touch the
preserved execution branch. It does not alter any authorization semantics, any section 4.7
NON-CONFIRMATORY status, or any value established by A47, A48, A49 or A50.

## A52 — POST-BOUNDARY AUTHORIZATION-FIELD DEVIATION

```json
{"id": "A52", "kind": "DEVIATION",
 "commits": ["75d1e3fd"],
 "classification": "POST-BOUNDARY AUTHORIZATION-FIELD DEVIATION (APPARATUS)",
 "made_after_boundary": "de60dddf906bc4b01e5ffbe9af4d3e833a9a2be7 (continuation boundary)",
 "results_already_visible": {
  "members": 17,
  "pages": 4190,
  "d_frame_census": 13992,
  "s1_documents_firing": "17/17",
  "p_head_documents": 12,
  "p_head_pages": 2864,
  "cross_engine": "17/17 measured, n_qualified 0"
 },
 "affects_membership": false,
 "affects_scoring_rule": false,
 "affects_metric_values": false,
 "affects_architecture_decision": false,
 "affects_execution_authorization": true,
 "affects_reproducibility_surface": false,
 "narrowing": "A52 changes ONE field of the continuation authorization -- `acknowledged_deviations` -- and the validation of that one field. It reads no holdout byte, produces no metric, and changes no threshold, route, selection rule, scoring rule or architecture rule. It does not touch the original marker, the population, the manifest, the deviations blob, provenance, merge attribution, or any write-once rule. affects_execution_authorization is TRUE, deliberately and unlike A51: the contract an authorization must satisfy to be VALID is narrower after this change than before it, so an artifact that would have passed can now be refused. No authorization artifact exists at the time of this record, so nothing already issued is invalidated by it.",
 "files_touched": ["probes/x04_freeze_check.py"]}
```

**The defect.** `acknowledged_deviations` was built as `[r.get("id") for r in
parse_deviations()[0]]` -- every record in the register -- while the field's stated purpose
is to name the deviations the authorization RELIES ON. On the real tree those differ: the
register declares A47, A48, A49, A50 and A51, and history supports A48 alone. Validation
agreed with the generator rather than with the purpose, requiring only
`required_deviation_ids(...) <= acknowledged`, so the padded field passed.

**Why it stayed invisible.** A50-16 already proved the field cannot OMIT a relied-on
deviation, which reads as exactness and is half of it. The subset check is green for every
superset, and the generator only ever produced the largest superset there is, so the two
halves of the contract were never in tension. The register and the relied-on set also
coincide whenever every declared deviation happens to be result-bearing -- true of the A50
synthetic fixture, which is why no control caught this.

**Why padding is not harmless.** A superset asserts the authorization rests on records it
does not rest on, and this is the field a human reads to learn what was relied on. It also
restates `deviations_blob`, which already binds the complete register by content: two
mechanisms for one fact, where the weaker one eventually disagrees.

**Evidence.** With the exactness control added and the repair withheld, the self-test
returns 103/104, failing exactly `A52-1 acknowledging the relied-on deviation PLUS an
irrelevant declared one is refused` and nothing else; its companion assertions confirm the
refusal is absent rather than arriving for the wrong reason. After the repair the same
control returns 104/104. A50-10c (unknown id) and both A50-16 assertions (omission) stay
green, so neither existing rejection was absorbed into the new one. On the real tree
`required_deviation_ids()` is `["A48"]` before and after, so the repaired generator emits
`["A48"]`.

**What A52 does not do.** It does not create the continuation authorization, regenerate the
oracle, adjudicate, score, or produce an architecture decision. It does not touch the
preserved execution branch. It does not alter any section 4.7 NON-CONFIRMATORY status, or
any value established by A47, A48, A49, A50 or A51.

## A53 — POST-BOUNDARY AUTHORIZATION-FIELD DEVIATION

```json
{"id": "A53", "kind": "DEVIATION",
 "commits": ["c223c6b1"],
 "classification": "POST-BOUNDARY AUTHORIZATION-FIELD DEVIATION (APPARATUS)",
 "made_after_boundary": "de60dddf906bc4b01e5ffbe9af4d3e833a9a2be7 (continuation boundary)",
 "results_already_visible": {
  "members": 17,
  "pages": 4190,
  "d_frame_census": 13992,
  "s1_documents_firing": "17/17",
  "p_head_documents": 12,
  "p_head_pages": 2864,
  "cross_engine": "17/17 measured, n_qualified 0"
 },
 "affects_membership": false,
 "affects_scoring_rule": false,
 "affects_metric_values": false,
 "affects_architecture_decision": false,
 "affects_execution_authorization": true,
 "affects_reproducibility_surface": false,
 "narrowing": "A53 changes ONE field of the continuation authorization -- `results_already_visible` -- its generation, and its validation. It reads no holdout byte, produces no metric, and changes no threshold, route, selection rule, scoring rule or architecture rule. It does not modify CONTINUATION.json, the canonical cross-engine artifact, the original marker, the population, the manifest, the deviations blob, provenance, merge attribution, or any write-once rule. It adds one derived read of the committed canonical cross-engine control, used ONLY to report exposure and never to re-decide anything that artifact measured. affects_execution_authorization is TRUE: the contract an authorization must satisfy to be VALID is narrower after this change, so an artifact that would have passed can now be refused. No authorization artifact exists at the time of this record, so nothing already issued is invalidated by it.",
 "files_touched": ["probes/x04_freeze_check.py"]}
```

**The defect.** `results_already_visible` was generated from `CONTINUATION.json`
alone and validated only for being non-empty. That record is the truthful history of
Run 1, and Run 1 stopped BEFORE the canonical cross-engine control -- it says so, under
`prior_execution.stopped_before`. The control was measured afterwards over the same frozen
population and committed as `results/cross_engine_control.json` (17 documents, n_qualified
0). The generated summary therefore named Run 1's results and omitted a committed
confirmatory-population measurement, and a non-empty check cannot tell an incomplete
sentence from a complete one.

**Why it matters in one direction only.** Overstating exposure is self-penalising and
visible. Understating it is neither: a shorter list of already-visible results makes
whatever the study has left to do look more independent than it is, and a reader holding
only the authorization has nothing to compare it against. `continuation_auth_errors`
already described the field as recording what was visible "when it was written", so the
contract was right and only the check was weak.

**Why it stayed invisible.** The register itself had disclosed the cross-engine result in
prose since A52, so a human reading DEVIATIONS.md saw it; only the authorization did not
carry it. The generator and the validator also agreed with each other -- both were built
around the Run 1 record -- so the two halves of the contract were never in tension, which
is the same shape as the A52 defect one field over.

**The design.** Two phases, kept apart. `CONTINUATION.json` is preserved unchanged as the
historical Run 1 record; `historical_exposure_summary` (renamed from
`exposure_summary_for_authorization`, because it is no longer the whole answer) owns that
half. `authorization_exposure_summary` is the union of Run 1 and everything committed
since. The cross-engine phase is derived from the committed artifact and re-derived from
its own document rows, so a summary disagreeing with its evidence, or an unreadable,
incomplete or uncommitted artifact, is REFUSED at generation rather than silently omitted.
The snapshot has a fixed lifetime: generation records the pre-authorization HEAD,
validation independently derives the authorizing commit's parent, requires
`head_at_authorization` to equal it, and reconstructs exposure from that tree -- so a later
authorized result cannot retroactively falsify a summary that was truthful when written,
and the record cannot nominate the tree it will be judged against.

**Evidence.** The self-test goes from 104 to 118 gates. With the validator withheld and the
controls in place, exactly two fail -- `A53-2 deleting the cross-engine fact from
results_already_visible is REFUSED` and `A53-3 a head_at_authorization that is not the
derived pre-authorization parent is REFUSED` -- and the generation-side controls stay
green, so the refusal is attributable to the validator. With the generator withheld
instead, 17 controls fail, because the repaired validator refuses a Run-1-only summary
outright. After the repair the suite returns 118/118. The non-empty check is REPLACED
rather than supplemented: the exact comparison subsumes it, and keeping both would be two
mechanisms for one fact.

**What A53 does not do.** It does not create the continuation authorization, regenerate the
oracle, adjudicate, score, or produce an architecture decision. It does not touch the
preserved execution branch. It does not modify `CONTINUATION.json`, the cross-engine
result, `pyproject.toml`, or any production parser. It does not alter any section 4.7
NON-CONFIRMATORY status, or any value established by A47, A48, A49, A50, A51 or A52.

## A54 — POST-BOUNDARY APPARATUS DEVIATION

```json
{"id": "A54", "kind": "DEVIATION",
 "commits": ["4b5c2f6a", "f4cd4fdc", "0a10f2f9"],
 "classification": "POST-BOUNDARY APPARATUS DEVIATION (ROUTE DERIVATION)",
 "made_after_boundary": "de60dddf906bc4b01e5ffbe9af4d3e833a9a2be7 (continuation boundary)",
 "results_already_visible": {
  "members": 17,
  "pages": 4190,
  "d_frame_census": 13992,
  "s1_documents_firing": "17/17",
  "p_head_documents": 12,
  "p_head_pages": 2864,
  "cross_engine": "17/17 measured, n_qualified 0"
 },
 "affects_membership": false,
 "affects_scoring_rule": false,
 "affects_metric_values": true,
 "affects_architecture_decision": true,
 "affects_execution_authorization": false,
 "affects_reproducibility_surface": true,
 "narrowing": "A54 changes WHICH ROUTES A CONSUMER ASKS FOR, and only for the single frozen pre-A48 artifact identified by its complete content digest. Reinterpretation is OFF by default: for every other key the stored `adjudication_routes` remain the requirement exactly as before A54, so ordinary post-A48 validation is untouched and a key whose stored routes disagree with its purposes is still judged on what it stored. It reads no holdout byte and changes no threshold, selection rule, metric definition or architecture rule. It does not modify the key, the blind artifact, the images, the membership, the frames, the original marker, the continuation authorization or any write-once rule, and it never rewrites or reinterprets the frozen key's historical bytes as a current claim. affects_scoring_rule is FALSE: A54 implements the ALREADY-FROZEN A27.3 rule as A48 installed it, and introduces no rule of its own. affects_metric_values is TRUE, corrected from an earlier reading of this record: for the real key the R1 and evaluability path moves from REFUSAL to the effective population, so the metric block that gets produced is not the one the pre-A54 apparatus would have produced, and \"no metric could be produced before\" describes an unsatisfiable gate rather than an absence of effect. affects_architecture_decision is TRUE for the same reason at one remove: the repair makes the decision artifact REACHABLE at all, and can affect A48-dependent `decided_by` attribution, even though the outcome enum at a census above the budget remains constrained to INSUFFICIENT_COMPARATIVE_EVIDENCE and Rule 1 still cannot select corrected extended glyph. affects_reproducibility_surface is TRUE: `probes/build_oracle.py` and `probes/score_metrics.py` are both members of the 31-entry authorization manifest, so integrating this into the study branch moves two manifest blobs and the continuation authorization at 74ccf247 would no longer speak for the current apparatus.",
 "files_touched": ["probes/build_oracle.py", "probes/score_metrics.py", "probes/x31_dframe_budget_routes.py", "probes/x32_effective_routes.py"]}
```

**The defect.** A48 closed a real hole: a key must not self-certify its A27.3 state,
so `d_frame_census` and `d_decision_route_required` are re-derived in
`score_metrics.validate_inputs` from the committed frames and the frozen predicate.
For keys that carry those fields that is complete. For a key that predates them, A48
chose `key.get("d_decision_route_required", True)` at the consumers, reasoning that an
older artifact should keep meaning exactly what it meant when it was built rather than
being silently reinterpreted as having fewer required routes.

That reasoning holds for every key but one. The frozen confirmatory key has a realized
D-frame census of 13,992. A27.3, as implemented by A48, has already ruled that route
non-decision-bearing: Rule 1 cannot select corrected extended glyph, and the outcome is
INSUFFICIENT_COMPARATIVE_EVIDENCE. Defaulting that key to `True` therefore demands a
human answer on all 15,417 stored human routes as a hard prerequisite for producing any
metric at all, on a route that cannot decide anything. The effective human workload is
45: 25 seeded C-audit items and 20 controls. A default that cannot be satisfied is not
conservative.

**Measured, not argued.** Against the real committed key, before this change,
`build_oracle.validate_adjudicated` refused a complete 45-item human review with
`ADJUDICATION_ROUTE_MISSING {'route': 'human'}`. After it, the same call accepts, with
the effective human population at exactly 45 and the AI population unmoved at 122.

**Why derivation is from purposes.** The stored `adjudication_routes` on a pre-A48 key
were derived from raw frame membership, which is precisely the quantity A27.3 governs,
so they cannot be the thing consumers ask. `human_answer_purposes` already records why
each human answer exists, and `PURPOSE_ROUTE` already maps purpose to route. Dropping
only `d_decision`, only where the predicate denies it, leaves `c_audit` and
`control_human` untouched. That is what keeps all 25 seeded C-audit items human-required
even where they are also D-frame members; 19 of them are. A rule that excluded anything
carrying `d_decision` would have silently reduced the frozen 25-item C audit to six.

**Scoped to one artifact, cryptographically.** `PRE_A48_FROZEN_KEY_SHA256` is the SHA-256 of
the frozen key's complete canonical content, `66972235...`, the same digest as the committed
file. It is computed by streaming `iterencode`, so the 307 MB serialization is never
materialized, and memoized per object so each consumer does not recompute it.

An earlier spelling of this record pinned a SUMMARY fingerprint instead: schema, stimulus
count, prompt digest and aggregate frame counts. That is not an identity. The entire `stimuli`
mapping can change while every one of those fields holds, and because routes are derived from
`human_answer_purposes`, a key could drop `c_audit` from one selected record, keep
`frame_counts.c_audit_selected == 25`, receive the exception, and validate 24 audit answers
while looking complete. x32 asserts that exact mutation is denied with every summary field
unchanged, and the same for a single altered stored route.

**Reinterpretation is off by default.** Only the frozen artifact has its routes derived from
purposes. Every other key keeps the pre-A54 meaning of its stored routes, so the exception
cannot make a malformed post-A48 key easier to validate; x32 asserts that direction too.

**What A54 does not do.** It does not create or modify any authorization, regenerate any
oracle input, prepare a human-review packet, adjudicate, score, or decide the
architecture. It does not perform the optional 60-region descriptive D sample, which
cannot change the architecture result.

**What it obliges next.** Because two authorization-manifest files move, integrating this
into `pdf-study-continuation-execution` requires a NEW continuation authorization; the one
at 74ccf247 speaks for the apparatus as it stood before this repair. That is deliberately
not done in this round.
## A55 — POST-BOUNDARY APPARATUS DEVIATION

```json
{"id": "A55", "kind": "DEVIATION",
 "commits": ["e785f4cb", "87d4d2f2"],
 "classification": "POST-BOUNDARY APPARATUS DEVIATION (AUTHORIZATION MECHANISM)",
 "made_after_boundary": "de60dddf906bc4b01e5ffbe9af4d3e833a9a2be7 (continuation boundary)",
 "results_already_visible": {
  "members": 17,
  "pages": 4190,
  "d_frame_census": 13992,
  "s1_documents_firing": "17/17",
  "p_head_documents": 12,
  "p_head_pages": 2864,
  "cross_engine": "17/17 measured, n_qualified 0"
 },
 "affects_membership": false,
 "affects_scoring_rule": false,
 "affects_metric_values": false,
 "affects_architecture_decision": false,
 "affects_execution_authorization": true,
 "affects_reproducibility_surface": false,
 "narrowing": "A55 changes only HOW A CONTINUATION AUTHORIZATION IS SUCCEEDED. It reads no holdout byte and changes no threshold, selection rule, metric definition, route derivation or architecture rule. It does not modify the population, the frames, the frozen key, the original execution marker or any existing authorization, and it never renames, edits, deletes, recommits or reinterprets the sequence-1 artifact. A55 also validates every chain entry against its OWN pre-authorization snapshot: an entry must have been TRUE when committed, not merely immutable afterwards, so a successor cannot launder a predecessor whose payload was false when written. affects_execution_authorization is TRUE by construction: this record is about the authorization mechanism itself. affects_reproducibility_surface is FALSE, and that is AUDITED rather than assumed: `probes/x04_freeze_check.py` is a member of none of METHODOLOGY_SURFACE, RESULT_BEARING_DATA or AUTHORIZATION_EXTRAS, so no blob in the 31-entry authorization manifest moves. It is the gate that polices the surface, not a member of it. Verified against the real tree at 74ccf247: the repaired gate reports EXECUTION PERMITTED AS CONTINUATION with 31 current result-bearing blobs unchanged, the identical verdict the pre-A55 gate gives on the same commit.",
 "files_touched": ["probes/x04_freeze_check.py"]}
```

**The defect.** A50 made the continuation authorization write-once, which is correct, and
implemented that as a TERMINAL state. `--authorize-apparatus-continuation` refuses unless
the authorization is ABSENT, so once a valid one exists the generator will not produce
another under any circumstances. A50's own closing clause, "a further deviation requires a
NEW explicit review and ruling; this does not chain", states the review requirement
correctly. The code enforced it by making the required artifact unbuildable. Those are not
the same thing, and the difference is invisible until a second reviewed deviation arrives.

**Why it surfaces now.** A54 moves `probes/build_oracle.py` and `probes/score_metrics.py`,
both members of the 31-entry authorization manifest. Projected onto
`pdf-study-continuation-execution`, the authorization at 74ccf247 correctly goes stale: it
still validates as an artifact, and it no longer speaks for the apparatus in force. Before
this repair there was no lawful way forward. The only ways to resume were to edit a
write-once file or to suppress the check, and both destroy the evidence the artifact exists
to preserve.

**The repair.** An append-only chain. Sequence 1 keeps its filename and is never renamed,
edited, deleted or recommitted. Each successor is a NEW file,
`EXECUTION-CONTINUATION-AUTHORIZATION-<n>.json`, committed exactly once, carrying an
explicit integer sequence and binding its immediate predecessor by path, authorizing commit
and blob. The chain is derived from repository history and exact filenames, never from what
the newest artifact claims its own ancestry to be, so a successor cannot certify the one
fact the chain exists to establish.

**What it does not weaken.** Write-once is preserved exactly, because nothing is ever
edited: a successor is an addition, not a revision. Authority does not roll forward. Every
changed apparatus still requires its own separate reviewed, committed artifact, and the gate
stays FORBIDDEN until that artifact is committed. An invalid, missing, mutated or deleted
predecessor invalidates the whole chain, and a later entry cannot cure an earlier one, so
appending is not a repair mechanism. "Is there something new to authorize" is asked against
the LATEST authorization rather than the original marker, so an unchanged apparatus cannot
receive a second licence. A55 supersedes A50 in exactly one respect: A50 provided no
successor mechanism. Nothing else A50 established is changed.

**Read-only verification against the real tree.** Established without modifying the
preserved worktree, which remains clean at 74ccf247. At 74ccf247 the one-entry chain is
valid and the gate reports PERMITTED AS CONTINUATION, with zero drift against the
authorization itself. Projecting integration of d5330a54 onto a scratch branch: freeze
integrity COMPLETE, execution readiness OPEN, sequence 1 still VALID but stale on exactly
two manifest blobs, execution FORBIDDEN, and sequence 2 named as required. The relied-on
deviation set derives from history to exactly `["A48", "A54"]`. Generating sequence 2 there
succeeded with its entire working-tree footprint being one new untracked file, so no frozen
scientific artifact is touched. That generated artifact was discarded and the scratch
worktrees removed; no successor authorization was committed anywhere.

**Historical truthfulness.** Chain validation deliberately does not judge a predecessor
by today's tree, because going stale is what made its successor necessary. An earlier
spelling of this repair implemented that as not judging it by ANYTHING: the manifest, the
pinned register blob, the relied-on deviation set and surface provenance were checked only
for the latest entry and only against the live tree, so the moment an entry acquired a
successor those claims stopped being checked. A sequence 2 whose payload was false when
written therefore became permanent as soon as a correctly bound sequence 3 sat on top of
it. Write-once fixes the bytes without making them true, and the binding checks only prove
that entries point at each other.

Every entry is now re-validated against its own immutable pre-authorization commit, derived
from history as the authorizing commit's parent and never read from the artifact. Coverage,
the register and history are all read AT that snapshot, so a truthful entry cannot be failed
by later commits and a false one cannot be excused once the register catches up. The latest
entry must satisfy both historical truthfulness and agreement with the current tree.

**What A55 does not do.** It does not integrate `pdf-study-continuation-execution`, create
any successor authorization, prepare a human-review packet, adjudicate, score, or decide the
architecture. It creates no authorization of any kind. It makes one buildable, once, subject
to the same review every authorization has always required.

## A56 — POST-BOUNDARY TEST-ISOLATION DEVIATION

```json
{"id": "A56", "kind": "DEVIATION",
 "commits": ["e75111d9"],
 "classification": "POST-BOUNDARY TEST-ISOLATION DEVIATION (TOOLING)",
 "made_after_boundary": "de60dddf906bc4b01e5ffbe9af4d3e833a9a2be7 (continuation boundary)",
 "results_already_visible": {
  "members": 17,
  "pages": 4190,
  "d_frame_census": 13992,
  "s1_documents_firing": "17/17",
  "p_head_documents": 12,
  "p_head_pages": 2864,
  "cross_engine": "17/17 measured, n_qualified 0"
 },
 "affects_membership": false,
 "affects_scoring_rule": false,
 "affects_metric_values": false,
 "affects_architecture_decision": false,
 "affects_execution_authorization": false,
 "affects_reproducibility_surface": false,
 "narrowing": "A56 changes WHERE THE F7 AND F8 NEGATIVE CONTROLS PUT THEIR BAD BYTES, and nothing else. The gate is untouched: `check_freeze`'s F7 and F8 clauses, their wording and their verdicts are exactly as before, and only the self-test's own fixture moved. It reads no holdout byte for any research purpose, produces no metric, and changes no threshold, route, selection rule, scoring rule or architecture rule. It adds four arms, three isolation checks plus a pre-mutation cleanliness check, removing no control and rewording no existing arm. affects_execution_authorization is FALSE: the authorization state machine, its states, its refusals and every authorization artifact are untouched. affects_reproducibility_surface is FALSE on the same audited basis as A55: `probes/x04_freeze_check.py` is a member of none of METHODOLOGY_SURFACE, RESULT_BEARING_DATA or AUTHORIZATION_EXTRAS, so no blob in the 31-entry authorization manifest moves.",
 "files_touched": ["probes/x04_freeze_check.py"]}
```

**The defect.** The F7 and F8 negative controls mutated the CANONICAL POPULATION. F8
truncated the first manifested holdout file in place, to `<!DOCTYPE html>` followed by that
file's own first 100 bytes; F7 created an intruder inside `holdout/`. Each was undone in a
`finally`. Both controls are correct about what they assert and were wrong about where they
assert it.

**Why it stayed invisible.** A `finally` runs on exceptions and on ordinary interpreter
exit, which covers every failure the controls were written against. It does not run on
SIGKILL. Nothing in the self-test could report the difference either, because F2 (every
holdout file matches its recorded SHA-256) and F10 (frozen artifacts have no uncommitted
change) live in the GATE and not in `--self-test`. A self-test can therefore pass every one
of its arms and still leave the frozen population corrupted, which is precisely the state a
green run is read as excluding.

**Measured, not argued.** A self-test run driven by a mutation harness was killed with
SIGKILL mid-arm. It left `holdout/116-hr-7611/rh.pdf` at 116 bytes, down from 286,181, and
a later `git add -A` committed the corrupted frozen artifact. The file was restored to blob
`8a5d46f1`, verified identical to the blob at the population freeze commit `4e2b520d`, and
that branch was abandoned rather than rewritten, since a mergeable history containing a
post-freeze mutation of a frozen artifact is not repaired by a later restoring commit.

**The repair.** `DOCS_DIR` is rebound to a temporary fixture for the duration of both
controls, which isolates them together because F7 and F8 read nothing else. No canonical
`holdout/**` path is opened for writing at any point. The `finally` now restores a global,
not a file, so a hard kill at the worst possible moment destroys nothing that matters.
Cleanup is deliberately no longer the thing that protects the population: `finally`, signal
handlers and post-run repair are one bet, that the process survives to clean up, and a hard
kill wins that bet every time.

**Red before green.** Three arms assert the property that matters, where the bad bytes go,
rather than whether cleanup happened to run. Measured against a faithful reconstruction of
the direct-write implementation on a disposable worktree, all three fail: the mutation
target is not outside the canonical tree; the canonical file is not byte-identical while
the corrupt bytes exist, asserted before cleanup because afterwards the old code would
satisfy it too; and the canonical tree gained a file. The F7 and F8 detection arms stay
green under that same mutant, so the reds are attributable to isolation rather than to
detection breaking.

**What A56 does not do.** It changes no gate, no authorization, no scientific value, and no
research artifact. It does not integrate any branch, create an authorization, prepare a
packet, adjudicate, score, or decide the architecture.

## A57 — POST-BOUNDARY APPARATUS DEVIATION

```json
{
 "id": "A57",
 "kind": "DEVIATION",
 "commits": [
  "dcc2e990",
  "49ed1f7d",
  "7e87acd2",
  "b263360f",
  "fc8ce91f",
  "8a3ad000",
  "3321d5b6",
  "fafa2b45",
  "4b7b851e",
  "05e772e2",
  "a5fa991a",
  "39359aae",
  "17dfcd72",
  "f0687016",
  "0a5d9eb3",
  "ce717732",
  "ba7cae8d",
  "38c0982e",
  "a398eaa6",
  "202b7ec9",
  "57e73d72"
 ],
 "classification": "POST-BOUNDARY APPARATUS DEVIATION (AI ADJUDICATION ARM)",
 "made_after_boundary": "de60dddf906bc4b01e5ffbe9af4d3e833a9a2be7 (continuation boundary)",
 "results_already_visible": {
  "members": 17,
  "pages": 4190,
  "d_frame_census": 13992,
  "s1_documents_firing": "17/17",
  "p_head_documents": 12,
  "p_head_pages": 2864,
  "cross_engine": "17/17 measured, n_qualified 0"
 },
 "affects_membership": false,
 "affects_scoring_rule": false,
 "affects_metric_values": false,
 "affects_architecture_decision": false,
 "affects_execution_authorization": true,
 "affects_reproducibility_surface": true,
 "narrowing": "A57 BUILDS THE AI ADJUDICATION ARM that PRE-REGISTRATION 5.5 specifies and no code implemented. It reads no holdout byte and changes no threshold, selection rule, metric definition, route derivation or architecture rule. It does not modify the population, the frames, the frozen key, the blind artifact, the images, the original execution marker or either existing authorization. affects_metric_values is FALSE: no metric definition moves, and the single change to a pre-existing surface file (score_metrics.write_metrics at 3321d5b6) only REFUSES -- it computes nothing new and alters no value that was computable before. affects_execution_authorization and affects_reproducibility_surface are TRUE by construction: three files join METHODOLOGY_SURFACE / RESULT_BEARING_DATA, taking the authorization manifest from 31 entries to 34, so sequence 2 correctly goes stale and cannot speak for files it has never seen. The scorer's frozen import allowlist is widened by one, `ai_finalize`, so that whether an oracle may be scored can depend on where it came from; x27's own control is what made that widening visible, and the rejected alternative (moving verify_provenance into build_oracle) is recorded at the allowlist. NAMING NOTE: commit messages under these shas refer to 'the A57, A58, A59 and A60 reviews'. Those were labels for four independent reviews, not register ids; this record is the first use of A57 as a deviation id and the reviews have no register entries. COMMIT COVERAGE EXTENDED AFTER THE SURFACE GREW. results/AI-ADJUDICATION-PROTOCOL.json was not result-bearing when it was written, so the six commits that touched it (4b7b851e, 05e772e2, 49ed1f7d, a5fa991a, 39359aae, 17dfcd72) named no surface path and needed no declaration. Adding it to RESULT_BEARING_DATA at fafa2b45 made its entire history result-bearing, and surface_provenance_errors correctly required every one of those commits to be declared and to name the path. They are declared here rather than exempted: a file whose history is unaccounted for is exactly the silent surface hole A50 exists to close. 17dfcd72 SIMPLIFIED the arm, removing the run ledger, commencement semantics, resume-only recovery, run states and the two-phase START marker -- roughly 1,500 lines defending a property no local mechanism can enforce, now attested instead. It also carries three repairs to the GATE itself: blob_sha treating a path absent at a commit as present, the A50 synthetic controls inheriting the real RESULT_BEARING_DATA, and the self-test's membership tamper not surviving a signal. f0687016 rebuilt ai_finalize against the bundle the simplified runner actually writes -- it had been left addressing the removed run-<id> layout, so it could not have run at all -- and made derivation REPLAY the runner's acceptance rules over raw stdout rather than read the `accepted` flag beside it. 0a5d9eb3 replaced score_metrics.write_metrics(payload, path) with score_canonical(), which loads the committed inputs, verifies the oracle's origin, scores and writes as ONE operation: the payload argument made 'verify this oracle, write a metric computed from that one' expressible, which the protocol's finalizer.scoring_gate forbids. ce717732 extended the replay to compare every field an attempt records about itself against its own raw stdout, not only `accepted`, because the transcript is what a reviewer reads and an unchecked summary field can misdescribe an attempt without moving an answer. ba7cae8d drove `materialize()`, the production entry, which was the one path in the arm with no control over it -- the same shape as the f0687016 defect, where a module was green over a layout nothing produced. It changes no result-bearing code: x34_ai_finalize.py is a control file, declared here because F9 protects every .py under the study directory, not because it is on the authorization surface. NO METRIC DEFINITION MOVES IN ANY OF THEM: score() is untouched, and affects_metric_values stays FALSE. The scorer's frozen import allowlist is widened by a further two, `execute_study` (the committed owner of which documents are in the study, so that canonical_inputs does not become a second authority for the population) and `hashlib` (the oracle digest that binds the bytes verified to the bytes scored); the rejected alternative for each is recorded at the allowlist, as the ai_finalize widening was. ANSWERED AN INDEPENDENT ADVERSARIAL REVIEW AT 38c0982e, which found seven real defects in the arm as it stood at sequence 3. Four were introduced this session. In order of consequence: a harness envelope decoding to anything but an object raised after the paid subprocess call and before the transcript write, destroying the evidence of an attempt already paid for (predates this session, and would also have broken derivation, which replays the same function over committed stdout); the canonical score read oracle_key.json, s1_control.json and cross_engine_control.json straight off disk, so an edited S1 or cross-engine row moved a reported result without touching the AI bundle; provenance named the run directory by absolute path, defeating the clean-checkout reproduction the protocol's evidence bundle requires; the runner that produced a bundle was never compared with the runner replaying its acceptance rules, so a rule change was silent because it need not change any answer; the digest binding verification to scoring was taken by re-opening the file after verification returned; materialize() inverted the protocol's attestation order and checked nothing, so the statement would be signed by someone who had already seen the result; and several provenance fields were written and never read, letting the record assert more than a green verifier established. NO METRIC DEFINITION MOVES IN ANY OF THEM EITHER: score() is still untouched and affects_metric_values stays FALSE. probes/execute_study.py joins files_touched because the committed-input check belongs with load_frames, which has asked the same question since A43; x27's own import-allowlist control is what established that, by refusing the first version that asked it inside the scorer. A SECOND ADVERSARIAL PASS OVER THOSE FIXES, answered at a398eaa6, found more -- and the worst of it in the RUN path rather than the analysis. A usage limit discarded attempts that had already been paid for and handed the item a fresh retry budget on resume, so a stimulus could receive more attempts than the protocol declares; transcript writes were not atomic, so an interruption could leave a file whose name said the item was finished and whose contents could not be parsed; the runner identity was hashed when RUN.json was written at the end rather than before the first paid call, so a runner edited mid-run would be recorded as the one that produced the bundle; the oracle was written WITHOUT build_oracle's assert_write_permitted, making it the one canonical artifact producible before a valid execution boundary; the attested bundle digest was not compared with the materialized one; and the committed-input check was check-then-read rather than one read compared against HEAD, which also left a tracked-symlink hole. Four controls were found to be false-green and were repaired so each kills the code it names. NO METRIC DEFINITION MOVES HERE EITHER: score() remains untouched and affects_metric_values stays FALSE. THE ONE FINDING NOT FIXED is recorded rather than smoothed away: committing results/AI-ADJUDICATION-ATTESTATION.md trips F9, which requires a declaration, which takes the standing authorization stale. That is the gate working as designed, and adding the attestation to F9_IGNORE would weaken a gate for the operator's convenience; the sequence belongs in the runbook instead. A THIRD REVIEW, RUN IN TWO HALVES, RETURNED NO-GO ON BOTH, answered at 202b7ec9. The most serious finding was that the oracle could be written with NONE of its preconditions: they lived in materialize(), while finalize() writes the canonical artifact by default, so calling the lower function with an injected runs_root and item list produced the study's oracle from an external uncommitted bundle -- and verification passed it, because it checked the item COUNT and never that the ids were the frozen AI-route population. Next worst was in the arm's own acceptance rule: a refusal the model expressed AS JSON beside an empty heading list was accepted as the substantive claim 'no heading is printed in this image', while the same refusal in prose was correctly refused -- a defect that converts a refusal into a metric denominator. The run loop lost paid attempts on interruption and granted a fresh retry budget, did not stop on a usage limit reported through the raw error channel, and re-read the prompt per item after checking it once. THE PROTOCOL IS AMENDED under this entry, with the operator's approval and BEFORE any stimulus was adjudicated: it now declares the three model-identity failure conditions the code enforced and the protocol omitted, the six isolation control labels a committed bundle is held to, and an atomicity claim corrected to what the code does. That amendment is legitimate exactly as the protocol's own amendment_note says -- the ai namespace is empty and no transcript exists, so the artifact still records what was fixed before anyone could see a result. NO METRIC DEFINITION MOVES: score() remains untouched and affects_metric_values stays FALSE. THE ARM WAS THEN EXECUTED, and 57e73d72 is the commit the note above anticipated: it carries the operator's signed attestation naming run id bf3e1346d963647071b996af73d94785e8727a97e05cbaf29a850f5ca13f75d7, it is a post-freeze .md under the study directory, and it is declared HERE rather than added to F9_IGNORE, with the authorization regenerated behind it. The run itself is committed at 0a6cdd02 as results data, which F9 does not protect and which therefore needs no declaration: 122/122 items answered, every one on its first attempt, no refusals, no usage-limit stop, all six declared isolation controls passing with their leaking arms, and model_usage naming only the declared confirmatory model and the declared auxiliary. NO METRIC DEFINITION MOVES HERE EITHER: score() remains untouched and affects_metric_values stays FALSE.",
 "files_touched": [
  "probes/ai_adjudicate.py",
  "probes/ai_finalize.py",
  "probes/execute_study.py",
  "probes/score_metrics.py",
  "probes/x04_freeze_check.py",
  "probes/x27_score_metrics.py",
  "probes/x33_ai_adjudicate.py",
  "probes/x34_ai_finalize.py",
  "probes/x35_mutation_harness.py",
  "results/AI-ADJUDICATION-ATTESTATION.md",
  "results/AI-ADJUDICATION-PROTOCOL.json"
 ]
}
```

**What was missing.** PRE-REGISTRATION 5.5 specifies the coverage-frame oracle as AI
image-adjudication by a separate `claude -p` process with no repository context, its prompt
and transcript committed. No code implemented it. The human route was adjudicated and
committed at 0b493c9f; the AI route's 122 items had never been run, and
`score_metrics.validate_inputs` refuses without them, so the study could not be scored.

**Why it took four reviews.** Three independent code reviews each found the same property —
that the first binding run cannot be re-rolled — unenforced in a different place: no driver at
all, then a driver gating only the cheap setup phase, then a guard bypassable by deleting a
directory, aborting mid-run, or running twice concurrently. Each time the author reported it
implemented and verified beforehand. A fourth review of the APPROACH found the rule itself was
wrong rather than merely unimplemented: "the first run that COMPLETES binds" permits watching
transcripts land item by item and aborting once they look disagreeable. The rule now binds on
first COMMENCEMENT with resume-only recovery.

**What is claimed, and what is not.** The binding property is an ATTESTATION, not a repository
proof. The operator controls the filesystem, the processes, the credential and git history, so
no local mechanism can establish that a command was never run; local guards defend against
ACCIDENT and the operator's signed attestation carries the rest. Assurance beyond that needs an
executor the operator does not control, which is a study-design decision and not a coding one.
The execution marker already makes the same admission in the same words.

**Isolation is measured, not assumed,** and the finding was counter-intuitive: `--restricted`
suppresses BOTH project-level and user-level memory, while `ANTHROPIC_CONFIG_DIR` alone does
not — with it set and `--restricted` absent, a planted project `CLAUDE.md` was read back
verbatim and a separate probe recovered the operator's name and role. Every isolation control
has an arm that must leak, and each was proved to fire before its protected counterpart was
trusted.

**Verified.** x33 51/51, x34 24/24, x27 195/195, x35 23/23. x35 is a mutation harness: it
breaks the apparatus on purpose, 23 defects one at a time, and requires the verifier to notice.
Its first run caught 10 of 22 — the number that justified the exercise, since x33 had until
then reported 26/26 while staying green under a deleted binding guard. It is a corpus, not a
proof: it establishes that these specific defects cannot pass unnoticed.

## A61 — POST-BOUNDARY APPARATUS DEVIATION

```json
{
 "id": "A61",
 "kind": "DEVIATION",
 "commits": [
  "f865dfb4"
 ],
 "classification": "POST-BOUNDARY APPARATUS DEVIATION (AUTHORIZATION GENERATOR REPAIR)",
 "made_after_boundary": "de60dddf906bc4b01e5ffbe9af4d3e833a9a2be7 (continuation boundary)",
 "results_already_visible": {
  "members": 17,
  "pages": 4190,
  "d_frame_census": 13992,
  "s1_documents_firing": "17/17",
  "p_head_documents": 12,
  "p_head_pages": 2864,
  "cross_engine": "17/17 measured, n_qualified 0",
  "ai_route": "122/122 adjudicated, committed at 0a6cdd02"
 },
 "affects_membership": false,
 "affects_scoring_rule": false,
 "affects_metric_values": false,
 "affects_architecture_decision": false,
 "affects_execution_authorization": true,
 "affects_reproducibility_surface": false,
 "narrowing": "A61 REPAIRS THE GENERATOR THAT MINTS A CONTINUATION AUTHORIZATION, and changes no threshold, selection rule, metric definition, route derivation or architecture rule. score() is untouched and affects_metric_values is FALSE. No file joins or leaves METHODOLOGY_SURFACE, RESULT_BEARING_DATA or AUTHORIZATION_EXTRAS, so the authorization manifest is the same 34 entries before and after and affects_reproducibility_surface is FALSE; probes/x04_freeze_check.py is declared here because F9 protects every .py under the study directory, not because it is on that surface. THE DEADLOCK: the gate retires an authorization whose pinned DEVIATIONS.md blob has moved, while the generator tested only manifest_divergence over the methodology surface, which does not include the register. Declaring the operator's attestation in A57 moved the register without touching any surface file, so the gate read EXECUTION FORBIDDEN and the generator read 'nothing has changed'. The apparatus could not be advanced by any supported command. The generator now delegates that verdict to continuation_auth_errors, the gate's own validator, because two implementations of 'is this authorization still in force' is the defect and the missing register check was only where it surfaced. ONE SNAPSHOT PER RECORD: both artifact producers pinned blobs read from the working tree into records naming a HEAD commit, and nothing reconciled the two. The register reached neither check that would -- F9 exempts it by F9_IGNORE and F10 does not carry it -- so an uncommitted declaration could be pinned into a record claiming a head at which those bytes never existed, refused by historical validation only after the entry was already in an append-only chain. Every pin now resolves at the commit the record names, in the continuation producer AND in the execution marker, which carried the identical defect. build_execution_marker was extracted because its payload was built inline in main, where no control could reach it. ALSO: publication is now atomic and no-clobber via os.link, because a temp-and-rename overwrites and an exclusive create can strand a truncated record; the freeze and readiness gates are revalidated immediately before publication rather than only at entry; and the PERMITTED AS CONTINUATION line now names the chain entry actually in force, having read sequence 1 unconditionally. WHAT IS NOT CLOSED: there is no single atomic check before publication. Each read opens its own window and the last closes only at the link. A change that PERSISTS is retired by the gate on its next run; a TRANSIENT one, reverted before anything looks again, is not. This is a single-operator local repository, which is why that exposure is tolerable rather than answered. VERIFIED: the gate's own self-test at 270/270, and forty-five mutations each required to kill the control written for it. Several controls were found vacuous first and repaired -- a truthiness check under a comment claiming exactness, a substring match where 8 matched 18, an assertion comparing HEAD against HEAD, a refusal branch the fixture could never enter, and an ordering fix whose own undoing nothing detected. NOT ADDRESSED and tracked separately: G2's baseline fixture is already invalid, so several G2 controls pass for reasons unrelated to their labels. That predates this work and reworking those fixtures is its own change with its own review.",
 "files_touched": [
  "probes/x04_freeze_check.py"
 ]
}
```

## A62 — POST-BOUNDARY APPARATUS DEVIATION

```json
{
 "id": "A62",
 "kind": "DEVIATION",
 "commits": [
  "4599505d"
 ],
 "classification": "POST-BOUNDARY APPARATUS DEVIATION (R1 ROUTE COMPARISON)",
 "made_after_boundary": "de60dddf906bc4b01e5ffbe9af4d3e833a9a2be7 (continuation boundary)",
 "results_already_visible": {
  "members": 17,
  "pages": 4190,
  "d_frame_census": 13992,
  "s1_documents_firing": "17/17",
  "p_head_documents": 12,
  "p_head_pages": 2864,
  "cross_engine": "17/17 measured, n_qualified 0",
  "ai_route": "122/122 adjudicated, committed at 0a6cdd02",
  "oracle": "materialized at 8f9831a8"
 },
 "affects_membership": false,
 "affects_scoring_rule": false,
 "affects_metric_values": true,
 "affects_architecture_decision": true,
 "affects_execution_authorization": false,
 "affects_reproducibility_surface": true,
 "narrowing": "A62 MAKES THE R1 ROUTE COMPARISON ASK THE A54 OWNER, and changes no threshold, selection rule, metric definition, frame derivation or architecture rule. A48 conditioned the frame-derived REQUIREMENT on the A27.3 budget but left `_required_r1_routes` reading the repeat's stored `adjudication_routes` raw, so the two sides of that comparison were derived under different rules. On the frozen pre-A48 key, whose routes came from RAW D membership, they can never agree: 1399 of 1401 R1 repeats mismatch, 1395 D-only declaring ['human'] against a required (), and 4 C+D declaring ['ai','human'] against ('ai',). `score_canonical()` refused outright. `score_metrics` was the ONLY route-requirement consumer outside `effective_record_routes`; `build_oracle.validate_adjudicated` and `ai_adjudicate.ai_route_items` already ask it. THIS IS THE THIRD LAYER OF ONE DEFECT: the first A48 pass conditioned route derivation, A48.7 found `heading_metrics` still walking (D_FRAME, PURPOSE_D_DECISION), and this is the declared-side comparison. Each was latent until the layer above it was unblocked, because scoring could never run end to end on the real key: `validate_inputs` refused without the AI route, which exists only as of the confirmatory adjudication at 0a6cdd02. affects_scoring_rule is FALSE: A62 implements the already-frozen A27.3 rule as A48 and A54 installed it and introduces no rule of its own. affects_metric_values is TRUE on the same reading A54 recorded: the R1 path moves from REFUSAL to the effective population, so the metric block produced is not the one the pre-A62 apparatus would have produced. affects_architecture_decision is TRUE at one remove: the repair makes the decision artifact REACHABLE, and the R1 verdict it yields sets A48-dependent `decided_by` attribution, though the outcome enum at a census above the budget remains constrained to INSUFFICIENT_COMPARATIVE_EVIDENCE and Rule 1 still cannot select corrected extended glyph. affects_reproducibility_surface is TRUE: `probes/score_metrics.py` is a member of the authorization manifest, so the continuation authorization at sequence 7 no longer speaks for the current apparatus. `probes/x27_score_metrics.py` is declared here because F9 protects every .py under the study directory, not because it is on that surface. THE REFUSAL IS UNWEAKENED: `reinterpret` is False for every key but the one pinned by a SHA-256 over its complete canonical content, and with it False `effective_record_routes` returns the stored routes unchanged, so a shortened repeat still mismatches its frame requirement and still refuses; the digest covers `adjudication_routes` and `human_answer_purposes` alike, so shortening the pinned key to earn the reinterpretation denies recognition instead. VERIFIED: x27 at 199/199, the gate's own self-test at 270/270, ruff clean. Every pre-existing R1 fixture is a post-A48 key for which reinterpretation never engages, so all 23 of them passed against an implementation that never enabled it at all; four checks now pin it in both directions and were shown RED before green. NOT ADDRESSED and tracked separately as issue 726: the scorer emits NOT_EVALUABLE_NO_R1_PAIRS for a zero-evidence R1 while `rule3_gates` accepts only NOT_EVALUABLE, so that verdict falls through to PASS. Not exercised by this run, since R1 text is FAIL on a non-empty denominator, and unrelated to route reinterpretation. ALSO NOT ADDRESSED, predating this work: G2's baseline fixture is already invalid, so several G2 controls pass for reasons unrelated to their labels.",
 "files_touched": [
  "probes/score_metrics.py",
  "probes/x27_score_metrics.py"
 ]
}
```

### A62.1 — the R1 population collapse, and why no evidence floor was added

**This is a finding about the study design under A27.3, not a defect and not a repair.**
It is recorded because the number it produces decides a Rule 3 gate.

With the comparison fixed, R1 resolves to **6 pairs, all on the AI route, with a summed
heading-occurrence denominator of 5**:

| dimension | observed | threshold | verdict |
|---|---|---|---|
| text | 4/5 = 0.80 | >= 0.90 | **FAIL** |
| role | 4/5 = 0.80 | >= 0.80 | **PASS**, by exact equality |

Four pairs are one-vs-one matched and agree on both dimensions. One pair is one-sided: the
adjudicator enumerated no heading on the primary presentation and one on the repeat. Under
R6.1 that occurrence stays in the denominator and earns no numerator, so **that single item
alone produces both 4/5 figures**. The sixth pair is zero-vs-zero and contributes nothing,
which is why `n_pairs` reads 6 while the denominator is 5; the pair count overstates the
evidence and should not be read as the evidence base.

**The AI arm was never a designed sample.** `plan_r1_repeats` draws an unstratified 10 % of
all eligible primaries, `floor(14016 * 0.10) = 1401`, with no frame or stratum quota. The D
frame outnumbers C by about 146:1, so a draw of 1395 D-only, 4 C+D and 2 C-only repeats is
an arithmetic consequence of the population shape rather than an allocation. R1's designed
power lived entirely in the human arm, and A27.3 as implemented by A48 removed that arm.
What remains is the residue of an unstratified draw, now carrying the whole gate.

**What the five occurrences are.** Four carry the fine section 5.3 role `other` and are bill
designators (`†HR 6157 EAS`, `•S 1609 PCS`, `•HR 6147 RH`); one is `section` (`SEC. 504.`).
`other` belongs in R1: section 5.3's codebook includes it, section 5.6 restricts no role set,
and R6.3 records that M5 alone coarsens. Excluding designators would itself be post-hoc, and
the role is not causal in any case, since any one-sided occurrence fails both dimensions
identically.

**No evidence floor was added, deliberately.** Section 5.6 freezes the 10 % repeat fraction
and the two thresholds and nothing else: no minimum pair count, no minimum denominator, no
stratification. A floor introduced now would take its value from having seen that a
denominator of 5 produces a FAIL, which is the substitution the pre-registration exists to
prevent. `_r1_status` therefore continues to treat every positive denominator as evaluable,
exactly as frozen.

**The consequence is applied, not softened.** Section 5.6's R1 row reads "below -> text
metrics void / role metric void". The scorer reports that at `metrics.r1_text_gate`, which
names M2 and M3 as voided when the text dimension is FAIL; `decide_architecture` does not
read it, because Rule 3 (A27.6) owns the decision consequence and a failing Rule 3 blocker
already forecloses a comparative result. **So the artifact carries M2 and M3 flagged void on
the strength of five heading occurrences.** That is the conservative direction and it is what
section 5.6 froze: declining to apply it after seeing the number would be the softening the
register exists to refuse.

**The contrary reading is recorded rather than dismissed.** A36.6's "C only -> AI, D only ->
human" and section 5.6's "10 % of regions presented twice" read literally keep the 1395
D-only repeats as human-route items, in which case their absent answers would REFUSE rather
than resolve to no required route. A48 chose the other interpretation, that a
non-result-bearing route is absent and is not scored. That choice is what makes any metric
producible at all, and it is why every figure above is labelled NON-CONFIRMATORY under
section 4.7.

**An auditability gap, reported because it is not closed.** `_r1_pair_facts` emits aggregate
counts per pair and not the occurrence keys or heading texts, so the scored artifact alone
cannot show WHICH item drove the FAIL or confirm that the four matched occurrences bind the
intended printed starts. Both were established out of band against the committed
adjudications for this entry and are not reconstructible from `metrics.json`.

### A62.2 — the heading population is unsettled for running page furniture, and R1's verdict turns on it

**This qualifies A62.1 and partly corrects it.** A62.1 recorded that four of R1's five
denominator-bearing occurrences are bill designators carrying the fine role `other`, and argued
the role was not causal because any one-sided occurrence fails both dimensions identically. That
is true of the role LABEL and beside the point about the POPULATION. Recomputed over the same
committed answers, with running page designators removed from both sides of every pair:

| R1 text, AI route | numerator / denominator | ratio | verdict |
|---|---|---|---|
| as scored | 4 / 5 | 0.80 | **FAIL** |
| excluding running designators | 1 / 1 | 1.00 | **PASS** |

The single occurrence that earns no numerator is `•S 1609 PCS`, reported on the repeat
presentation and not on the primary. It is a running page designator. Removing designators leaves
one occurrence, `SEC. 504.`, matched and agreeing on both text and role. **So the R1 text FAIL,
and with it section 5.6's void of M2 and M3, rests entirely on whether a running page designator
is a heading.**

**The two routes answer that question differently, and the frozen prompt does not settle it.**

| | headings reported | running page designators | roles |
|---|---|---|---|
| AI, 122 answers | 95 | **23** | section 32, account 23, other 35, agency 4, grouping 1 |
| human, 45 answers | 33 | **0** | section 9, UNREADABLE 23, agency 1 |

Twenty-one designators carry a leading dagger or bullet (`†HR 6157 EAS`, `•S 1609 PCS`,
`•HR 6147 RH`, `•HR 7611 RH`, `•S 2976 PCS`, `•S 4663 IS`, `•HR 5961 RH`); two more are the same
running designator without the mark (`HR 7617 RFS`, `HR 8469 PCS`). The human reported none of
them across any answer.

`adjudicator_prompt.md` defines a heading by printed composition alone: "centered, or set in
capitals, or set in italic, or set in a distinctly larger or heavier face, or otherwise
typographically separated from the paragraphs around it." Its exclusion list is "running body
text, ordinary paragraphs, tables of figures, dollar amounts, and the small numbers printed in
the left margin." A page-foot bill designator is set in bold capitals and is typographically
separated, and running page furniture is not excluded. **On a literal reading of the frozen
prompt the AI route is correct and the human route is applying an unstated exclusion.** Neither
is transcribing wrongly; the instrument does not say which is intended.

This is a definitional gap in a frozen document, so it is recorded, not repaired. Deciding it now,
having seen that one answer yields R1 PASS and the other R1 FAIL, is the substitution
PRE-REGISTRATION 4.7 exists to prevent. What the run establishes is that the gap exists and that
it is load-bearing.

**Reach beyond R1, stated as exposure rather than as a correction.** 23 of the 95 AI-route
headings are running designators, so they also sit in the M1 recall denominator and the M2/M3
populations for the C estimand. No recomputation of those is offered here: doing so would be a
second post-hoc definition applied to a result already in hand.

### A62.3 — the two adjudication routes fail differently, and both failures are systematic

The N-A and N-B control failures recorded in the scoring commit are not scattered unreliability.
Both routes were examined against the rendered images they were shown.

**The human route silently repairs spacing defects.** N-A outcomes by mutation variant:

| variant | AI | human |
|---|---|---|
| DELETE_ONE_WORD | 3/3 | 3/3 |
| WELD_TWO_WORDS | 3/3 | **0/3** |
| SPLIT_ONE_WORD | 1/2 | **0/2** |

Every deleted word is caught; every spacing mutation is normalised away. Three of the five
spacing fixtures carry no strike-through and render cleanly at 300 DPI in a serif face:
`OPERATIONSAND SUPPORT` is plainly legible and was transcribed `OPERATIONS AND SUPPORT`. This is
the failure class N-A exists to detect, and it is also the defect class the STUDY exists to
measure, so it bears directly on the human route's fitness as ground truth for weld and split
errors.

**The human route substitutes a familiar spelling.** `RESCISSION` appears as `RECISSION` in 3 of
4 human headings and twice more in human free-text notes; the AI route has 4 of 4 correct and no
substitutions. Both N-B failures are this substitution. The images unambiguously print
`RESCISSION`. Both behaviours are reading-for-meaning: normalise the spacing, correct the word.

**One N-A fixture is confounded and is the AI route's only N-A failure.** A SPLIT was applied to a
heading already carrying strike-through markup, and the strike line bridges the inserted gap. Both
routes read one word, and the AI's committed note reasons explicitly that the gap is a strike
artifact. The fixture's `mutation_evidence` validates the text layer only and asserts nothing
about legibility in the render. Tracked as issue 727 and NOT repaired here: `control_fixtures.json`
is on the result-bearing manifest, so editing it would retire the standing authorization and
invalidate the scored metrics, and rebuilding an instrument after seeing which result it produced
is the same post-hoc substitution refused above. Setting that fixture aside, the AI route is 8/8
on N-A and 8/8 on N-B.

**What the C-audit does and does not corroborate.** The 25 C-audit stimuli carry both routes'
answers; 16 of 25 agree exactly on text and role. Neither control behaviour recurs there, and that
is expected rather than reassuring: the C-audit contains no injected spacing defects to normalise
and few instances of the substituted word, so it cannot detect either. Of the 9 differences, 4 are
the designator disagreement of A62.2, 2 are role-only (the human marking `UNREADABLE` on text both
routes transcribed identically), and 3 are human transcription or segmentation errors confirmed
against the images: `SEC. 214.` read as `SEC. 215.` and merged with the following heading, an
omitted `SEC. 722.`, and a stray quotation mark with trailing space. On every one of the three the
AI route matches the image.

**Direction, not rate.** One human across 8 N-A fixtures, 8 N-B fixtures and 25 C-audit stimuli.
The mechanisms are established; the frequencies are not.

### A62.4 — the running-designator question cannot be settled on the frozen text, and R1's failure is re-attributed

**This resolves the question A62.2 left open by establishing that it is not resolvable on the
instrument, and it corrects A62.2's account of what the R1 failure is evidence of.** Nothing here
changes a threshold, a metric definition, a selection rule or any committed value, and nothing is
recomputed.

**A62.2's conclusion is confirmed, on evidence A62.2 did not have. The frozen prompt does not
settle it.**

The reason is not that the definition is vague. It is that **the compositional test over-generates,
and every reader silently reads it down.** The first property in the definition's list is
"centered". A centered page folio is centered, is typographically separated from the text block,
and is not one of "the small numbers printed in the left margin", which are the marginal line
numbers. On a strict compositional reading a page number is therefore a heading.

**No one read it that way.** The AI route's notes discuss a page folio in **25** answers and report
one as a heading in **none**. Across both routes, over all 167 committed answers, a bare-number
heading is reported **zero** times. Two of those folio exclusions sit in the R1 pair that agrees:
`9bf5371acb85cb21` and `5b3e82d843a78143` each report `SEC. 504.` and each explicitly set aside a
centered folio, one of them the numeral `504` itself.

So the compositional test is universally applied subject to an unstated page-furniture carve-out.
**The frozen text nowhere says where that carve-out's boundary runs, and that boundary is exactly
the question.** It excludes folios on everyone's reading. Whether it also excludes a page-foot bill
designator is what the instrument does not say.

This also disposes of the strongest argument for the literal reading, which is worth recording
because it is the one a reader reaches for first: that the exclusion list names left-margin numbers
and so shows the drafter had page furniture in view and enumerated it deliberately. The list
demonstrably fails to cover furniture that every reader excluded regardless. It is an incomplete
enumeration, not a considered one, and it cannot bear the weight of an expressio unius inference.

**Two further readings were tested and neither settles it.** "Judge this visually, from composition
alone" is the prompt's own instruction to prefer composition over function, and it is the best
argument that a designator is a heading; but it is the same instruction that would admit folios, so
it cannot be applied strictly and the question of how far to read it down returns unanswered.
Against it, a structural presupposition runs through the fields surrounding the definition: every
`role` label but `other` names a structural element of an appropriations bill, and `parent` asks
for "the nearest heading above this one that **this heading sits under**". `other` does not resolve
this, because it classifies something already determined to be a heading rather than conferring
heading-hood on anything typographically distinct.

**THE INSTRUMENT FINDING.** `adjudicator_prompt.md` defines a heading compositionally, surrounds it
with fields that presuppose structure, and states no rule for page furniture beyond one incomplete
example. A successor instrument should settle running page furniture in one explicit sentence
rather than leave it to be inferred from a composition test that, read strictly, admits page
numbers.

**THE CORRECTION: the R1 text FAIL is not a disagreement between routes.**

A62.2 presents the gap as AI route against human route and infers that the definitional answer
decides whether the text metrics stand. **A62.2's arithmetic sensitivity is not disputed here**:
filtering designators does change R1 from 0.80 to 1.00. What does not hold is the attribution.

**Every R1 pair is on the AI route.** `metrics.json` `r1_reliability` carries `n_pairs` 6 and
`route` reads `ai` on all six. The human route contributes no R1 pair, having been removed from R1
by A48, and carries no record at all for either id in the failing pair. **The human route is not
party to this failure.**

**Both presentations print the designator, and the adjudicator saw it both times.** The pair is
primary `265fdcf236211f36`, repeat `8f6286a669bc6f38`. Section 5.6 specifies an R1 repeat as the
same region "re-rendered at a different but visually equivalent scale so they cannot be recognised
by hash", and that is what these are: 1499x1208 against 1649x1328, a uniform 1.100 scale, mean
absolute greyscale difference 2.6/255 after resampling to a common size, ink fraction 0.03246
against 0.03273 overall and 0.04252 against 0.04311 in the foot band. Both images print
`•S 1609 PCS` in bold at the foot, confirmed by inspecting the rendered images rather than the text
layer.

**The primary's committed note excludes it in terms:** "A bold page-foot line reading '•S 1609 PCS'
appears at the bottom... **It is set in bold and separated from the text block, but it is a page
footer/document identifier rather than a heading over any content**, so it is not reported as a
heading." The repeat reports the same string with role `other`. **This is not a perceptual miss. It
is one adjudicator applying two incompatible rules to the same object across two presentations of
the same region**, which is what section 5.6 says R1 exists to detect: "R1 exists because phase 1
found six identical stimuli answered 3 BOUNDARY / 3 NO_BOUNDARY and reported it as a defect in its
own work."

**The instability is specific to this class, which is the sharpest thing the run establishes.**

| page furniture class | admitted as a heading | excluded | consistent? |
|---|---|---|---|
| centered page folio | 0 | 25 | **yes** |
| page-foot bill designator | 23 | 2 | **no** |

The adjudicator holds a stable rule for folios and an unstable one for designators. The second
designator exclusion, `16f182372a39af6e` (`†HR 3237 EAS`, note: "page furniture (a running
footer/printer's mark), not a heading over any content"), sits in no R1 pair and moves no metric.
Every image whose last printed line carries the designator signature was accounted for: 12
reported, 2 reasoned away, none overlooked.

**THE CONSEQUENCE, stated without inventing a rule the protocol does not have.**

| reading | R1 text | protocol status |
|---|---|---|
| as scored, designators counted | 4/5 = 0.80 | **FAIL**; section 5.6 voids M2 and M3 |
| designators excluded | 1/1 = 1.00 | **PASS**, and a genuine one |

**The 1/1 is a real protocol PASS and is not dismissed here.** Section 5.6 sets no minimum pair
count and no minimum denominator, and A62.1 deliberately declined to add one after seeing that a
denominator of 5 produces a FAIL. Declaring 1/1 unevaluable now would install exactly that floor,
retrospectively, which is the substitution the register has already refused once. **It is a PASS on
one observation: very weak evidence, and NON-CONFIRMATORY under 4.7 like every other figure in this
run.** That is a statement about evidential weight, not about protocol status, and the two are kept
apart deliberately.

**But the exclusion reading is not the cheap rescue A62.2's two-row table implies, and three costs
go unrecorded there.** First, excluding designators removes **4 of the 5 denominator-bearing
occurrences, 3 agreeing and the 1 failing**. Second, R6.1 scores against a symmetric union
denominator, so ruling designators out does not simply delete the repeat's report: **it converts
that report into an over-trigger**, and reaching 1/1 requires a further, unstated filter on the
output population as well as on the reference. Third, the same ruling would reclassify **19 of the
65 C-frame headings** as reported-but-not-headings, which bears on M1 precision and on what N-C
exists to detect. None of that has been computed.

**So the definitional answer does not, by itself, decide whether the text metrics stand.** Under
the population as scored, R1 fails and section 5.6's void applies. Under the contrary reading, R1
passes on a single observation while the route acquires an unexamined over-reporting problem
elsewhere. Neither outcome is a confirmatory result about reliability.

**THE EXPOSURE, confirmed and resolved by population.** A62.2 gave 23 of 95, which is the count
across all 122 AI-route answers, and said those designators also sit in the M1 recall denominator.
Resolved against the key's frame flags:

| population | headings | of which running designators |
|---|---|---|
| C frame | 65 | **19** |
| controls | 25 | 0 |
| R1 repeats | 5 | 4 |
| all AI answers | 95 | 23 |

The C-frame total of 65 is exactly M1 recall's reported denominator, which corroborates the
mapping. **Roughly three in ten of the headings in the C estimand's adjudicated enumeration are
running page furniture whose status the instrument does not settle.** That is the exposure, and it
is larger for the C estimand than the 23-of-95 figure suggests.

**WHAT STANDS.** The metrics are left exactly as scored, because that is what the committed
apparatus produced and because nothing in this entry authorizes a change: R1 text 4/5 FAIL, M2 and
M3 void under section 5.6, and the 19 C-frame designators in place. Applying section 5.6's frozen
consequence is the conservative direction and the one A62.1 already committed to; declining to
apply it now, having seen that the other reading would avoid it, is the softening the register
exists to refuse.

**On PRE-REGISTRATION 4.7.** This question was examined in full knowledge of which answer yields
PASS and which yields FAIL. The outcome is that the instrument does not decide, which moves no
value and is the only outcome that does not substitute a post-hoc definition for a frozen one. The
exposure is stated rather than argued away: the examination happened after the results were
visible, and every figure it touches was already NON-CONFIRMATORY on other grounds.
