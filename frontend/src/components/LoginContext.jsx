"use client";
import React, { createContext, useContext, useState, useEffect } from "react";

const LoginContext = createContext();

export function LoginProvider({ children }) {
  const [user, setUser] = useState(null); // null = guest, { username } = logged in
  const [loading, setLoading] = useState(true);

  // On mount, check if logged in
  useEffect(() => {
    fetch("/api/me", { credentials: "include" })
      .then((res) => (res.ok ? res.json() : { username: null }))
      .then((data) => {
        setUser(data.username ? { username: data.username, userType: data.user_type } : null);
        setLoading(false);
      })
      .catch(() => {
        setUser(null);
        setLoading(false);
      });
  }, []);

  const login = async (username, userType = 'guest') => {
    // First set user with provided info
    setUser({ username, userType });
    
    // Then fetch the latest user data from the server to ensure we have the correct user_type
    try {
      const res = await fetch("/api/me", { credentials: "include" });
      if (res.ok) {
        const userData = await res.json();
        if (userData.username) {
          setUser({ username: userData.username, userType: userData.user_type });
        }
      }
    } catch (error) {
      console.error("Error fetching user data after login:", error);
    }
  };
  
  const logout = async () => {
    await fetch("/api/logout", { method: "POST", credentials: "include" });
    setUser(null);
  };

  return (
    <LoginContext.Provider value={{ user, loading, login, logout }}>
      {children}
    </LoginContext.Provider>
  );
}

export function useLogin() {
  return useContext(LoginContext);
}
