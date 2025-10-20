# Client-side Dockerfile for Frontend
# Build the React app
FROM node:20-alpine AS build

# Set Docker working directory
WORKDIR /app

# Install dependencies (package.json + package-lock.json or yarn.lock)
COPY package*.json ./
RUN npm install

# Copy all source code
COPY . .

# Build the React app for production (creates /app/build)
RUN npm run build

# Serve with Nginx
FROM nginx:alpine

# Remove default nginx static files
RUN rm -rf /usr/share/nginx/html/*

# Copy Vite build output (dist folder) to nginx html folder
COPY --from=build /app/dist /usr/share/nginx/html

# Copy custom nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start Nginx in foreground (necessary for Docker)
CMD ["nginx", "-g", "daemon off;"]