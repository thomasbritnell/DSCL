// frontend/src/components/DifficultySelector.jsx
"use client";

import React from "react";

const difficulties = ["All", "Easy", "Medium", "Hard"];

export default function DifficultySelector({ selected, onChange }) {
  return (
    <div className="flex justify-center space-x-3 mt-4">
      {difficulties.map((diff) => (
        <button
          key={diff}
          onClick={() => onChange(diff)}
          className={`px-4 py-2 rounded-md font-medium transition ${
            selected === diff
              ? "bg-blue-600 text-white shadow-md"
              : "bg-gray-200 text-gray-700 hover:bg-gray-300"
          }`}
        >
          {diff}
        </button>
      ))}
    </div>
  );
}
