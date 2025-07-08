// frontend/src/app/challenges/[id]/page.js

import React from "react";
import Link from "next/link";

export default async function ChallengeDetailPage({ params }) {
  // Await params before destructuring
  const { id } = params;

  // Fetch the challenge data from our Flask API (use relative path for production)
  // Use absolute URL for server-side fetch
  const baseUrl = "http://backend:5000";
  const res = await fetch(`${baseUrl}/api/challenges/${id}`, {
    cache: "no-store",
  });
  
  if (!res.ok) {
    return (
      <div className="max-w-3xl mx-auto px-4 py-8">
        <h1 className="text-2xl font-semibold text-red-600 mb-4">
          Challenge not found
        </h1>
        <p className="text-gray-700 mb-8">
          Sorry, we couldn’t find a challenge with ID {id}.
        </p>
        <Link href="/" className="text-blue-600 font-medium hover:underline">
          ← Back to all challenges
        </Link>
      </div>
    );
  }

  const challenge = await res.json();
  // challenge = { id, title, description, difficulty, subcategory, technology, dataset_url, overview, task, outcomes }

  return (
    <div className="max-w-3xl mx-auto px-4 py-10">
      {/* Back to all challenges */}
      <Link href="/" className="text-blue-600 font-medium hover:underline mb-6 inline-block">
        ← Back to all challenges
      </Link>

      {/* Title */}
      <h1 className="text-3xl font-bold mb-2">{challenge.title}</h1>

      {/* Difficulty & Subcategory Badges */}
      <div className="flex flex-wrap gap-2 mb-6">
        <span className="text-xs px-2 py-1 bg-blue-100 text-blue-800 rounded-full">
          {challenge.difficulty}
        </span>
        <span className="text-xs px-2 py-1 bg-gray-100 text-gray-800 rounded-full">
          {challenge.subcategory.replace("-", " ")}
        </span>
      </div>

      {/* Technology Badge */}
      {challenge.technology && (
        <div className="mb-6">
          <span className="text-xs px-2 py-1 bg-green-100 text-green-800 rounded-full">
            {challenge.technology}
          </span>
        </div>
      )}

      {/* Dataset Link */}
      {challenge.dataset_url && (
        <p className="mb-6">
          <strong>Dataset URL:</strong>{" "}
          <a
            href={challenge.dataset_url}
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-600 hover:underline break-all"
          >
            {challenge.dataset_url}
          </a>
        </p>
      )}

      {/* Overview */}
      {challenge.overview && (
        <section className="mb-6">
          <h2 className="text-2xl font-semibold mb-2">Overview</h2>
          <p className="text-gray-800 whitespace-pre-line">{challenge.overview}</p>
        </section>
      )}

      {/* Description */}
      {challenge.description && (
        <section className="mb-6">
          <h2 className="text-2xl font-semibold mb-2">Description</h2>
          <p className="text-gray-800 whitespace-pre-line">{challenge.description}</p>
        </section>
      )}

      {/* Task to Perform */}
      {challenge.task && (
        <section className="mb-6">
          <h2 className="text-2xl font-semibold mb-2">Task to Perform</h2>
          <pre className="bg-gray-100 p-4 rounded-md overflow-x-auto whitespace-pre-wrap">
            {challenge.task}
          </pre>
        </section>
      )}

      {/* Required Outcomes */}
      {challenge.outcomes && (
        <section className="mb-6">
          <h2 className="text-2xl font-semibold mb-2">Required Outcomes</h2>
          <pre className="bg-gray-100 p-4 rounded-md overflow-x-auto whitespace-pre-wrap">
            {challenge.outcomes}
          </pre>
        </section>
      )}

      {/* Additional Notes */}
      <section className="mb-6">
        <h2 className="text-2xl font-semibold mb-2">Additional Notes</h2>
        <p className="text-gray-800">
          • Make sure your final submission includes a well‐commented Jupyter Notebook or Python script.  
          <br />
          • Include any charts as embedded PNG or interactive HTML (if using Plotly).  
          <br />
          • Write a short README explaining how to run your code and interpret your results.
        </p>
      </section>
    </div>
  );
}
