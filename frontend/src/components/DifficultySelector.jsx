// frontend/src/components/DifficultySelector.jsx

import React from "react";

/**
 * DifficultySelector displays filter buttons for challenge difficulty.
 * @param {Object} props
 * @param {string} props.selected - Currently selected difficulty
 * @param {Function} props.onChange - Callback for difficulty change
 * @returns {JSX.Element}
 */
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
              ? "bg-blue-600 text-black shadow-md"
              : "bg-gray-200 text-black hover:bg-gray-300"
          }`}
        >
          {diff}
        </button>
      ))}
    </div>
  );
}
