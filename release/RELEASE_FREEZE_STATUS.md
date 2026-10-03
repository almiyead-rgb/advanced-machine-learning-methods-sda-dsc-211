# Portal Release Freeze Status | حالة تجميد إصدار البوابة

**Target | الهدف:** `v1.1.0`  
**Repository | المستودع:** `almiyead-rgb/advanced-machine-learning-methods-sda-dsc-211`  
**Current state | الحالة الحالية:** `CANDIDATE — NOT PUBLISHED | مرشح — غير منشور`

## Automated controls | الضوابط الآلية

- [x] Portal structure and bilingual quality check
- [x] Required section and link validation
- [x] Canonical URL, hreflang and Course JSON-LD validation
- [x] Portal/learner-template coordination validation
- [x] Deterministic candidate manifest generation

## Manual and coordinated controls | الضوابط اليدوية والمنسقة

- [ ] Hosted-browser desktop review completed
- [ ] Tablet and mobile-width review completed
- [ ] Keyboard and focus review completed
- [ ] Zoom-to-200% review completed
- [ ] Contrast and screen-reader review completed
- [ ] Hosted Colab acceptance completed for the learner template
- [ ] Private evaluator and submission registry tested
- [ ] Portal and learner candidate manifests cross-checked
- [ ] Final portal content freeze approved
- [ ] Final `portal_release_manifest.json` generated after freeze
- [ ] Coordinated merge and `v1.1.0` publication approved

## Freeze rule | قاعدة التجميد

The portal must not be merged or published independently of the learner template. Publication is authorised only after the hosted browser record, hosted Colab record, private controls and final manifests are complete.

لا تُدمج البوابة أو تُنشر بصورة مستقلة عن قالب المتدرب. لا يعتمد النشر إلا بعد اكتمال سجل المتصفح وسجل Colab والضوابط الخاصة وManifest النهائي للمستودعين.
