import { User } from './model.js';

import { setUser } from './services.js';

async function handleUserSignUp(req, res) {
    const { name, password } = req.body;
    await User.create({ name, password });

    return res.send("User Created Successfully");
}


async function handleUserlogin(req, res) {
    const { name, password } = req.body;

    const user = await User.findOne({ name, password });
    if (!user) return res.send("INVAILD NAME OR PASSWORD");

    const token=setUser(user);
    res.cookie("user",token);

    return res.redirect("/");
}


export { handleUserSignUp, handleUserlogin };