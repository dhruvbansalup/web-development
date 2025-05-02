import jwt from "jsonwebtoken";

const JWTsecret="MySecretKey";

function setUser(user){
    const payload={
        ...user
    };
    return jwt.sign(payload,JWTsecret);
}

function checkUser(token){
    if (!token) return false;
    return jwt.verify(token,JWTsecret);
}

export { setUser,checkUser };