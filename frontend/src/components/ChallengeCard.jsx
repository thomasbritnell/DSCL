// frontend/src/components/ChallengeCard.jsx
"use client";

import React from "react";
import Link from "next/link";

/**
 * ChallengeCard component displays a summary card for a challenge.
 * Shows title, description, difficulty, subcategory, and completion status.
 * @param {Object} props
 * @param {Object} props.challenge - Challenge data object
 * @returns {JSX.Element}
 */
export default function ChallengeCard({ challenge }) {
  // Lookup for difficulty badge styles
  const difficultyStyles = {
    Easy: "bg-green-100 text-black",
    Medium: "bg-yellow-100 text-black",
    Hard: "bg-red-100 text-black",
  };

  // Get difficulty badge class
  const diffClass =
    difficultyStyles[challenge.difficulty] || "bg-gray-100 text-black";

  // Lookup for subcategory badge styles
  const subcatStyles = {
    "AI-ML": "bg-blue-100 text-black",
    "Data-Visualization": "bg-purple-100 text-black",
    "Data-Analytics": "bg-indigo-100 text-black",
    "Case-Studies": "bg-pink-100 text-black",
  };
  // Get subcategory badge class
  const subClass =
    subcatStyles[challenge.subcategory] || "bg-gray-100 text-black";

  
  return (
    <>
      {/* Challenge card container */}
      <div className="bg-white border rounded-lg p-4 shadow-sm hover:shadow-md transition transform hover:-translate-y-1">
        {/* Challenge title */}
        <h3 className="text-lg font-semibold mb-2 text-black">{challenge.title}</h3>
        {/* Challenge description */}
        <p className="text-sm text-black mb-3 line-clamp-3">
          {challenge.description}
        </p>
        {/* Badges for difficulty and subcategory */}
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
        {/* Link to challenge details */}
        <div className="mt-3 text-black text-sm font-medium">
          View Details ↗
        </div>
      </div>
    </>
  );
}
