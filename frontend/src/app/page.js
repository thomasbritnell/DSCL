// frontend/src/app/page.js
"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import DifficultySelector from "../components/DifficultySelector";
import SubcategoryTabs from "../components/SubcategoryTabs";
import TechnologySelector from "../components/TechnologySelector";
import ChallengeCard from "../components/ChallengeCard";

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

export default function HomePage() {
  // ─── Two filter states (remove 'subject') ───────────────────────────
  const [difficulty, setDifficulty] = useState("All");
  const [subcategory, setSubcategory] = useState("All");
  const [technology, setTechnology] = useState("All");

  const [challenges, setChallenges] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // ─── Fetch whenever any filter changes ───────────────────────────────
  useEffect(() => {
    setLoading(true);
    setError(null);

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
        setLoading(false);
      });
  }, [difficulty, subcategory, technology]);

  // ─── Clear All Filters ───────────────────────────────────────────────
  function clearFilters() {
    setDifficulty("All");
    setSubcategory("All");
    setTechnology("All");
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8 bg-white">
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
      {loading && <p className="text-center mt-8 text-black">Loading challenges…</p>}
      {error && (
        <p className="text-center mt-8 text-red-700">
          Error: {error}
        </p>
      )}
      {!loading && !error && challenges.length === 0 && (
        <p className="text-center mt-8 text-black">
          No challenges match those filters.
        </p>
      )}

      {/* ── Grid of ChallengeCard ─────────────────────────────────────── */}
      {!loading && challenges.length > 0 && (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 mt-8">
          {challenges.map((ch) => (
            <Link key={ch.id} href={`/challenges/${ch.id}`} className="block" passHref>
              <ChallengeCard challenge={ch} />
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}
