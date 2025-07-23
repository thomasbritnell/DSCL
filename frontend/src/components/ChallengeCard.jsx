// frontend/src/components/ChallengeCard.jsx
"use client";

import React from "react";
import Link from "next/link";

export default function ChallengeCard({ challenge }) {
  // Define a small lookup for difficulty → (bg + text) classes
  const difficultyStyles = {
    Easy: "bg-green-100 text-black",
    Medium: "bg-yellow-100 text-black",
    Hard: "bg-red-100 text-black",
  };

  const diffClass =
    difficultyStyles[challenge.difficulty] || "bg-gray-100 text-black";

  const subcatStyles = {
    "AI-ML": "bg-blue-100 text-black",
    "Data-Visualization": "bg-purple-100 text-black",
    "Data-Analytics": "bg-indigo-100 text-black",
    "Case-Studies": "bg-pink-100 text-black",
  };
  const subClass =
    subcatStyles[challenge.subcategory] || "bg-gray-100 text-gray-800";

  return (
    <>
      {/* The entire card is now clickable */}
      <div className="bg-white border rounded-lg p-4 shadow-sm hover:shadow-md transition transform hover:-translate-y-1">
        <h3 className="text-lg font-semibold mb-2 text-black">{challenge.title}</h3>
        <p className="text-sm text-black mb-3 line-clamp-3">
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
        {/* {user && (
          <label className="flex items-center mb-2 select-none">
            <input
              type="checkbox"
              checked={!!completed[challenge.id]}
              onChange={() => toggleCompleted(challenge.id)}
              className="mr-2"
            />
            <span className="text-sm text-black">Completed</span>
          </label>
        )} */}
        <div className="mt-3 text-black text-sm font-medium">
          View Details ↗
        </div>
      </div>
    </>
  );
}
