import { checkUser } from "./services.js";

function restrictToLoggedInUsers(req, res, next) {
    const userCookie=req.cookies.user;
    if (checkUser(userCookie)) {
        return next();
    } else {
        res.status(401).json({ message: 'Unauthorized: Please log in to access this resource.' });
    }
}

export { restrictToLoggedInUsers };