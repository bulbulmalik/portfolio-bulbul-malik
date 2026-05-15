# Portfolio Deployment

This repository contains a static portfolio site and a portfolio project demo.

## What is deployed on Vercel
- `portolio.html` as the main homepage
- `rag-knowledge-base/index.html` as the featured project page
- static assets like `About Me-Picsart-AiImageEnhancer.png`, `I H.png`, and `rag-knowledge-base/screenshot.svg`

## Vercel setup
1. Sign in to Vercel and connect your GitHub/GitLab/Bitbucket repository.
2. Create a new project and select this repository.
3. Set the root directory to the repository root.
4. Vercel will use `vercel.json` to route `/` to `portolio.html` and `/rag` to `rag-knowledge-base/index.html`.

## Access
- Portfolio homepage: `/`
- Featured project page: `/rag`

## Notes
- The static portfolio is ready for Vercel.
- The FastAPI backend in `rag-knowledge-base/app.py` is not part of the static site and must be deployed separately if you want a live API.
