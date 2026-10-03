# Phase 5 · Portal Release Candidate Freeze Controls
# المرحلة 5 · ضوابط تجميد مرشح إصدار البوابة

## Scope | النطاق

This phase persisted the deterministic portal candidate manifest and added the manual browser-acceptance record required before publication.

ثبّتت هذه المرحلة Manifest حتميًا لمرشح البوابة وأضافت سجل اعتماد المتصفح اليدوي المطلوب قبل النشر.

## Implemented | ما تم تنفيذه

- Updated `Portal Release Candidate` to generate and persist `release/portal_release_manifest.candidate.json` on the controlled development branch.
- Preserved a copy of the manifest in the workflow artifact.
- Added `docs/HOSTED_BROWSER_QA_RECORD.md` for desktop, tablet, mobile, keyboard, contrast and screen-reader evidence.
- Added `release/RELEASE_FREEZE_STATUS.md` with coordinated learner/portal release gates.
- Opened public tracking issue `#2` without placing private learner or submission information in the portal repository.
- Kept final tag and commit identity outside the manifest to avoid circular identity.

## Candidate integrity identity | هوية سلامة المرشح

```text
release_version: v1.1.0
file_count: 17
aggregate_sha256: e6e8e85e9c3f0cedb7c1e07392190d4405ad9b2cef3492f148c86e5b362af329
```

This candidate inventory may change until browser QA, hosted Colab acceptance and private controls are complete.

قد يتغير جرد المرشح حتى اكتمال اختبار المتصفح واعتماد Colab والضوابط الخاصة.

## Automated evidence | الأدلة الآلية

- Portal Quality Check: PASS.
- Portal Release Candidate: PASS.
- Portal/learner-template coordination: PASS.
- Deterministic candidate manifest: generated and persisted.

## Deliberate limitations | الحدود المقصودة

- No claim is made that Chrome, Edge, mobile widths or screen readers have been manually accepted.
- No claim is made that hosted Colab acceptance has passed.
- No portal merge or GitHub Pages publication is authorised independently of the learner template.
- No final portal manifest, tag or public release is authorised.

## Release decision | قرار الإصدار

```text
PORTAL_CANDIDATE_READY_FOR_MANUAL_QA
NOT_AUTHORISED_FOR_MERGE_OR_PUBLICATION
```
