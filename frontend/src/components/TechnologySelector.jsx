// frontend/src/components/TechnologySelector.jsx
"use client";

import React from "react";

const TECHNOLOGIES = [
  { key: "All", label: "All Technologies" },
  { key: "pandas", label: "Pandas" },
  { key: "sklearn", label: "SciKitLearn" },
  { key: "matplotlib", label: "Matplotlib" },
];

export default function TechnologySelector({ selected, onChange }) {
  return (
    <div className="mt-6">
      <label
        htmlFor="tech-select"
        className="block text-sm font-medium text-gray-700 mb-1"
      >
        Technology
      </label>
      <select
        id="tech-select"
        value={selected}
        onChange={(e) => onChange(e.target.value)}
        className="mt-1 block w-full border border-gray-300 rounded-md bg-white py-2 px-3 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
      >
        {TECHNOLOGIES.map((t) => (
          <option key={t.key} value={t.key}>
            {t.label}
          </option>
        ))}
      </select>
    </div>
  );
}
