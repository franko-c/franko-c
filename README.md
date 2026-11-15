I'm the buyer at [Ortaggi](https://ortaggi.co.uk), a family-run fruit, vegetable and provisions wholesaler at [New Covent Garden Market](https://www.newcoventgardenmarket.com/), and I lead the work of automating how the business runs. Nights, I walk the stands choosing produce for London kitchens. Days, I build the systems.

I build almost all of it with large language models, Claude in particular, and some of it is run by them. The growth agent below is Claude on a timer, working inside guardrails and test gates I wrote: nothing it makes reaches the live site until every check passes.

### The numbers so far

| | April 2026 | October 2026 |
| --- | --- | --- |
| Google search impressions a month | 512 | **6,274** (12x) |
| Clicks from search a month | 11 | **75** (7x) |
| Pages in Google's index | 16 of 56 | **63 of 65** |
| Changes the agent has shipped by itself | 0 | **72** |

November is running at 484 impressions a day, more than double October's 202. Search Console monthly totals, the first full month on record against the last complete one; index counts 7 October to 14 November. The agent's 72 include 25 blog posts, 4 market reports and 16 weekly Market Notes.

### ortaggi.co.uk

- **A growth agent that ships its own pages.** On a schedule it picks a search gap, writes the landing page, blog post or market report for it, and opens a branch. A gate of roughly 4,800 unit tests plus accessibility, SEO and device checks decides whether it merges. A failed gate leaves a draft for review.
- **Measurement that picks the next job.** Search Console, first-party page views and daily rank checks feed a scorer that rates every shipped change after 28 days, and the planner reorders its queue on what moved.
- **Guards for its own failure modes.** Separate gates for doorway pages, near-duplicate posts, invented claims about the business and leaked prices. Each was added after something shipped wrong once.
- **One house style.** Our market stationery turned into a site: cream paper, a serif, brass rules, every picture an etching that develops into a photograph, designed in light and dark. Copy, theme and section order live in one typed config.

### The Market Note

A weekly letter from the market floor for chefs: what is in season, what is scarce, what is about to turn. Subscriber prices sit in a separate layer that no public page can render. Double opt-in, one-click unsubscribe, out every Monday morning.

### Behind the counter

- **Sales pipeline.** Finds trade kitchens across a set of postcodes, scores them against food hygiene and company records, clusters them on a map for visit planning, and sorts every reply into an outcome.
- **People and dispatch.** HR, leave and delivery dispatch for the team, on Frappe and ERPNext with a React front end.
- **An always-on box.** The scheduled agents run on one machine that never sleeps, with a persistent Claude Code session per project that I pick up from a phone on the market floor.

### Stack

TypeScript, Node and Next.js, Tailwind, Vitest and Playwright. Netlify, Cloudflare Workers and D1, Postgres, Frappe. Claude Code for the agents, Bash for whatever runs on a timer.

Most of this is private because it runs a live business.
