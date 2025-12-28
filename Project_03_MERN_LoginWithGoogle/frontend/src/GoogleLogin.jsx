import React from "react";
import { useGoogleLogin } from "@react-oauth/google"

function GoogleLogin() {

    const responseGoogle=async(authResult)=>{
        try {
            
        } catch (error) {
            
        }
    }

    const googleLogin = useGoogleLogin({
        onSuccess: responseGoogle,
        onError: responseGoogle,
        flow:"auth-code"
    })


    return (
        <div className="App">

            <button onClick={googleLogin}>
                Login With Google
            </button>
        </div>
    );
}

export default GoogleLogin