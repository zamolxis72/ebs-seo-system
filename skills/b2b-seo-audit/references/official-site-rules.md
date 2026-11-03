# Official site rules: page experience, rendering, submission

> Bundled reference of `b2b-seo-audit`. Fetched 2026-11-03. Quotes are short, as the fetch returned them;
> where a source gave a paraphrase it is marked *(paraphrase)*. Page experience and rendering are what the
> **web-design** service (`services/web-design.md`) hands to front end; submission is the audit's own check.

Sources: **[PX]** Google Search Central, *Understanding page experience* · **[JS]** Google Search Central,
*Understand JavaScript SEO basics* · **[RW]** web.dev, *Rendering on the Web* (updated 2026-01-05) ·
**[IN]** indexnow.org, *Documentation* · **[BW]** Bing Webmaster Blog, *Introducing AI Performance in Bing
Webmaster Tools Public Preview* (2026-02-10).

## Page experience (this is what "SXO" means in Google's terms) [PX]

- "Google's core ranking systems look to reward content that provides a good page experience."
- "There is no single signal." · "Core Web Vitals are used by our ranking systems." · "other page experience
  aspects don't directly help your website rank higher in search results."
- "We recommend site owners achieve good Core Web Vitals for success with Search"
- The self-assessment: "Do your pages have good Core Web Vitals?" · "Are your pages served in a secure
  fashion?" · "Does your content display well on mobile devices?" · "Does your content avoid using an excessive
  amount of ads that distract from or interfere with the main content?" · "Do your pages avoid using intrusive
  interstitials?" · "Is your page designed so visitors can easily distinguish the main content from other
  content on your page?"

**EBS adaptation.** SXO is not a separate discipline here: it is these six questions, audited per page
template, with Core Web Vitals as the only measured one (`library/ai-seo-limits.md` § SEO). The other five are
yes/no checks on a template, owned by web design.

## Rendering: what a crawler receives [JS] [RW]

- "Google processes JavaScript web apps in three main phases": crawling, rendering, indexing. [JS]
- Server-side or pre-rendering "is still a great idea because it makes your website faster for users and
  crawlers"; some bots cannot run JavaScript at all *(paraphrase)*. [JS]
- "Google can only discover your links if they are `<a>` HTML elements with an `href` attribute." [JS]
- "don't use fragments to load different page content"; use the History API *(paraphrase)*. [JS]
- "When Google encounters the `noindex` tag, it may skip rendering and JavaScript execution" — so JavaScript
  cannot reliably remove a `noindex`. [JS]
- Client-side routing makes real status codes hard; redirect to a server 404 or add `noindex` *(paraphrase)*. [JS]
- SSR: "Rendering an app on the server to send HTML, rather than JavaScript, to the client." Static rendering
  "happens at build time." CSR: "Rendering an app in a browser, using JavaScript to modify the DOM." [RW]
- "Server-side rendering is a popular choice for delivering a 'complete looking' experience that crawlers can
  interpret." · "Client-side rendering can work, but often needs additional testing and overhead." [RW]
- Rehydration "can have a significant negative impact on TBT and INP, even if it improves FCP." [RW]
- Recommendation: "consider server-side rendering or static rendering over a full rehydration approach." [RW]

**EBS adaptation.** The rule for every page and component: **the text, the links and the structured data are
in the first HTML response.** Tabs and accordions may hide nothing an answer engine needs (`google-text-rules.md`
§ Visibility). The case-study listing that renders client-side only (site-problems P4) is the live example.
AI crawlers (GPTBot, OAI-SearchBot, PerplexityBot) are among the bots that do not run JavaScript, which makes
this a GEO rule as much as an SEO one.

## Submission: telling engines a page changed [IN] [BW]

- IndexNow is a protocol where "submitted URLs will be automatically shared with all other participating
  search engines." [IN]
- Ownership: a UTF-8 key file, simplest "at the root directory of your host"; single URL by GET
  `https://<searchengine>/indexnow?url=…&key=…`, bulk by POST JSON with `host`, `key`, `urlList`, "up to 10,000
  URLs per post." [IN]
- "The HTTP 200 response code only indicates that the search engine has received your URL." Submission is not
  indexing. [IN]
- Bing's advice for being cited in its AI answers includes "use IndexNow to notify search engines of changes"
  *(paraphrase)*. [BW]

**EBS adaptation.** Two site-level setups, neither done yet (checked 2026-11-03): **Bing Webmaster Tools**
verified for ebs-integrator.com (it is also the only first-party source for Copilot citations, see
`seo-strategy` references) and **IndexNow** on publish from the CMS. ChatGPT search draws on Bing, so this is
the cheapest route to the one engine that cited us in the 2026-11-03 baseline.
