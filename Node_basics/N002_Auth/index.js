import express from 'express';
import path from 'path';
import {fileURLToPath} from 'url';
import cookieParser from 'cookie-parser';

const app = express();

//Setup for imporing templates
const __filename=fileURLToPath(import.meta.url);
const __dirname=path.dirname(__filename);
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

//middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

import connectDB from './db.js';
connectDB();

import routes from './routes.js';
app.use(routes);


const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
