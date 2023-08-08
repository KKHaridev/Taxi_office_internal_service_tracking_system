# Use an official Node.js runtime as the base image
FROM node:17

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files and install dependencies
COPY package.json .
RUN npm install -g pnpm
RUN pnpm install

# Copy the rest of the application code
COPY . .

# Build the React app
RUN npm run build

# Expose the port on which the React app will run
EXPOSE 5173

# Define the command to run your React app when the container starts
CMD ["npm", "run","dev","--","--host"]