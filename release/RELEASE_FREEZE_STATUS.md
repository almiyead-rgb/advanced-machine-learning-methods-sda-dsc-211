# Portal Release Freeze Status | حالة تجميد إصدار البوابة

**Target | الهدف:** `v1.1.0`  
**Repository | المستودع:** `almiyead-rgb/advanced-machine-learning-methods-sda-dsc-211`  
**Current state | الحالة الحالية:** `CANDIDATE — NOT PUBLISHED | مرشح — غير منشور`

## Corrected candidate identity | هوية المرشح المصححة

```text
file_count: 19
aggregate_sha256: 6bad2a8f253eff07b9821921a24bc3aa351b69f9b52e95df40a287488132c589
```

The portal manifest builder now recurses through any matched directory instead of silently omitting nested files. The earlier 17-file identity is superseded.

أصبحت أداة Manifest الخاصة بالبوابة تتوسع داخل أي مجلد مطابق بدل إسقاط الملفات المتداخلة بصمت. أصبحت هوية 17 ملفًا السابقة ملغاة.

## Automated controls | الضوابط الآلية

- [x] Portal structure and bilingual quality check
- [x] Required section and link validation
- [x] Canonical URL, hreflang and Course JSON-LD validation
- [x] Portal/learner-template coordination validation
- [x] Deterministic recursive candidate manifest generation
- [x] Cross-repository candidate identity check

## Manual and coordinated controls | الضوابط اليدوية والمنسقة

- [ ] Hosted-browser desktop review completed
- [ ] Tablet and mobile-width review completed
- [ ] Keyboard and focus review completed
- [ ] Zoom-to-200% review completed
- [ ] Contrast and screen-reader review completed
- [ ] Hosted Colab acceptance completed for the learner template
- [ ] Private evaluator and submission registry tested
- [x] Portal and learner candidate manifests cross-checked automatically
- [ ] Final portal content freeze approved
- [ ] Final `portal_release_manifest.json` generated after freeze
- [ ] Coordinated merge and `v1.1.0` publication approved

## Freeze rule | قاعدة التجميد

The portal must not be merged or published independently of the learner template. Publication is authorised only after the hosted browser record, hosted Colab record, private controls and final manifests are complete.

لا تُدمج البوابة أو تُنشر بصورة مستقلة عن قالب المتدرب. لا يعتمد النشر إلا بعد اكتمال سجل المتصفح وسجل Colab والضوابط الخاصة وManifest النهائي للمستودعين.
