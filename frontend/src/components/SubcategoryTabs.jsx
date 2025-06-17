// frontend/src/components/SubcategoryTabs.jsx
"use client";

import React from "react";

export default function SubcategoryTabs({ subcats, selected, onChange }) {
  return (
    <div className="flex justify-center space-x-4 mt-6 border-b border-gray-300 pb-2">
      {subcats.map((sc) => (
        <button
          key={sc.key}
          onClick={() => onChange(sc.key)}
          className={`px-3 py-1 font-medium text-sm transition ${
            selected === sc.key
              ? "border-b-2 border-blue-600 text-blue-600"
              : "text-gray-600 hover:text-gray-800"
          }`}
        >
          {sc.label}
        </button>
      ))}
    </div>
  );
}
