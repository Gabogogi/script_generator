// src/App.tsx
import React, { useState } from 'react';
import './App.css';
import AuthForm from './Log.tsx';

const App: React.FC = () => {
  const [isLogin, setIsLogin] = useState(true);

  const toggleForm = () => {
    setIsLogin(!isLogin);
  };

  return (
    <div className="container">
      {isLogin ? (
        <AuthForm
          formType="login"
          toggleForm={toggleForm}
          title="Login"
          subtitle="Welcome back! Please login to your account."
          buttonText="Login"
          switchText="Don't have an account?"
          switchLinkText="Register"
        />
      ) : (
        <AuthForm
          formType="register"
          toggleForm={toggleForm}
          title="Register"
          subtitle="Create a new account."
          buttonText="Register"
          switchText="Already have an account?"
          switchLinkText="Login"
        />
      )}
    </div>
  );
};

export default App;
