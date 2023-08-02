FROM node:16.17.0
WORKDIR /app
COPY package.json .
RUN npm i
RUN npm add @vitejs/plugin-react
COPY . .
EXPOSE 3000
CMD ["npm", "run", "dev","--","--host","0.0.0.0"]