# Content Governance and Release Controls | حوكمة المحتوى وضوابط الإصدار

Owner: Meaad Al-Marri | ميعاد المري  
Course: SDA-DSC-211 — Advanced Machine Learning Methods

## Controlled repositories | المستودعات الخاضعة للحوكمة

| Repository | Role | Public status |
|---|---|---|
| `advanced-machine-learning-methods-sda-dsc-211` | Course portal and public course guidance | Public |
| `sda-dsc-211-student-template` | Learner project template, labs, data, self-checks | Public |
| `sda-dsc-211-private-evaluator` | Hidden assessment data and instructor-only evaluation | Private — planned |
| `sda-dsc-211-submission-registry` | Private submission receipt and cohort register | Private — planned |

## Branch model | نموذج الفروع

- `main`: published and learner-safe release only.
- `develop/bilingual-v1.1.0`: controlled development for the bilingual redesign.
- Feature branches: one bounded change, one acceptance report.
- No direct experimental changes on `main`.

## Release policy | سياسة الإصدار

A release may be tagged only after:

1. Portal validation passes.
2. All required bilingual checks pass.
3. Notebooks `00–05` execute in fresh kernels.
4. Notebook `99` passes against a completed fixture project and fails against known incomplete fixtures.
5. Public repositories contain no hidden labels, credentials, instructor-only data, or private submission records.
6. Colab CPU validation is completed from a clean Google account.
7. README, portal version, release notes, hashes, and manifests agree.
8. The exact release commit is signed or verified by GitHub.

لا يُنشأ وسم إصدار إلا بعد اجتياز فحوص البوابة والمحتوى الثنائي وتشغيل الدفاتر والتحقق من دفتر 99 وسلامة حدود البيانات العامة والخاصة واختبار Colab من جلسة نظيفة وتطابق رقم الإصدار والبصمات والملفات المرجعية.

## Source of truth | مصادر الحقيقة

| Information | Authoritative source |
|---|---|
| Course title, code, duration, learning outcomes | `content/course_metadata.yml` |
| Canonical English–Arabic terminology | `content/terminology.yml` |
| Assessment weights | Student template `RUBRIC.md` |
| Required submission files | `scripts/submission_contract.py` |
| Python package versions | `requirements-colab.txt`, `constraints.txt` |
| Learner project data schema | `data/data_contract.json` |
| Public release summary | `RELEASE_NOTES.md` and GitHub Release |

A duplicated value must not be changed in one location only. The change owner must update every dependent file or automate generation from the authoritative source.

## Change classes | تصنيف التغييرات

### A — Editorial

Spelling, spacing, translation quality, link labels, and accessibility text. Must not change scientific meaning or learner requirements.

### B — Instructional

Objectives, explanations, learner tasks, sequencing, rubrics, or completion criteria. Requires course-alignment review.

### C — Technical

Notebook logic, data contracts, package versions, hashes, tests, inference interface, or assessment checks. Requires fresh-kernel execution and regression testing.

### D — Assessment-sensitive

Hidden evaluation logic, scoring boundaries, anti-hardcoding tests, labels, or submission registry. Must remain private and must never be committed to public repositories.

## Approval evidence | أدلة الاعتماد

Each phase report must record:

- Files changed.
- Reason for change.
- Learner impact.
- Tests executed.
- Known limitations.
- Commit SHA.
- Decision: approve, revise, or reject.

## Privacy and attribution | الخصوصية والنسبة

- Learners use a student code in public repositories.
- Full names, grades, receipts, private email addresses, and access tokens must not appear in public Issues or commits.
- Instructor attribution remains visible in the portal, template, reports, and release notes.
- SDAIA Academy links are references to the training entity; the repositories must not claim to be official SDAIA accounts.

## Deprecation policy | سياسة الإيقاف

A published learner link is not deleted without one of these controls:

1. A redirect.
2. A replacement notice.
3. One release cycle of overlap.
4. A documented migration path.

## Definition of done | تعريف الاكتمال

A phase is complete only when its outputs are committed, independently reviewable, tested against explicit acceptance criteria, and reversible without damaging the published release.
