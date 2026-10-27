FROM nginx:alpine
HEALTHCHECK --interval=5s --timeout=2s --retries=2 CMD wget -q --spider http://localhost/ || exit 1