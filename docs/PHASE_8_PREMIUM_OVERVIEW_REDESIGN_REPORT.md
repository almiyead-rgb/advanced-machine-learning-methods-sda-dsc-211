# Phase 8 â€” Premium course overview redesign
# Ø§Ù„Ù…Ø±Ø­Ù„Ø© 8 â€” è¥Ø¹Ø§Ø¯Ø© ØªØµÙ…ÙŠÙ… Ø§Ù„ÙˆØ§Ø¬Ù‡Ø© Ø§Ù„ØªÙ†ÙÙŠØ°ÙŠØ© Ù„Ø¯ÙˆØ±Ø©

## Decision | Ø§Ù„Ù‚Ø±Ø§Ø±

The course portal was redesigned around a clear information hierarchy rather than one dense content block. The supplied MEAAD visual identity is now placed in a dedicated square logo tile, followed by the Arabic course title and English subtitle.

Ø£Ø¹ÙŠØ¯ ØªØµÙ…ÙŠÙ… Ø¨ÙˆØ§Ø¨Ø© Ø§Ù„Ø¯ÙˆØ±Ø© ÙˆÙÙ‚ ØªØ³Ù„Ø³Ù„ Ø¨ØµØ±ÙŠ ÙˆØ§Ø¶Ø­ Ø¨Ø¯Ù„ ØªØ¬Ù…ÙŠØ¹ Ø§Ù„Ù…Ø¹Ù„ÙˆÙ…Ø§Øª ÙÙŠ ÙƒØªÙ„Ø© ÙˆØ§Ø­Ø¯Ø©. ÙˆÙØ¹Øª Ø§Ù„Ù‡ÙˆÙŠØ© Ø§Ù„Ø¨ØµØ±ÙŠØ© Ø§Ù„Ù…Ø±ÙÙ‚Ø© Ø¯Ø§Ø®Ù„ Ù…Ø±ØªØ¹ Ù…Ø³ØªÙ‚Ù„ ÙŠÙ„ÙŠÙ‡Ø§ Ø§Ø³Ù… Ø§Ù„Ø¯ÙˆØ±Ø© Ø¨Ø§Ù„Ø¹Ø±Ø¨ÙŠØ© ÙˆØ§Ù„Ø¹Ù†ÙˆØ§Ù† Ø§Ù„Ø¥Ù†Ø¬Ù„ÙŠØ²ÙŠ.

## Implemented UX structure | Ø§Ù„Ù‡ÙŠÙƒÙ„ Ø§Ù„Ù…Ù†ÙØ°

 1. Premium hero with the supplied logo, course name, value proposition and primary actions.
 2. Separate course overview, five-day learning journey, outcomes and assessment panels.
 3. Beginner start path with direct readiness, repository-template and tool-guide links.
 4. Individual Day 1â€“5 cards with one Colab action and one guide action per day.
 5. Separate project workspace for data, report templates and final presentation.
 6. Separate requirements and assessment sections.
 7. Separate final-submission flow and learner-support library.
 8. System Architecture section positioned at the end of the portal.

## System architecture | Ù…Ø¹Ù…Ø§Ø±ÙŠØ© Ø§Ù„Ù†Ø¸Ø§Ù…>

```text
Student
â†’ GitHub Student Repository
â†’ Google Colab Notebooks 01â€“05
â‚‚ Data, Models and Evidence
â‚‚ Notebook 99 Final Evaluation
â‚‚ Final Presentation and Private Submission
```

The architecture also states the privacy boundary: hidden evaluator data, grades, identities and receipts are not exposed through the public portal.

## Visual system | Ø§Ù„Ù†Ø¸Ø§Ù… Ø§Ù„Ø¨ØµØ±ÙŠ
B‹HØ\›HÜ™X[K™ZYÙK›XÚÈ[™™\İ˜Z[™YÛÛ[]H\š]™Yœ›ÛHHİ\YYY[]K‚‹HØ\™È[™ÙXİ[ÛœÈÙ\\˜]YH\œÜÙK›İH\˜š]˜\HXÛÜ˜][Û‹‚‹H[™Û\Ú[YÈ\˜XšXË\šYÚ[™›Ü›X][ÛˆZ\š[™Ë‚‹H™\ÜÛœÚ]™H[Øš[HİXÚÚ[™Ë‚‹HÙ^X›Ø\™›Øİ\ËÚÚ\[šË™YXÙY[İ[Ûˆ[™š[İ\Ü‚‹HÛİ\œÙH™\Ûİ\˜Ù\È™[XZ[ˆ[šÙYÈHX›XÈİY[[\]NÈš]˜]HÛÛ›ÛÈ™[XZ[ˆ[œİXİÜ‹[Û›K‚‚ˆÈÈXØÙ\[˜ÙH]šY[˜ÙH6(ö+öa6*H6)öa6`¶*6b6a‚•HÜ[]X[]HÛÜšÙ›İÈ™\šYšY\Î‚‚‹HHİ\YYÙÛÈ\ÜÙ]\È™\Ù[[™\ÙYÂ‹H\˜XšXÈ[™[™Û\ÚÛİ\œÙH]\È\™H™\Ù[Â‹HH\˜Ú]Xİ\™HÙXİ[Ûˆ^\İÎÂ‹H[™\]Z\™YİY[ÙXİ[ÛœÈ^\İÂ‹H[ØØ[\ÜÙ]È™\ÛÛ™NÂ‹H™\ÜÛœÚ]™H[™™YXÙY[[İ[ÛˆÔÔÈ\™H™\Ù[Â‹HØ[›ÛšXØ[™Y›[™Ë”ÓÓ‹S[™HÑRPH\ØÛZ[Y\ˆ™[XZ[ˆ[Xİ‚