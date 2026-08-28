# Google's official text-formatting rules, verbatim

Sources (fetched 2026-07-28): **[SG]** SEO Starter Guide (2025-12-10) · **[SN]** Snippets doc (2026-04-20) · **[FS]** Featured snippets (2025-12-10) · **[TL]** Title links (2025-12-10) — all developers.google.com/search/docs.

## Text and organization

[SG]: "The text is easy-to-read and well organized: Write content naturally and make sure the content is well written, easy to follow, and free of spelling and grammatical mistakes. **Break up long content into paragraphs and sections, and provide headings** to help users navigate your pages."

## Headings — the official surprise

[SG]: "Having your headings in semantic order is fantastic for screen readers, but **from Google Search perspective, it doesn't matter if you're using them out of order** … There's also no magical, ideal amount of headings a given page should have. However, if you think it's too much, then it probably is." → Heading hierarchy is an accessibility and reader practice, not a ranking trick. Don't sell it as one.

## Vocabulary — official basis for dual-register writing

[SG]: "Think about the words that a user might search for to find a piece of your content. **Users who know a lot about the topic might use different keywords in their search queries than someone who is new to the topic.**" · "Google's language matching systems are sophisticated and can understand how your page relates to many queries, even if you don't explicitly use the exact terms." · "If you are varying the words (writing naturally to not be repetitive), you have more chances to show up in Search simply because you are using more keywords."

Limits: "Keyword stuffing: Excessively repeating the same words over and over (even in variations) is tiring for users, and keyword stuffing is against Google's spam policies." · "The length of the content alone doesn't matter for ranking purposes (there's no magical word count target, minimum or maximum…)."

## Snippets — you write them by writing the page

[SN]: "Snippets are automatically created from page content … Google Search might show different snippets for different searches." · "Snippets are primarily created from the page content itself. However, Google sometimes uses the meta description HTML element if it might give users a more accurate description of the page." · [SG]: "The snippet is sourced from the actual content of the page … thus **you have complete control over the words that can be used to generate the snippet.**"

Meta descriptions [SN]: "like a pitch that convince the user that the page is exactly what they're looking for" · "There's no limit on how long a meta description can be, but the snippet is truncated … typically to fit the device width." · "Identical or similar descriptions on every page of a site aren't helpful." · "meta descriptions comprised of long strings of keywords … are less likely to be displayed." · "Good descriptions are human-readable and diverse."

## Visibility — machines don't click

[SN best practices]: "**Make sure content is immediately visible on the page to a human (and not hidden behind an expandable section or tabbed interface, for example).**" This pairs with Google's rendering doc: "Google Search does not interact with your page" — content requiring a click, tab, or scroll-trigger effectively doesn't exist for extraction.

## Featured snippets

[FS]: "Featured snippets are special boxes where the format of a regular search result is reversed … They can also appear within a related questions group (also known as 'People Also Ask')." · Can you mark a page as one? "**You can't.** Google systems determine whether a page would make a good featured snippet for a user's search request, and if so, elevates it." · Opt-outs: `nosnippet`, or "experiment with setting the `max-snippet` rule to lower lengths." · "Clicking a featured snippet takes the user directly to the section of the page that appeared in the featured snippet" — self-contained sections are what get lifted.

## Title links

[TL] Google's title generation "is completely automated and takes into account both the content of a page and references to it." Sources it uses: "Content in `<title>` elements; Main visual title shown on the page; Heading elements, such as `<h1>` elements; Content in `og:title` meta tags; Other content that's large and prominent through the use of style treatments; Other text contained in the page; Anchor text on the page; Text within links that point to the page; `WebSite` structured data."

Best practices: "Write descriptive and concise text … Avoid vague descriptors like 'Home' … Avoid keyword stuffing … It's important to have distinct text … for each page." · "Consider ensuring that your main title is distinctive from other text on a page and stands out as being the most prominent (for example, using a larger font, putting the title text in the first visible `<h1>` element)." · "Use the same language and writing system … as the primary content."

What makes Google rewrite your title: half-empty, obsolete, inaccurate, or micro-boilerplate `<title>` elements; "No clear main title" ("If Google Search detects that there are multiple large, prominent headings, it may use the first heading"); language mismatch.

## Links and images

[SG] anchor text: "This text tells users and Google something about the page you're linking to. With appropriate anchor text, users and search engines can easily understand what your linked pages contain before they visit." · External links: "make sure you trust the resource you're linking to. If you can't trust the content and you still want to link to them, add a nofollow or similar annotation."

[SG] images: "place them near text that's relevant to the image. The text that's near images can help Google better understand what the image is about." · "Alt text is a short, but descriptive piece of text that explains the relationship between the image and your content."
