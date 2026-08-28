# Official machine-signal rules, verbatim

Sources (fetched 2026-07-28): **[AR]** Article structured data (2025-12-10) · **[PP]** ProfilePage structured data (2025-12-10) · **[BD]** Byline dates (2025-12-10) · **[SP]** Structured data policies (2026-07-10) — developers.google.com. Crawler docs: **[GC]** Google crawlers (2026-07), **[OA]** developers.openai.com/api/docs/bots, **[PX]** docs.perplexity.ai crawlers, **[AN]** support.claude.com crawler article (2026-04).

## 1. Article schema [AR]

"There are no required properties; instead, add the properties that apply to your content." Key recommended: `headline` ("Consider using a concise title, as long titles may be truncated"), `image` ("multiple high-resolution images (minimum of 50K pixels…) with the following aspect ratios: 16x9, 4x3, and 1x1"), `datePublished`/`dateModified` ("ISO 8601 format. We recommend that you provide timezone information; otherwise, we will default to the timezone used by Googlebot"), `author`, `author.name`, `author.url`.

**Author best practices [AR], verbatim:**
- `author.url`: "A link to a web page that uniquely identifies the author … the author's social media page, an 'about me' page, or a bio page. If the URL is an internal profile page, we recommend marking up that author using profile page structured data. You can use the `sameAs` property as an alternative. Google can understand both `sameAs` and `url` when disambiguating authors."
- "Include all authors in the markup — Make sure that all the authors that are presented as authors on the web page are also included in markup."
- "When specifying multiple authors, list each author in their own `author` field … Don't merge multiple authors in the same `author` field."
- "We strongly recommend using the `type` and `url` (or `sameAs`) properties."
- "In the `author.name` property, only specify the name of the author. Don't add any other piece of information" — not the publisher (use `publisher`), not job title (use `jobTitle`), not honorifics (use `honorificPrefix`/`honorificSuffix`), no "posted by".
- "Use the `Person` type for people, and the `Organization` type for organizations. Don't use the `Thing` type."

## 2. ProfilePage schema (the author bio page) [PP]

"`ProfilePage` markup is designed for any site where creators (either people or organizations) share first-hand perspectives." Valid uses include "An author page on a news site", "An 'About Me' page on a blog site". Required: `mainEntity` (Person/Organization). Recommended: `name` ("real names", `alternateName` for handles), `description` ("The user's byline or applicable credential"), `sameAs` ("URL to other external profiles"), `dateCreated`/`dateModified`, `image`. Article `author.url` should point at this page — this is the machine-readable version of the E-E-A-T byline chain (byline → bio → external verification).

## 3. Byline dates [BD]

"A byline date is the date that Google estimates that the web page was updated or published … our systems look at several factors to determine our best estimate."

Best practices, verbatim: "Add a user-visible date to the page and feature it prominently. Label your dates appropriately with text like 'Publish' or 'Last updated'." · "Specify dates with structured data … `datePublished` and/or `dateModified`." · "The date is required; the time is not: However, we recommend you provide a time and timezone in markup for added precision." · "**Make your dates and times consistent.** Ensure that the date … match between the equivalent user-visible and structured values." · "**Don't specify future dates, or the date of the action described on the page.** The dates must describe the publication or update date of the page, not the stories or events described therein." · "Minimize the presence of other dates on the page." · "Google doesn't guarantee that a byline date … will be shown."

(Artificial date-freshening without content change is called out as a warning sign in Google's helpful-content doc, not this page.)

## 4. Structured data policies [SP]

"Google does not guarantee that your structured data will show up in search results, even if your page is marked up correctly." · "Your structured data must be a true representation of the page content." · "**Don't** mark up content that is not visible to readers of the page." · "**Don't** mark up irrelevant or misleading content, such as fake reviews." · "**Don't** use structured data to deceive or mislead users. Don't impersonate any person or organization." · "The more recommended properties that you provide, the higher quality the result is to users." · Manual actions: "a page loses eligibility for appearance as a rich result; it doesn't affect how the page ranks in Google web search."

## 5. The crawler matrix (official, per vendor)

**Google [GC]:**
- `Googlebot` — Search crawling; "Crawling preferences addressed to the Googlebot user agent affect Google Search (including Discover and all Google Search features)" — AI Overviews/AI Mode ride on Googlebot.
- `Google-Extended` — control token, not a bot: manages "whether content Google crawls … may be used for **training future generations of Gemini models** … and for **grounding** … in Gemini Apps and Grounding with Google Search on Vertex AI." · "Google-Extended does not impact a site's inclusion in Google Search nor is it used as a ranking signal." → **Blocking Google-Extended removes Gemini-app visibility but not Search AI Overviews.**
- User-triggered fetchers (Google-Agent, Gemini Notebook) "generally ignore robots.txt rules."
- Rendering (documented for Google Search only): "Google Search runs JavaScript with an evergreen version of Chromium"; "If the content isn't visible in the rendered HTML, Google won't be able to index it"; "**Google Search does not interact with your page**" (no clicks, no scrolling). · "Google's crawlers and fetchers only crawl the first 15MB of a file."

**OpenAI [OA]:** `GPTBot` (model training; blockable independently) · `OAI-SearchBot` — "Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search answers" · `ChatGPT-User` (user-initiated fetch; "robots.txt rules may not apply"). "~24 hours from a site's robots.txt update for our systems to adjust."

**Perplexity [PX]:** `PerplexityBot` — "designed to surface and link websites in search results on Perplexity. It is not used to crawl content for AI foundation models." · `Perplexity-User` — user fetch, "generally ignores robots.txt rules." No training crawler documented.

**Anthropic [AN]:** `ClaudeBot` (training) · `Claude-SearchBot` ("navigates the web to improve search result quality") · `Claude-User` (user-query fetch; blocking it "may reduce your site's visibility for user-directed web search"). All honor robots.txt per the article.

**Not officially documented (never state as fact):** JS rendering by OpenAI/Perplexity/Anthropic bots; main-content extraction methods; tab/accordion handling outside Google. **llms.txt:** no vendor documents consuming it from third-party sites (Google's guide explicitly says Search ignores such files).

## 6. The practical visibility matrix (derived strictly from the above)

To be visible in: AI Overviews/AI Mode → allow `Googlebot`, be indexed + snippet-eligible. Gemini apps → additionally allow `Google-Extended`. ChatGPT search → allow `OAI-SearchBot`. Perplexity → allow `PerplexityBot`. Claude search → allow `Claude-SearchBot`. Blocking training bots (`GPTBot`, `ClaudeBot`, `Google-Extended`-training aspect) is a separate policy decision that does not remove search/answer visibility for OpenAI (OAI-SearchBot separate) — but for Google, `Google-Extended` bundles Gemini training AND grounding in one token.
