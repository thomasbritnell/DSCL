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
        setUser(data.username ? { username: data.username } : null);
        setLoading(false);
      })
      .catch(() => {
        setUser(null);
        setLoading(false);
      });
  }, []);

  const login = (username) => setUser({ username });
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
