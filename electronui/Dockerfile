FROM node:25.8-alpine

WORKDIR /app

RUN pnpm install
RUN pnpm install react-router-dom

EXPOSE 5173

RUN useradd app
USER app

COPY . .

# Change to build for prod
CMD ["pnpm", "run", "dev"]
