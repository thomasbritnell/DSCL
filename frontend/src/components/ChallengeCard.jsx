// frontend/src/components/ChallengeCard.jsx
"use client";

import React from "react";
import Link from "next/link";

export default function ChallengeCard({ challenge }) {
  // Define a small lookup for difficulty → (bg + text) classes
  const difficultyStyles = {
    Easy: "bg-green-100 text-green-800",
    Medium: "bg-yellow-100 text-yellow-800",
    Hard: "bg-red-100 text-red-800",
  };

  const diffClass =
    difficultyStyles[challenge.difficulty] || "bg-gray-100 text-gray-800";

  const subcatStyles = {
    "AI-ML": "bg-blue-100 text-blue-800",
    "Data-Visualization": "bg-purple-100 text-purple-800",
    "Data-Analytics": "bg-indigo-100 text-indigo-800",
    "Case-Studies": "bg-pink-100 text-pink-800",
  };
  const subClass =
    subcatStyles[challenge.subcategory] || "bg-gray-100 text-gray-800";

  return (
    <>
      {/* The entire card is now clickable */}
      <div className="bg-white border rounded-lg p-4 shadow-sm hover:shadow-md transition transform hover:-translate-y-1">
        <h3 className="text-lg font-semibold mb-2">{challenge.title}</h3>
        <p className="text-sm text-gray-700 mb-3 line-clamp-3">
          {challenge.description}
        </p>
        <div className="flex flex-wrap gap-2 mb-6">
          {/* Difficulty badge */}
          <span className={`text-xs px-2 py-1 rounded-full ${diffClass}`}>
            {challenge.difficulty}
          </span>

          {/* Subcategory badge */}
          <span className={`text-xs px-2 py-1 rounded-full ${subClass}`}>
            {challenge.subcategory.replace("-", " ")}
          </span>
        </div>
        <div className="mt-3 text-blue-600 text-sm font-medium">
          View Details ↗
        </div>
      </div>
    </>
  );
}
