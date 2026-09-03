# LPX Website Agent Instructions

You are working on the documentation website for the **Live Production Exchange (LPX)**. LPX is an open-source standard for automating live video metadata and scheduling across IP networks, based on the IPTC ninjs standard.

## Tech Stack & Architecture
- **Framework:** Hugo (with Pagefind for search)
- **Content:** All documentation is written in Markdown (`.md`) and is located in the `content/` directory.
- **Styling:** Custom styling is managed in `static/css/custom.css`. The site uses Bootstrap 5.
- **Assets:** Images and visual assets are stored in `static/assets/`.

## Development Guidelines

1. **Running the Server:**
   To start the dev server, run:
   ```bash
   npm run dev
   ```
   If running as an agent tool, use the `run_command` tool with `IsDaemon: true` to run the server in the background.

2. **Styling & Theming:**
   - The site uses a modern, sleek design language based on Bootstrap 5 with the `Inter` font.
   - **Do not hardcode colors** in a way that breaks visibility. Rely on Bootstrap 5's CSS variables (e.g., `--bs-primary`) where possible.
   
3. **Writing Documentation:**
   - Use Hugo's built-in shortcodes or custom shortcodes (e.g., `{{< card >}}`, `{{< cardgrid >}}`, `{{< caution >}}`) in Markdown files to enhance documentation formatting.
   - Ensure you use root-relative paths (e.g., `/assets/logos/`) when linking to assets or other documentation pages.

4. **Git Commit Format:**
   - All commits must follow the **Conventional Commits** specification (e.g., `feat(ui): add new button`, `fix(docs): resolve typo`, `chore(deps): update packages`).
   - Please always include a scope where applicable, formatted as `type(scope): message`.

## Helpful References
- [Hugo Documentation](https://gohugo.io/documentation/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Pagefind Documentation](https://pagefind.app/docs/)
