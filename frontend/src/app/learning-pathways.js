// frontend/src/app/learning-pathways.js
"use client";

import React, { useEffect, useState } from "react";
import { useLogin } from "../components/LoginContext";
import LoginForm from "../components/LoginForm";
import { usePathname } from "next/navigation";
import Link from "next/link";
import ChallengeCard from "../components/ChallengeCard";


/**
 * LearningPathwaysPage displays groups of challenge cards for each pathway.
 * @returns {JSX.Element}
 */
export default function LearningPathwaysPage() {
  const { user, loading, login, logout } = useLogin();
  const [showLogin, setShowLogin] = useState(false);
  const [showRegister, setShowRegister] = useState(false);
  const [registerError, setRegisterError] = useState(null);
  const [registerLoading, setRegisterLoading] = useState(false);

  async function handleRegister(e) {
    e.preventDefault();
    setRegisterError(null);
    setRegisterLoading(true);
    const form = e.target;
    const username = form.username.value;
    const password = form.password.value;
    const user_type = form.user_type.value;
    try {
      const res = await fetch("/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password, user_type }),
      });
      if (res.ok) {
        setShowRegister(false);
        setShowLogin(true);
      } else {
        const data = await res.json();
        setRegisterError(data.error || "Registration failed.");
      }
    } finally {
      setRegisterLoading(false);
    }
  }
  const pathname = usePathname();
  const [challenges, setChallenges] = useState([]);
  const [pathways, setPathways] = useState([]);

  // Fetch all challenges and pathways once for mapping
  useEffect(() => {
    fetch("/api/challenges")
      .then((res) => res.json())
      .then((data) => setChallenges(data));
    fetch("/api/pathways")
      .then((res) => res.json())
      .then((data) => setPathways(data));
  }, []);

  // Helper to get challenge objects by ID
  function getChallengesByIds(ids) {
    return challenges.filter((ch) => ids.includes(ch.id));
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8 bg-white text-black relative">
      {/* User status and auth menu */}
      <div className="absolute right-0 top-0 mt-4 mr-4 z-10">
        {loading ? null : user ? (
          <div className="flex items-center space-x-2">
            <span className="text-sm text-gray-700">Logged in as <span className="font-semibold">{user.username}</span></span>
            {user.userType === "admin" && (
              <Link href="/admin/challenges" className="text-green-700 text-sm hover:underline bg-white px-2 py-1 rounded">Admin Panel</Link>
            )}
            <button onClick={logout} className="text-blue-700 text-sm hover:underline bg-white px-2 py-1 rounded">Logout</button>
          </div>
        ) : (
          <div className="flex items-center space-x-2">
            <span className="text-sm text-gray-700">Guest</span>
            <button onClick={() => setShowLogin(true)} className="text-blue-700 text-sm hover:underline bg-white px-2 py-1 rounded">Sign In</button>
            <button onClick={() => setShowRegister(true)} className="text-blue-700 text-sm hover:underline bg-white px-2 py-1 rounded">Register</button>
          </div>
        )}
      </div>

      {/* Login Modal */}
      {showLogin && (
        <div className="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded shadow-lg w-full max-w-xs relative">
            <button onClick={() => setShowLogin(false)} className="absolute top-2 right-2 text-gray-400 hover:text-gray-700">✕</button>
            <LoginForm onLoginSuccess={async (username) => {
              setShowLogin(false);
              // Use the enhanced login function which will fetch the correct user data
              await login(username);
            }} />
          </div>
        </div>
      )}

      {/* Register Modal */}
      {showRegister && (
        <div className="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded shadow-lg w-full max-w-xs relative">
            <button onClick={() => setShowRegister(false)} className="absolute top-2 right-2 text-gray-400 hover:text-gray-700">✕</button>
            <form onSubmit={handleRegister} className="space-y-4 bg-white text-black">
              <h2 className="text-lg font-semibold mb-2">Register</h2>
              <label className="block mb-2">
                Username:
                <input name="username" type="text" required className="w-full border rounded px-2 py-1 mt-1 text-black bg-white" />
              </label>
              <label className="block mb-4">
                Password:
                <input name="password" type="password" required className="w-full border rounded px-2 py-1 mt-1 text-black bg-white" />
              </label>
              <label className="block mb-4">
                User Type:
                <select name="user_type" className="w-full border rounded px-2 py-1 mt-1 text-black bg-white">
                  <option value="guest">Guest</option>
                  <option value="admin">Admin</option>
                </select>
              </label>
              {registerError && <p className="text-red-600 text-sm">{registerError}</p>}
              <button type="submit" className="w-full bg-blue-700 text-white py-2 rounded" disabled={registerLoading}>
                {registerLoading ? "Registering..." : "Register"}
              </button>
            </form>
          </div>
        </div>
      )}

      {/* Navigation Bar */}
      <nav className="mb-8 flex items-center">
        <div className="flex space-x-4">
          <Link
            href="/"
            className={
              `text-blue-700 font-semibold hover:underline px-4 py-2 rounded ${pathname === "/" ? "border-2 border-blue-700 bg-blue-50" : ""}`
            }
            style={pathname === "/" ? { boxShadow: "0 0 0 2px #3b82f6" } : {}}
          >
            All Challenges
          </Link>
          <Link
            href="/learning-pathways"
            className={
              `text-blue-700 font-semibold hover:underline px-4 py-2 rounded ${pathname === "/learning-pathways" ? "border-2 border-blue-700 bg-blue-50" : ""}`
            }
            style={pathname === "/learning-pathways" ? { boxShadow: "0 0 0 2px #3b82f6" } : {}}
          >
            Learning Pathways
          </Link>
        </div>
      </nav>
      <h1 className="text-3xl font-bold text-center mb-10">Learning Pathways</h1>
      {pathways.map((pathway) => (
        <section key={pathway.name} className="mb-12">
          <h2 className="text-2xl font-semibold mb-6">{pathway.name}</h2>
          <div className="flex flex-row items-center space-x-6 overflow-x-auto pb-4">
            {getChallengesByIds(pathway.challengeIds).map((challenge, idx, arr) => (
              <React.Fragment key={challenge.id}>
                <Link href={`/challenges/${challenge.id}`} className="block">
                  <ChallengeCard challenge={challenge} />
                </Link>
                {idx < arr.length - 1 && (
                  <span className="text-2xl text-gray-400">→</span>
                )}
              </React.Fragment>
            ))}
          </div>
        </section>
      ))}
    </div>
  );
}
