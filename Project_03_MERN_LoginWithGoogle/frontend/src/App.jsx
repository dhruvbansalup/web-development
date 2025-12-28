import { useState } from 'react'
import './App.css'
import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom"
import GoogleLogin from './GoogleLogin'
import Dashboard from './Dashboard'
import { GoogleOAuthProvider } from '@react-oauth/google'

// Define GoogleAuthWrapper as a separate component
const GoogleAuthWrapper = () => {
  const clientId = import.meta.env.VITE_GOOGLE_CLIENT_ID;

  return (
    <GoogleOAuthProvider clientId={clientId}>
      <GoogleLogin />
    </GoogleOAuthProvider>
  );
};

function App() {
  return (
    <BrowserRouter>
      <Routes>  
        <Route path="/login" element={<GoogleAuthWrapper />} />
        <Route path="/" element={<Navigate to="/login" />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="*" element={<div>NOT FOUND</div>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;