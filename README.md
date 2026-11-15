I'm the buyer at [Ortaggi](https://ortaggi.co.uk), a family-run fruit, vegetable and provisions wholesaler at [New Covent Garden Market](https://www.newcoventgardenmarket.com/). Nights, I walk the stands choosing produce for London kitchens. Days, I build the systems the business runs on.

### ortaggi.co.uk

The website is written and maintained mostly by software, with a person signing off on the parts that need one.

- **A growth agent that ships its own pages.** On a timer it picks a search gap, writes the landing page, blog post or market report for it, and opens a branch. Nothing merges unless a gate of roughly 4,800 unit tests plus accessibility, SEO and device checks passes. A failed gate leaves a draft for review.
- **Measurement that picks the next job.** Search Console, first-party page views and daily rank checks feed a scorer that rates every shipped change 28 days later, and the planner reorders its queue on what moved. Google's indexed count went from 16 pages to 63 in five weeks.
- **Guards for its own failure modes.** Separate gates for doorway pages, near-duplicate posts, invented claims about the business and leaked prices. Each was added after something shipped wrong once.
- **One house style.** The design is our market stationery turned into a site: cream paper, a serif, brass rules, every picture an etching that develops into a photograph, in a light and a dark version. Copy, theme and section order live in one typed config.

### The Market Note

A weekly letter from the market floor for chefs: what is in season, what is scarce, what is about to turn. Subscriber prices sit in a separate layer that no public page can render. Double opt-in, one-click unsubscribe, out every Monday morning.

### Behind the counter

- **Sales pipeline.** Finds trade kitchens across a set of postcodes, scores them against food hygiene and company records, clusters them on a map for visit planning, and sorts every reply into an outcome.
- **People and dispatch.** HR, leave and delivery dispatch for the team, on Frappe and ERPNext with a React front end.
- **An always-on box.** The scheduled jobs run on one machine that never sleeps, with a persistent session per project that I can pick up from a phone on the market floor.

### Stack

TypeScript, Node and Next.js, Tailwind, Vitest and Playwright. Netlify, Cloudflare Workers and D1, Postgres, Frappe. Bash for whatever runs on a timer.

Most of this is private because it runs a live business. The one public repo is **[training_insights](https://github.com/franko-c/training_insights)**, a Zwift racing dashboard: bikes are what I do when the market is shut.
