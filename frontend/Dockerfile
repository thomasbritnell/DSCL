# Use official Node.js image for building and running Next.js
FROM node:20-alpine as builder

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy frontend source code
COPY . .

# Build the Next.js app
RUN npm run build

# --- Production image ---
FROM node:20-alpine as runner
WORKDIR /app

# Copy built app and node_modules from builder
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/next.config.mjs ./next.config.mjs

ENV PORT=80
EXPOSE 80
CMD ["npm", "run", "start", "--", "-p", "80"]

