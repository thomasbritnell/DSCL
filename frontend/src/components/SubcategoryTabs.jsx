// frontend/src/components/SubcategoryTabs.jsx

import React, { useState } from "react";

/**
 * SubcategoryTabs displays a capped set of subcategory filter buttons with navigation.
 * Shows up to MAX_VISIBLE tabs at a time, with next/prev navigation for overflow.
 * @param {Object} props
 * @param {Array} props.subcats - Array of subcategory objects
 * @param {string} props.selected - Currently selected subcategory key
 * @param {Function} props.onChange - Callback for tab change
 * @returns {JSX.Element}
 */
const MAX_VISIBLE = 7;

export default function SubcategoryTabs({ subcats, selected, onChange }) {
  const [startIdx, setStartIdx] = useState(0);
  const endIdx = Math.min(startIdx + MAX_VISIBLE, subcats.length);
  const canPrev = startIdx > 0;
  const canNext = endIdx < subcats.length;

  function handlePrev() {
    setStartIdx(Math.max(0, startIdx - MAX_VISIBLE));
  }
  function handleNext() {
    setStartIdx(Math.min(subcats.length - MAX_VISIBLE, startIdx + MAX_VISIBLE));
  }

  return (
    <div className="flex items-center justify-center mt-6 border-b border-gray-300 pb-2">
      {/* Previous button for overflow navigation */}
      {canPrev && (
        <button
          onClick={handlePrev}
          className="px-2 py-1 mr-2 text-black border rounded bg-gray-200 hover:bg-gray-300"
        >
          ◀
        </button>
      )}
      {/* Visible subcategory tabs */}
      <div className="flex space-x-4 overflow-x-auto scrollbar-hide">
        {subcats.slice(startIdx, endIdx).map((sc) => (
          <button
            key={sc.key}
            onClick={() => onChange(sc.key)}
            className={`px-3 py-1 font-medium text-sm transition whitespace-nowrap ${
              selected === sc.key
                ? "border-b-2 border-blue-600 text-black"
                : "text-black"
            }`}
          >
            {sc.label}
          </button>
        ))}
      </div>
      {/* Next button for overflow navigation */}
      {canNext && (
        <button
          onClick={handleNext}
          className="px-2 py-1 ml-2 text-black border rounded bg-gray-200 hover:bg-gray-300"
        >
          ▶
        </button>
      )}
    </div>
  );
}
