# Hosted Browser QA Record | سجل اختبار المتصفح المستضاف

**Release candidate | مرشح الإصدار:** `v1.1.0`  
**Portal repository | مستودع البوابة:** `almiyead-rgb/advanced-machine-learning-methods-sda-dsc-211`  
**Status | الحالة:** `PENDING MANUAL EXECUTION | بانتظار التنفيذ اليدوي`

> Automated HTML checks do not replace visual, keyboard or screen-reader testing in real browsers.  
> لا تحل فحوص HTML الآلية محل الاختبار البصري واختبار لوحة المفاتيح وقارئ الشاشة في متصفحات فعلية.

## Test identity | بيانات الاختبار

| Field | Value |
|---|---|
| Tester |  |
| Date and time |  |
| Candidate commit SHA |  |
| Portal candidate manifest aggregate SHA-256 |  |
| Published preview URL, if used |  |

## Browser and viewport matrix | مصفوفة المتصفح والعرض

| Browser / device | Width | English left and Arabic right | No horizontal overflow | Links and focus | Result |
|---|---:|---:|---:|---:|---|
| Chrome / Windows | 1366 px | ☐ | ☐ | ☐ | ☐ PASS ☐ FAIL |
| Chrome / Windows | 1024 px | ☐ | ☐ | ☐ | ☐ PASS ☐ FAIL |
| Chrome responsive view | 390 px | Stacked/readable | ☐ | ☐ | ☐ PASS ☐ FAIL |
| Edge / Windows | 1366 px | ☐ | ☐ | ☐ | ☐ PASS ☐ FAIL |
| Edge / Windows | 1024 px | ☐ | ☐ | ☐ | ☐ PASS ☐ FAIL |
| Edge responsive view | 390 px | Stacked/readable | ☐ | ☐ | ☐ PASS ☐ FAIL |

## Accessibility checks | فحوص إمكانية الوصول

| Check | Result | Notes |
|---|---|---|
| Skip link reaches the main content | ☐ PASS ☐ FAIL |  |
| Complete keyboard navigation | ☐ PASS ☐ FAIL |  |
| Visible focus indicator | ☐ PASS ☐ FAIL |  |
| Zoom to 200% without loss of content | ☐ PASS ☐ FAIL |  |
| Meaning does not rely on colour alone | ☐ PASS ☐ FAIL |  |
| Reduced-motion preference respected | ☐ PASS ☐ FAIL |  |
| Arabic and English reading order is sensible | ☐ PASS ☐ FAIL |  |
| Screen-reader landmarks and headings are understandable | ☐ PASS ☐ FAIL |  |
| Contrast reviewed for text, links and controls | ☐ PASS ☐ FAIL |  |
| A4 print preview remains readable | ☐ PASS ☐ FAIL |  |

## Functional checks | الفحوص الوظيفية

- [ ] Student-template repository opens.
- [ ] Readiness route opens.
- [ ] Notebooks 01–05 open in Colab.
- [ ] Notebook 99 opens.
- [ ] Rubric and submission guide open.
- [ ] Beginner support links open.
- [ ] Instructor attribution is visible.
- [ ] Non-official SDAIA disclaimer is visible in both languages.
- [ ] Assessment signals show 90 + 10, pass 70 and distinction 95.

## Failure record | سجل الفشل

```text
Browser and width:
Section or control:
Observed issue:
Screenshot reference:
Severity:
Corrective commit SHA:
Retest result:
```

## Acceptance decision | قرار الاعتماد

- [ ] **ACCEPTED** — all mandatory browser and accessibility checks passed.
- [ ] **REJECTED** — one or more mandatory checks failed.
- [ ] **DEFERRED** — testing is incomplete; no publication decision is made.

**Tester signature/name | اسم المنفذ:**  
**Approval date | تاريخ الاعتماد:**  
**Evidence location | موقع الأدلة:**  
