// frontend/src/components/TechnologySelector.jsx

import React from "react";

/**
 * TechnologySelector displays a dropdown for filtering by technology.
 * @param {Object} props
 * @param {string} props.selected - Currently selected technology
 * @param {Function} props.onChange - Callback for technology change
 * @returns {JSX.Element}
 */
const TECHNOLOGIES = [
  { key: "All", label: "All Technologies" },
  { key: "pandas", label: "Pandas" },
  { key: "sklearn", label: "SciKitLearn" },
  { key: "matplotlib", label: "Matplotlib" },
  { key: "tensorflow", label: "TensorFlow" },
  { key: "keras", label: "Keras" },
  { key: "pytorch", label: "PyTorch" },
  { key: "numpy", label: "NumPy" },
  { key: "opencv", label: "OpenCV" },
  { key: "nltk", label: "Natural Language Toolkit" },
  { key: "seaborn", label: "Seaborn" },
  { key: "scipi", label: "SciPi" },
];

export default function TechnologySelector({ selected, onChange }) {
  return (
    <div className="mt-6">
      <label
        htmlFor="tech-select"
        className="block text-sm font-medium text-black mb-1"
      >
        Technology
      </label>
      <select
        id="tech-select"
        value={selected}
        onChange={(e) => onChange(e.target.value)}
        className="mt-1 block w-full border border-gray-300 rounded-md bg-white py-2 px-3 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500 text-black"
      >
        {TECHNOLOGIES.map((t) => (
          <option key={t.key} value={t.key} className="text-black">
            {t.label}
          </option>
        ))}
      </select>
    </div>
  );
}
