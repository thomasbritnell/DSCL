// frontend/src/app/page.js
"use client";

import React, { useState, useEffect } from "react";
import { usePathname } from "next/navigation";
import Link from "next/link";
import DifficultySelector from "../components/DifficultySelector";
import SubcategoryTabs from "../components/SubcategoryTabs";
import TechnologySelector from "../components/TechnologySelector";
import ChallengeCard from "../components/ChallengeCard";
import { useLogin } from "../components/LoginContext";
import LoginForm from "../components/LoginForm";

// List of subcategories for filtering challenges
const SUBCATEGORIES = [
  { key: "All", label: "All Topics" },
  { key: "Imputation", label: "Imputation" },
  { key: "Data Cleaning", label: "Data Cleaning" },
  { key: "Data Preparation", label: "Data Preparation" },
  { key: "Outliers", label: "Outliers" },
  { key: "Statistics", label: "Statistics" },
  { key: "Time Series", label: "Time Series" },
  { key: "Feature Importance", label: "Feature Importance" },
  { key: "Classification", label: "Classification" },
  { key: "Metrics", label: "Metrics" },
  { key: "NLP", label: "NLP" },
  { key: "Sentiment Analysis", label: "Sentiment Analysis" },
  { key: "Clustering", label: "Clustering" },
  { key: "Neural Nets", label: "Neural Nets" },
];

/**
 * HomePage component displays the main challenge library UI.
 * Includes filters, challenge cards, and error/loading states.
 * @returns {JSX.Element}
 */
export default function HomePage() {
  const { user, loading, login, logout } = useLogin();
  const [showLogin, setShowLogin] = useState(false);
  const [showRegister, setShowRegister] = useState(false);
  const [registerError, setRegisterError] = useState(null);
  const [registerLoading, setRegisterLoading] = useState(false);

  // Registration handler
  async function handleRegister(e) {
    e.preventDefault();
    setRegisterError(null);
    setRegisterLoading(true);
    const form = e.target;
    const username = form.username.value;
    const password = form.password.value;
    try {
      const res = await fetch("/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
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
  // State for filters
  const [difficulty, setDifficulty] = useState("All");
  const [subcategory, setSubcategory] = useState("All");
  const [technology, setTechnology] = useState("All");

  // State for challenge data and UI status
  const [challenges, setChallenges] = useState([]);
  const [challengeLoading, setChallengeLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch challenges whenever filters change
  useEffect(() => {
    setChallengeLoading(true);
    setError(null);

    // Build query params for API
    const params = new URLSearchParams();
    if (difficulty !== "All") {
      params.append("difficulty", difficulty);
    }
    if (subcategory !== "All") {
      params.append("subcategory", subcategory);
    }
    if (technology !== "All") {
      params.append("technology", technology);
    }

    const url = params.toString()
      ? `/api/challenges?${params.toString()}`
      : `/api/challenges`;

    // Fetch challenge data from backend
    fetch(url)
      .then((res) => {
        if (!res.ok) throw new Error("Failed to load challenges.");
        return res.json();
      })
      .then((data) => {
        setChallenges(data);
      })
      .catch((err) => {
        console.error(err);
        setError(err.message || "Unknown error");
      })
      .finally(() => {
        setChallengeLoading(false);
      });
  }, [difficulty, subcategory, technology]);

  // Reset all filters to default
  function clearFilters() {
    setDifficulty("All");
    setSubcategory("All");
    setTechnology("All");
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8 bg-white relative">
      {/* User status and auth menu */}
      <div className="absolute right-0 top-0 mt-4 mr-4 z-10">
      {loading ? null : user ? (
          <div className="flex items-center space-x-2">
            <span className="text-sm text-gray-700">Logged in as <span className="font-semibold">{user.username}</span></span>
            <button onClick={logout} className="text-blue-700 text-sm hover:underline">Logout</button>
          </div>
        ) : (
          <div className="flex items-center space-x-2">
            <span className="text-sm text-gray-700">Guest</span>
            <button onClick={() => setShowLogin(true)} className="text-blue-700 text-sm hover:underline">Sign In</button>
            <button onClick={() => setShowRegister(true)} className="text-blue-700 text-sm hover:underline">Register</button>
          </div>
        )}
      </div>

      {/* Login Modal */}
      {showLogin && (
        <div className="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded shadow-lg w-full max-w-xs relative">
            <button onClick={() => setShowLogin(false)} className="absolute top-2 right-2 text-gray-400 hover:text-gray-700">✕</button>
            <LoginForm onLoginSuccess={() => { 
              setShowLogin(false); 
              // Force a re-fetch of the current user
              fetch("/api/me", { credentials: "include" })
                .then(res => res.ok ? res.json() : null)
                .then(data => {
                  if (data && data.username) {
                    login(data.username);
                  }
                });
            }} />
            </div>
          </div>
          )}

          {/* Register Modal */}
          {showRegister && (
          <div className="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50">
            <div className="bg-white p-6 rounded shadow-lg w-full max-w-xs relative">
            <button onClick={() => setShowRegister(false)} className="absolute top-2 right-2 text-black hover:text-black">✕</button>
            <form onSubmit={handleRegister} className="space-y-4">
              <h2 className="text-lg font-semibold mb-2 text-black">Register</h2>
              <label className="block text-black">
              Username:
              <input name="username" type="text" required className="w-full border rounded px-2 py-1 mt-1 text-black" />
              </label>
              <label className="block text-black">
              Password:
              <input name="password" type="password" required className="w-full border rounded px-2 py-1 mt-1 text-black" />
              </label>
              {registerError && <p className="text-red-600 text-sm text-black">{registerError}</p>}
              <button type="submit" className="w-full bg-blue-700 text-black py-2 rounded" disabled={registerLoading}>
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

      <h1 className="text-3xl font-bold text-center mb-6 text-black">
        Data Science Challenge Library
      </h1>

      {/* ── Filter Controls ─────────────────────────────────────────────── */}
      <div className="space-y-6">
        <DifficultySelector
          selected={difficulty}
          onChange={(diff) => {
            setDifficulty(diff);
            // Reset subcategory whenever difficulty changes
            setSubcategory("All");
          }}
        />

        {/* ── Always show SubcategoryTabs ─────────────────────────────── */}
        <SubcategoryTabs
          subcats={SUBCATEGORIES}
          selected={subcategory}
          onChange={(sc) => setSubcategory(sc)}
        />

        <TechnologySelector
          selected={technology}
          onChange={(tech) => setTechnology(tech)}
        />

        {/* Clear Filters Button */}
        <button
          onClick={clearFilters}
          className="mt-2 inline-block text-sm text-blue-700 hover:underline"
        >
          Clear All Filters
        </button>
      </div>

      {/* ── Display Loading, Error, or “No Results” ─────────────────────── */}
      {challengeLoading && (
        <p className="text-center mt-8 text-black">Loading challenges…</p>
      )}
      {error && (
        <p className="text-center mt-8 text-red-700">Error: {error}</p>
      )}
      {!challengeLoading && !error && challenges.length === 0 && (
        <p className="text-center mt-8 text-black">
          No challenges match those filters.
        </p>
      )}

      {/* ── Grid of ChallengeCard ─────────────────────────────────────── */}
      {!challengeLoading && challenges.length > 0 && (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 mt-8">
          {challenges.map((ch) => (
            <Link
              key={ch.id}
              href={`/challenges/${ch.id}`}
              className="block"
              passHref
            >
              <ChallengeCard challenge={ch} />
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}
