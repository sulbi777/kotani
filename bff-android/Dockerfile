FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install --only=production
COPY . .
# Keamanan: non-root user
USER node
EXPOSE 3000
CMD ["node", "src/index.js"]
