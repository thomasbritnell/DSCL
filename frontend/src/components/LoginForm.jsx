import React, { useState } from 'react';

export default function LoginForm({ onLoginSuccess }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      const res = await fetch('/api/login', {
        method: 'POST',
        credentials: 'include',  // 🔑 Required for cookie-based login
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (res.ok) {
        if (onLoginSuccess) {
          onLoginSuccess(username);  // Pass the username back to parent
        }
      } else {
        const data = await res.json();
        setError(data.error || 'Login failed.');
      }
    } catch (err) {
      setError('Network error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded shadow-lg w-full max-w-xs text-black">
      <h2 className="text-lg font-semibold mb-2">Login</h2>
      <label className="block mb-2">
        Username:
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
          className="w-full border rounded px-2 py-1 mt-1 text-black bg-white"
        />
      </label>
      <label className="block mb-4">
        Password:
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          className="w-full border rounded px-2 py-1 mt-1 text-black bg-white"
        />
      </label>
      {error && <p className="text-red-600 text-sm mb-2">{error}</p>}
      <button type="submit" disabled={loading} className="w-full bg-blue-700 text-white py-2 rounded">
        {loading ? 'Logging in...' : 'Login'}
      </button>
    </form>
  );
}
