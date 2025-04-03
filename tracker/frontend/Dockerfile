# Step 1: Use an official Node.js image as the base image
FROM node:23 AS builder

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Step 4: Install dependencies
RUN npm install

# Step 5: Copy the rest of the app's source code
COPY . .

# Step 6: Build the Next.js app
RUN npm run build

# Step 7: Use a smaller image for the final production image
FROM node:23-slim

# Set the working directory in the container
WORKDIR /app

# Copy the built files and node_modules from the builder stage
COPY --from=builder /app /app

# Install any production dependencies (if needed)
RUN npm install --production

# Expose the port that the app will run on
EXPOSE 3000

# Step 8: Start the Next.js app in production mode
CMD ["npm", "start"]
