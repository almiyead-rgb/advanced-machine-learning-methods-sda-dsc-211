# Phase 6 — Coordinated Release Integrity | المرحلة 6 — سلامة الإصدار المنسق

## Decision | القرار

The portal remains a controlled `v1.1.0` candidate. This phase corrected recursive release inventory, established a cross-repository candidate identity and added an automated coordination gate. It did not authorise public deployment.

تبقى البوابة مرشحًا محكومًا للإصدار `v1.1.0`. صححت هذه المرحلة جرد ملفات الإصدار المتداخلة، وأنشأت هوية مشتركة للمستودعين، وأضافت بوابة تنسيق آلية. لم تمنح تصريح النشر العام.

## Manifest defect and correction | خلل Manifest وتصحيحه

The original portal and learner manifest collectors skipped files inside directories matched by patterns ending in `/**`. Both collectors now recurse explicitly through each matched directory.

كانت أدوات Manifest الأولى تتجاوز الملفات الموجودة داخل المجلدات المطابقة لأنماط تنتهي بـ`/**`. أصبحت الأداتان الآن تتوسعان داخل كل مجلد مطابق بصورة صريحة.

## Corrected candidate identities | الهويات المصححة

```text
Portal
file_count: 19
aggregate_sha256: 6bad2a8f253eff07b9821921a24bc3aa351b69f9b52e95df40a287488132c589

Learner template
file_count: 127
aggregate_sha256: 5e45aaf207fc67c605519e0fbdf8c67a9f67f5da42cc0954c0780544c3fc55c8
```

The earlier 17-file portal identity and 35-file learner identity are superseded.

## Implemented controls | الضوابط المنفذة

```text
release/coordinated_candidate.json
scripts/check_cross_repo_candidate.py
.github/workflows/coordinated_release_check.yml
docs/COORDINATED_RELEASE_RUNBOOK.md
```

The automated gate fetches both candidate manifests from their development branches and verifies:

- repository name,
- release version,
- file count,
- aggregate SHA-256,
- consistency between the files array and file count.

## Evidence | الأدلة

At coordinated commit `a78291e4d8b6d1a10c0adb89ee996c53f08c061d`:

| Gate | Run | Result |
|---|---:|---|
| Portal Quality Check | `37107651457` | PASS |
| Portal Release Candidate | `37107651453` | PASS |
| Coordinated v1.1.0 Candidate Check | `37107651450` | PASS |

## Separation of concerns | فصل المسؤوليات

The coordinated check proves that both public candidate manifests match the approved candidate record. It does not prove:

- hosted Colab usability,
- browser or screen-reader usability,
- private evaluator effectiveness,
- private submission receipt integrity,
- final merge/tag identity,
- public deployment success.

These remain separate mandatory gates.

## Remaining gates | البوابات المتبقية

- Hosted browser and accessibility QA.
- Hosted Colab acceptance against a complete learner project.
- Private evaluator implementation and hidden-asset test.
- Private submission registry and receipt test.
- Final content freeze.
- Final manifests generated from frozen trees.
- Learner merge and tag, followed by portal merge and deployment.
- Post-deployment link, Colab and accessibility verification.

## Release status | حالة الإصدار

```text
PORTAL_AUTOMATED_QUALITY: PASS
CROSS_REPOSITORY_IDENTITY: PASS
HOSTED_BROWSER_QA: PENDING
HOSTED_COLAB_ACCEPTANCE: PENDING
PRIVATE_CONTROLS: PENDING
MERGE_AUTHORISED: NO
PUBLICATION_AUTHORISED: NO
```
