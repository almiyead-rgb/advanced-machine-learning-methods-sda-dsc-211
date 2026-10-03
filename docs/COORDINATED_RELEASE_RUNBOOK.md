# Coordinated v1.1.0 Release Runbook | دليل الإصدار المنسق v1.1.0

## Current state | الحالة الحالية

`v1.1.0` is a controlled candidate, not a published release. The portal and learner template must move together. A successful automated candidate check does not authorise publication by itself.

الإصدار `v1.1.0` مرشح محكوم وليس إصدارًا منشورًا. يجب أن تتحرك بوابة الدورة وقالب المتدرب معًا. نجاح الفحص الآلي لا يمنح وحده تصريح النشر.

## Candidate identities | هويات المرشحين

| Component | Repository | Manifest | File count | Aggregate SHA-256 |
|---|---|---|---:|---|
| Portal | `almiyead-rgb/advanced-machine-learning-methods-sda-dsc-211` | `release/portal_release_manifest.candidate.json` | 19 | `6bad2a8f253eff07b9821921a24bc3aa351b69f9b52e95df40a287488132c589` |
| Learner template | `almiyead-rgb/sda-dsc-211-student-template` | `release/release_manifest.candidate.json` | 127 | `5e45aaf207fc67c605519e0fbdf8c67a9f67f5da42cc0954c0780544c3fc55c8` |

The first candidate manifests exposed a release-tool defect: directory globs such as `scripts/**` and `data/**` could resolve to directories without recursively adding their files. The manifest builders now recurse explicitly through every matched directory. The corrected identities above include nested release files rather than silently omitting them.

كشفت النسخة الأولى من الـManifest خللًا في أداة الجرد؛ فقد كانت أنماط المجلدات مثل `scripts/**` و`data/**` قد تُرجع المجلد نفسه دون إضافة ملفاته الداخلية. أصبحت الأدوات الآن تتوسع داخل كل مجلد بصورة صريحة، وتمثل الهويات المصححة أعلاه الملفات المتداخلة بدل إسقاطها بصمت.

These identities cover release-scoped content only. Operational records, private evidence, final tags and final merge SHAs are tracked separately.

تغطي هذه الهويات الملفات الواقعة ضمن نطاق الإصدار فقط. تحفظ سجلات التشغيل والأدلة الخاصة والوسوم النهائية وSHA الدمج النهائية خارج هذه البصمات.

## Required order | الترتيب الإلزامي

1. Complete hosted Colab acceptance on the learner-template candidate.
2. Complete hosted browser and accessibility QA on the portal candidate.
3. Create and test the private evaluator with hidden synthetic assets.
4. Create and test the private submission registry and immutable receipt flow.
5. Resolve every blocking observation and regenerate candidate manifests when release-scoped files change.
6. Run all learner-template quality gates and the portal coordinated-candidate check.
7. Approve a content freeze in both tracking issues.
8. Generate final manifests from the frozen trees.
9. Mark both pull requests ready for review.
10. Merge the learner template first.
11. Record its final merge SHA and create the learner release tag.
12. Update portal links only if the final learner identity requires it; otherwise do not alter the frozen portal content.
13. Merge the portal second.
14. Create the portal release tag and publish GitHub Pages.
15. Verify all public links, Colab launches and release assets after deployment.
16. Close the two release tracking issues only after the public verification record is complete.

## Automated coordination evidence | أدلة التنسيق الآلية

The workflow:

```text
Coordinated v1.1.0 Candidate Check
```

fetches both committed candidate manifests from their development branches and compares repository name, release version, file count and aggregate SHA-256 with:

```text
release/coordinated_candidate.json
```

A pass proves that the two public candidate identities agree with the coordinated record. It does not replace the manual or private gates below.

## Manual approval evidence | أدلة الاعتماد اليدوي

### Learner template

Complete:

```text
docs/HOSTED_COLAB_ACCEPTANCE_RECORD.md
```

Evidence must include the candidate manifest hash, tested browser/OS, notebook results, exported artifact checks, Notebook 99 result, Final Project Check URL and exact candidate commit. Do not place Google account details, private student data, hidden labels or tokens in the public record.

### Portal

Complete:

```text
docs/HOSTED_BROWSER_QA_RECORD.md
```

Evidence must cover desktop, tablet and mobile widths, keyboard navigation, 200% zoom, contrast, reduced motion, screen-reader landmarks, print preview and every required course link.

## Private controls | الضوابط الخاصة

The following repositories must be private and access-restricted:

```text
sda-dsc-211-private-evaluator
sda-dsc-211-private-submissions
```

Do not copy hidden labels, student identities, grades, receipt records or repository access credentials into either public course repository.

## Merge stop conditions | حالات إيقاف الدمج

Do not merge when any of the following is true:

- A required automated check is failing, pending or missing.
- Hosted Colab acceptance is incomplete or contains an unresolved blocker.
- Hosted browser/accessibility QA is incomplete or contains an unresolved blocker.
- The private evaluator cannot reproduce predictions from an exact SHA.
- The private registry cannot issue an immutable timestamped receipt.
- Candidate manifests differ from `release/coordinated_candidate.json`.
- A release-scoped file changed after the last candidate manifest was generated.
- The portal and learner assessment, submission or version signals disagree.
- Hidden data or personal information appears in a public repository.

## Post-release verification | التحقق بعد النشر

Record:

```text
Learner merge SHA
Learner tag and release URL
Portal merge SHA
Portal tag and release URL
GitHub Pages deployment URL
Public verification timestamp
Final Colab launch checks
Final link and accessibility smoke result
```

The public page must continue to state that it is an educational portal prepared by Meaad Al-Marri and is not an official SDAIA account.
