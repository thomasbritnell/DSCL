// frontend/src/components/SubjectSelector.jsx
"use client";

import React from "react";

const SUBJECTS = [
  { key: "All", label: "All Subjects" },
  { key: "AIDI1011", label: "AIDI1011" },
  { key: "AIDI1012", label: "AIDI1012" },
  { key: "AIDI1013", label: "AIDI1013" },
  { key: "AIDI1020", label: "AIDI1020" },
  // …any other course codes you use…
];

export default function SubjectSelector({ selected, onChange }) {
  return (
    <div className="mt-6">
      <label htmlFor="subject-select" className="block text-sm font-medium text-gray-700 mb-1">
        Subject (Course Code)
      </label>
      <select
        id="subject-select"
        value={selected}
        onChange={(e) => onChange(e.target.value)}
        className="mt-1 block w-full border border-gray-300 rounded-md bg-white py-2 px-3 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
      >
        {SUBJECTS.map((s) => (
          <option key={s.key} value={s.key}>
            {s.label}
          </option>
        ))}
      </select>
    </div>
  );
}
