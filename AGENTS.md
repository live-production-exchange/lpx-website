# LPX Website Agent Instructions

You are working on the documentation website for the **Live Production Exchange (LPX)**. LPX is an open-source standard for automating live video metadata and scheduling across IP networks, based on the IPTC ninjs standard.

## Tech Stack & Architecture
- **Framework:** Astro + Starlight
- **Content:** All documentation is written in Markdown (`.md`) or MDX (`.mdx`) and is located in `src/content/docs/`.
- **Styling:** Custom styling is managed in `src/styles/custom.css`.
- **Assets:** Images and visual assets are stored in `src/assets/`.

## Development Guidelines

1. **Running the Server:**
   When starting the dev server, you must use background mode:
   ```bash
   astro dev --background
   ```
   Manage the background server using `astro dev stop`, `astro dev status`, and `astro dev logs`.

2. **Styling & Theming:**
   - The site supports both Dark and Light modes (handled natively by Starlight). 
   - **Do not hardcode colors** in a way that breaks visibility in light mode (e.g., forcing white text on light backgrounds). Rely on Starlight's CSS variables (`--sl-color-*`) where possible.
   - The site uses a modern, sleek design language with the `Inter` font.

3. **Writing Documentation:**
   - Use Starlight's built-in components (e.g., `<Card>`, `<CardGrid>`, `<Aside>`, or `:::caution`) in MDX files to enhance documentation formatting.
   - Ensure you use relative paths when linking to assets or other documentation pages.

4. **Git Commit Format:**
   - All commits must follow the **Conventional Commits** specification (e.g., `feat(ui): add new button`, `fix(docs): resolve typo`, `chore(deps): update packages`).
   - Please always include a scope where applicable, formatted as `type(scope): message`.

## Helpful References
- [Starlight Documentation](https://starlight.astro.build/)
- [Astro Documentation](https://docs.astro.build)
