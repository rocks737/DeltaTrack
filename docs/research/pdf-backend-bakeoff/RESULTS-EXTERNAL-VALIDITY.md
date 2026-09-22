# Results: external-validity run — VOID

- Status: **the run is void under its own pre-registered controls.** It produces no
  comparative architecture result and none should be read out of it.
- Population: 17 confirmatory-holdout documents, 4190 pages, frozen before execution.
- Protocol: [`validation/external-validity/PRE-REGISTRATION.md`](validation/external-validity/PRE-REGISTRATION.md).
  Deviation register: [`validation/external-validity/results/DEVIATIONS.md`](validation/external-validity/results/DEVIATIONS.md)
  (entries through A62.4).
  Scored output: [`validation/external-validity/results/metrics.json`](validation/external-validity/results/metrics.json).
  **Every figure below is derivable from those two files.**
- Supersedes nothing in [`RESULTS.md`](RESULTS.md) or
  [`RESULTS-CONFIRMATORY.md`](RESULTS-CONFIRMATORY.md). This run was designed to test
  whether their findings generalise to unseen documents. **It could not, because the
  instrument failed, not because the finding failed.**
- Input to [DeltaTrack#112](https://github.com/AgoraDMV/DeltaTrack/issues/112).

---

## Headline

**§5.6's N-B control failed, and §5.6's consequence for that is "run void".**

The study did not measure the architectures. It measured its own adjudication instrument,
and the instrument did not survive. The useful finding is about the instrument.

---

## What voided it

Controls require both adjudication routes to pass on every fixture, with no tolerance.

| control | what it tests | AI route | human route | combined | status |
|---|---|---|---|---|---|
| **N-A** | injected defects are transcribed, not repaired | 7/8 | **3/8** | 10/16 | **FAIL** |
| **N-B** | unambiguous XML-corroborated headings agree | **8/8** | **6/8** | 14/16 | **FAIL** |
| **N-C** | no heading reported where none is printed | 4/4 | 4/4 | 8/8 | PASS |

§5.6: N-A failure voids M2/M3; **N-B failure voids the run**, because it shows the
adjudicator is unreliable independently of any architecture.

**Every N-B failure and five of six N-A failures are on the human route.** The AI's single
N-A failure is fixture `ab2f34a86416bf77`, where *both* routes failed identically — a
strike-through bridges the injected gap so the defect is not legible in the render. That is
a fixture defect, tracked as issue #727. Setting it aside, the AI route is **N-A 8/8,
N-B 8/8, N-C 4/4**.

### The human route repairs the defect class the study exists to measure

Both failure modes are systematic, not noise:

| human-route behaviour | evidence |
|---|---|
| **normalises spacing defects** | DELETE_ONE_WORD 3/3, but **WELD 0/3** and **SPLIT 0/2**. `OPERATIONSAND SUPPORT` transcribed `OPERATIONS AND SUPPORT`; `OPERA TIONS AND SUPPORT` transcribed `OPERATIONS AND SUPPORT`. |
| **substitutes a familiar spelling** | `RESCISSION` read as `RECISSION`. This is both N-B failures. The AI route is 4/4 correct on the same word. |

Three of the five spacing fixtures carry no strike-through and render cleanly at 300 DPI.
The defects were legible; they were read through. **Weld and split are precisely the
defect classes the bake-off exists to detect, so the ground truth silently repaired the
thing being measured.** That is why the failure is disqualifying rather than a tolerance
question.

On the 25-stimulus C-audit where both routes answered the same images, they agree exactly
on text and role in **16 of 25**. Of the 9 differences, 4 are the designator question
below, 2 are role-only, and 3 are human transcription or segmentation errors confirmed
against the rendered images. On all three the AI route matches the image.

---

## The second instrument finding: the heading definition is underdetermined

The frozen adjudicator prompt does not settle whether running page furniture is a heading,
and the gap is load-bearing.

Its definition is compositional — "centered, or set in capitals, or set in italic, or set
in a distinctly larger or heavier face". Its first listed property is *centered*, and a
centered page folio is centered, is typographically separated, and is not one of "the small
numbers printed in the left margin". **Read strictly, the test makes page numbers
headings.** No one read it that way: the AI notes discuss a page folio in 25 answers and
report one as a heading in none, and across all 167 committed answers neither route ever
reports a bare-number heading.

So every reader applies an unstated page-furniture carve-out that the text never defines.
It excludes folios on everyone's reading. Whether it also excludes a page-foot bill
designator (`•S 1609 PCS`) is exactly what the instrument does not say — and the routes,
and the AI route internally, went both ways:

| page furniture class | admitted as a heading | excluded | consistent? |
|---|---|---|---|
| centered page folio | 0 | 25 | **yes** |
| page-foot bill designator | 23 | 2 | **no** |

This surfaced through the R1 test-retest control, which failed at 4/5 against a 0.90
threshold. The failing pair is one region presented twice at visually equivalent scale.
**Both presentations print the designator and the adjudicator saw it both times** — its own
note on the one it declined reads "set in bold and separated from the text block, but it is
a page footer/document identifier rather than a heading over any content". One adjudicator,
one frozen prompt, two incompatible rules. Full analysis: register entry A62.4.

Roughly three in ten of the headings in the C-frame's adjudicated enumeration (19 of 65)
are running page furniture whose status the instrument does not settle.

---

## Why RQ1 and RQ2 have no answer

**RQ1 (comparative) — no evidence base.** RQ1's primary frame is the D-frame, a census of
every region where the two architectures' output differs, and the design required *every
D-frame item human-adjudicated*. The D census is 13,992 regions. Forty-five human answers
exist in total, of which 25 are the C-audit. The human arm was never executed at census
scale; the A27.3 budget and its A48 implementation resolved D-only items to no required
route. **RQ1 was foreclosed before the controls ever ran**, and the control failure is a
second, independent reason it cannot be answered.

**RQ2 (absolute) — computed, then voided.** The C-frame produced figures, but M2 and M3 are
void under §5.6 via the R1 text failure, and the whole run is void via N-B. Recorded for the
register only, not to be cited:

| metric | value | status |
|---|---|---|
| M1 precision | 38/42 = 0.905 | reported, run void |
| M1 recall | 38/65 = 0.585 | reported, run void |
| M2 exact heading text | 10/38 = 0.263 | **void** (R1 text FAIL) |
| M3 clean rate | 10/65 = 0.154 | **void** (R1 text FAIL) |
| M5 role agreement | 35/36 | reported, run void |

**The C-frame cannot separate the architectures in any case**: H and X produce identical
values on every pooled C metric. Cross-engine qualification returned
`both_headlines_qualified: false` with no document-level qualification for either RQ.

Every figure in this run is additionally labelled NON-CONFIRMATORY under §4.7, because
post-boundary deviations (A45, A48) were made after results were visible.

**The population was not the problem.** §4.5 adequacy returned **GENERALISABLE**: 2583
heading occurrences of the counted kinds across 7 filled strata, well above the
5-strata / 300-occurrence floor. S1 fired, all 17 documents scored, and the extraction ran
clean across all 4190 pages. **What failed was adjudication**, which is why a bigger or
different document sample would not help.

---

## What is worth keeping

1. **An AI image-adjudicator outperformed human ground truth on this study's own controls**
   (8/8 vs 6/8 on N-B; 8/8 vs 3/8 on N-A excluding the illegible fixture). The study was
   designed on the assumption that human adjudication is the reference. On the defect classes
   the controls probe, that assumption did not hold.
2. **Human adjudicators read for meaning.** They normalise spacing and correct spelling
   without noticing. Any future protocol that uses human transcription as ground truth for
   character-level defects needs a control that can catch this, and needs to expect it.
3. **A compositional heading definition needs an explicit page-furniture rule.** A successor
   instrument should settle running headers, footers, folios and bill designators in one
   sentence rather than leave them to be inferred.
4. **M3's boundary census found 445 TEXT_ERROR but zero WELD and zero SPLIT** across 975
   outcomes. Given that the human route demonstrably normalises welds and splits away, this
   is worth a successor's attention. It is flagged as a question, not a conclusion.

## What is not worth doing

Re-running the human arm. Both failure modes are systematic rather than noisy, so a larger
human sample fails the same way. Rescuing RQ2 means re-adjudicating a fresh population under
a new authorization, at significant cost, with no reason to expect a different result.

## Known open defects, not exercised by this void run

- **#726** — the scorer emits `NOT_EVALUABLE_NO_R1_PAIRS` while `rule3_gates` accepts only
  `NOT_EVALUABLE`, so a zero-evidence R1 falls through to PASS. Fail-open. Not triggered
  here, since R1 failed on a non-empty denominator. **Fix before any successor run.**
- **#727** — the N-A fixture above whose injected defect is not legible in the render. Its
  `mutation_evidence` validates the text layer only and asserts nothing about legibility.
- **G2** — the baseline fixture is already invalid, so several G2 controls pass for reasons
  unrelated to their labels.
- **No canonical decision operation.** `score_metrics.score_canonical()` loads committed
  artifacts and writes `metrics.json`; there is no equivalent on the decision side.
  `decide_architecture.decide()` exists, but every `DecisionInputs(...)` construction site is
  a control probe with supplied facts, and `results/scores.json` is never written. Not built
  here deliberately: the void verdict is already machine-computed and committed in
  `metrics.json` `control_verdicts`, so a decision module would re-emit a foregone conclusion.

## Reproduction

**On this branch.** `results/metrics.json` and the register through A62.4 are included, and
every figure in this document is derivable from them: control verdicts and the per-fixture
failures from `control_verdicts`, the R1 pair facts from `r1_reliability`, M1–M5 from
`headings_pooled.C`, the population verdict from `adequacy_4_5`.

**Not included, deliberately.** `results/oracle_adjudicated.json` and `ORACLE-PROVENANCE.json`
carry the adjudicated answers and are mode 0600 in the working tree. Publishing them would
expose answer-key material to any successor run, which the study's own contamination
apparatus exists to prevent. Re-deriving the raw per-answer counts quoted in A62.2 and A62.4
(designator and folio tallies, the 16/25 C-audit agreement) therefore requires the study
branch.

**The full apparatus** — the 307 MB answer key, `frames.json`, and the 15,437 rendered
stimuli — lives on the local branch `pdf-study-continuation-execution`, which is **not pushed**
because it tracks `oracle_key.json`. Preserve it as a bundle in `delta_track_mirror`.

Gate state at close: `x04_freeze_check` reports freeze integrity COMPLETE, 19/19 checks pass,
and `EXECUTION FORBIDDEN` pending a sequence-9 authorization that was deliberately not minted,
because nothing further is to be scored.
