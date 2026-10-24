# MANTA thesis website

Small public website for the MANTA thesis.

It has:

- a landing page explaining the overall thesis
- a demo page for the app/backend flow
- a thesis PDF download button
- the elephant logo and footer pattern from the other projects
- same-domain assumptions for the FastAPI backend

## Run locally

```bash
npm install
cp ../main.pdf public/manta-thesis.pdf
npm run dev
```

Open `http://localhost:3000`.

The demo page uses simulated events by default. It can also read backend data when the app and backend share the same origin and you type the private adapter token locally in the browser.

Keep the backend token private. The public demo page does not bake a token into the bundle.

## Compiler compatibility

The website uses TypeScript 7 for the tsc CLI and Microsoft's TypeScript 6 API
compatibility package for Next.js build tooling. The npm aliases follow the
[official side-by-side setup](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/#running-side-by-side-with-typescript-60).

Run npm run typecheck to check routes with the native compiler; npm run build
also validates the API-based Next.js build.
