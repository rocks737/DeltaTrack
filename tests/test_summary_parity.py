"""Summary parity between the two canonical producers (#706).

ADR 0006 sells pipeline neutrality: "a diff produced from XML inputs and a diff
produced from PDF inputs share this shape." The ``summary`` object broke that
promise — the XML producer seeded five keys (always including ``unchanged`` and
its zeros), while the PDF producer built a ``Counter`` over the change types
actually present and had no ``unchanged`` kind to emit at all. A consumer that
enumerates summary keys got five names from one pipeline and four from the
other for identical legislative content.

The fix is the issue's Option A: stop emitting ``unchanged`` from the XML
producer. Nothing is lost — the value was provably constant at 0 on every
document a shipped entry point produced, because the canonical adapter drops
``unchanged`` entries before serializing and no production caller can opt back
in since #693.

These tests run both producers over the same committed bill pair through the
public compare entry points (``compare_xml`` / ``compare_pdfs``), the layer the
web app calls — the same "measure at the consumed output" rule
``test_canonical_baseline`` states. The corpus pair used here,
``118-hr-8752 1_reported-in-house -> 2_engrossed-in-house``, is the one the
issue measured on.

Note what these tests do NOT assert: that the two summaries carry the same
*counts*. They do not — the pipelines are free to disagree about how many
changes they find (the PDF path found 16 adds where XML found 18 on this pair,
and that is a fidelity difference, not a contract break). Parity here is about
the *key set*, the shape a machine consumer enumerates.
"""

from __future__ import annotations

import pytest

from deltatrack.compare.pdf import compare_pdfs
from deltatrack.compare.xml import compare_xml
from tests.corpus_paths import fixture_path

pytestmark = pytest.mark.slow

_V1_STEM = "1_reported-in-house"
_V2_STEM = "2_engrossed-in-house"

#: The four canonical keys of schema/canonical-diff.md's prose contract. Zero-count
#: keys MAY be omitted per that contract, so a consumer must tolerate absence of
#: any of them — but no producer may emit a key outside this set.
CANONICAL_SUMMARY_KEYS = frozenset({"added", "removed", "modified", "moved"})


def _pair() -> tuple[bytes, bytes, bytes, bytes] | None:
    """Both sides of the 118-hr-8752 1->2 pair, XML and PDF, or None if absent.

    The XML and PDF fixtures are committed separately (format parity in the
    corpus is deliberately partial), so a missing side skips rather than
    asserting less — the same fail-open rule ``test_front_matter_parity`` uses.
    """
    xml_v1 = fixture_path("118-hr-8752", f"{_V1_STEM}.xml")
    xml_v2 = fixture_path("118-hr-8752", f"{_V2_STEM}.xml")
    pdf_v1 = fixture_path("118-hr-8752", f"{_V1_STEM}.pdf")
    pdf_v2 = fixture_path("118-hr-8752", f"{_V2_STEM}.pdf")
    if not all(p.exists() for p in (xml_v1, xml_v2, pdf_v1, pdf_v2)):
        return None
    return xml_v1.read_bytes(), xml_v2.read_bytes(), pdf_v1.read_bytes(), pdf_v2.read_bytes()


def test_summary_keys_are_canonical() -> None:
    """Every key each producer emits is one of the four the contract names.

    Red before #706's fix: the XML producer emitted a fifth key, ``unchanged``,
    that the prose contract does not name and the PDF producer never emits.
    """
    pair = _pair()
    if pair is None:
        pytest.skip("118-hr-8752 XML/PDF pair not present")
    xml_v1, xml_v2, pdf_v1, pdf_v2 = pair

    xml_summary = compare_xml(xml_v1, xml_v2)["summary"]
    assert set(xml_summary) <= CANONICAL_SUMMARY_KEYS, (
        f"XML summary carries non-canonical keys: {sorted(set(xml_summary) - CANONICAL_SUMMARY_KEYS)}"
    )

    pdf_summary = compare_pdfs(pdf_v1, pdf_v2)["summary"]
    assert set(pdf_summary) <= CANONICAL_SUMMARY_KEYS, (
        f"PDF summary carries non-canonical keys: {sorted(set(pdf_summary) - CANONICAL_SUMMARY_KEYS)}"
    )


def test_xml_pdf_summary_keys_agree_for_the_same_pair() -> None:
    """Both pipelines report the same summary key set for the same bill pair.

    The red state #706 measured: XML ``['added', 'modified', 'moved',
    'removed', 'unchanged']`` against PDF ``['added', 'modified', 'moved',
    'removed']``. Counts may legitimately differ between pipelines; the key set
    — the shape a machine consumer enumerates — may not.
    """
    pair = _pair()
    if pair is None:
        pytest.skip("118-hr-8752 XML/PDF pair not present")
    xml_v1, xml_v2, pdf_v1, pdf_v2 = pair

    xml_keys = set(compare_xml(xml_v1, xml_v2)["summary"])
    pdf_keys = set(compare_pdfs(pdf_v1, pdf_v2)["summary"])
    assert xml_keys == pdf_keys, (
        "summary key sets diverge between pipelines for the same bill pair: "
        f"XML-only={sorted(xml_keys - pdf_keys)} PDF-only={sorted(pdf_keys - xml_keys)}"
    )
