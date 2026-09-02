# Live Production Exchange (LPX)

The open-source standard for automating the exchange of live video metadata and scheduling across IP networks.

**[Read the Documentation](https://live-production-exchange.github.io)** (or wherever your docs are hosted)
**[Join the Community on GitHub](https://github.com/live-production-exchange)**

## Overview

LPX is evolving into an independent, open-source standard. It bridges the gap between live event producers, service providers, and broadcast technologies by replacing manual, high-touch legacy workflows with seamless machine-to-machine communication for live video content. 

The standard leverages a metadata schema based on the proven IPTC **ninjs** standard for describing live feeds, schedules, and transport protocols.

## Documentation Site Development

This repository contains the Astro + Starlight documentation site for LPX.

### Prerequisites

- Node.js
- npm

### 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |

### Contributing to the Docs

1. Documentation pages are written in Markdown (`.md`) or MDX (`.mdx`).
2. You can find all the content pages inside the `src/content/docs/` directory.
3. Simply create or edit files in there to update the site. The navigation sidebar will automatically generate based on the folder structure and `astro.config.mjs` settings.

## License

Built by the community, for the community. Moving towards a standalone, fully open ecosystem.
