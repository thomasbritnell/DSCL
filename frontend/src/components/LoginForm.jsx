// frontend/src/components/LoginForm.jsx

import React, { useState } from "react";
import { useLogin } from "./LoginContext";

/**
 * LoginForm component displays login and logout UI for the app.
 * Shows login form if not logged in, and user info/logout if logged in.
 * @returns {JSX.Element}
 */
export default function LoginForm() {
  const { user, login, logout } = useLogin();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  // If user is logged in, show username and logout button
  if (user) {
    return (
      <div className="flex items-center gap-4 mb-4">
        <span className="text-sm text-black">Logged in as <b>{user.username}</b></span>
        <button className="text-black hover:underline text-sm" onClick={logout}>
          Log out
        </button>
      </div>
    );
  }

  // Otherwise, show login form
  return (
    <form
      className="flex items-center gap-2 mb-4"
      onSubmit={e => {
        e.preventDefault();
        login(username, password);
        setUsername("");
        setPassword("");
      }}
    >
      <input
        className="border rounded px-2 py-1 text-sm text-black"
        placeholder="Username"
        value={username}
        onChange={e => setUsername(e.target.value)}
        required
      />
      <input
        className="border rounded px-2 py-1 text-sm text-black"
        placeholder="Password"
        type="password"
        value={password}
        onChange={e => setPassword(e.target.value)}
        required
      />
      <button className="bg-blue-600 text-black px-3 py-1 rounded text-sm" type="submit">
        Log in
      </button>
    </form>
  );
}
