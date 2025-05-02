import express from "express";
import { handleUserSignUp, handleUserlogin } from "./controller.js";
import { restrictToLoggedInUsers } from "./middleware.js";

const router = express.Router();

router.get("/", restrictToLoggedInUsers, (req, res) => {
    res.render("home", {
        message: "Welcome"
    });
});

router.get("/signup", (req, res) => {
    res.render("signup");
});

router.post("/signup", (req, res) => {
    handleUserSignUp(req, res);
});


router.get("/login", (req, res) => {
    res.render("login");
});

router.post("/login", (req, res) => {
    handleUserlogin(req, res);
});

export default router