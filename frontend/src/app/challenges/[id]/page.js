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
      <div className="max-w-3xl mx-auto px-4 py-8 bg-white">
        <h1 className="text-2xl font-semibold text-red-700 mb-4">
          Challenge not found
        </h1>
        <p className="text-black mb-8">
          Sorry, we couldn’t find a challenge with ID {id}.
        </p>
        <Link href="/" className="text-blue-700 font-medium hover:underline">
          ← Back to all challenges
        </Link>
      </div>
    );
  }

  const challenge = await res.json();
  // challenge = { id, title, description, difficulty, subcategory, technology, dataset_url, overview, task, outcomes }

  return (
    <div className="max-w-3xl mx-auto px-4 py-10 bg-white">
      {/* Back to all challenges */}
      <Link href="/" className="text-blue-700 font-medium hover:underline mb-6 inline-block">
        ← Back to all challenges
      </Link>

      {/* Title */}
      <h1 className="text-3xl font-bold mb-2 text-black">{challenge.title}</h1>

      {/* Difficulty & Subcategory Badges */}
      <div className="flex flex-wrap gap-2 mb-6">
        <span className="text-xs px-2 py-1 bg-blue-200 text-blue-900 rounded-full">
          {challenge.difficulty}
        </span>
        <span className="text-xs px-2 py-1 bg-gray-300 text-black rounded-full">
          {challenge.subcategory.replace("-", " ")}
        </span>
      </div>

      {/* Technology Badge */}
      {challenge.technology && (
        <div className="mb-6">
          <span className="text-xs px-2 py-1 bg-green-200 text-green-900 rounded-full">
            {challenge.technology}
          </span>
        </div>
      )}

      {/* Challenge Image */}
      {challenge.image_1 && (
        <div className="mb-6 flex justify-center">
          <img
            src={challenge.image_1}
            alt={challenge.title + " image 1"}
            className="w-full max-w-md h-64 object-cover rounded-lg shadow"
            style={{ backgroundColor: "#fff" }}
          />
        </div>
      )}


      {/* Dataset Link */}
      {challenge.dataset_url && (
        <p className="mb-6 text-black">
          <strong>Dataset URL:</strong>{" "}
          <a
            href={challenge.dataset_url}
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-700 hover:underline break-all"
          >
            {challenge.dataset_url}
          </a>
        </p>
      )}

      {/* Dataset Description */}
      {challenge.dataset_description && (
        <section className="mb-6">
          <h2 className="text-2xl font-semibold mb-2 text-black">Dataset Description</h2>
          <p className="text-black whitespace-pre-line">{challenge.dataset_description}</p>
        </section>
      )}

      {/* Challenge Image 2 */}
      {challenge.image_2 && (
        <div className="mb-6 flex justify-center">
          <img
            src={challenge.image_2}
            alt={challenge.title + " image 2"}
            className="w-full max-w-md h-64 object-cover rounded-lg shadow"
            style={{ backgroundColor: "#fff" }}
          />
        </div>
      )}

      {/* Overview */}
      {challenge.overview && (
        <section className="mb-6">
          <h2 className="text-2xl font-semibold mb-2 text-black">Overview</h2>
          <p className="text-black whitespace-pre-line">{challenge.overview}</p>
        </section>
      )}

      {/* Description */}
      {challenge.description && (
        <section className="mb-6">
          <h2 className="text-2xl font-semibold mb-2 text-black">Description</h2>
          <p className="text-black whitespace-pre-line">{challenge.description}</p>
        </section>
      )}

      {/* Steps */}
      {challenge.task && (
        <section className="mb-6">
          <h2 className="text-2xl font-semibold mb-2 text-black">Steps</h2>
          <pre className="bg-gray-300 p-4 rounded-md overflow-x-auto whitespace-pre-wrap text-black">
            {challenge.task}
          </pre>
        </section>
      )}

      {/* Required Outcomes */}
      {challenge.outcomes && (
        <section className="mb-6">
          <h2 className="text-2xl font-semibold mb-2 text-black">Required Outcomes</h2>
          <pre className="bg-gray-300 p-4 rounded-md overflow-x-auto whitespace-pre-wrap text-black">
            {challenge.outcomes}
          </pre>
        </section>
      )}

      {/* Sample Solution Link */}
      {challenge.sample_sol && (
        <section className="mb-8">
          <p className="text-black">
            <strong>
              Only click this once you are done and wanting to check your answers:
            </strong>{" "}
            <a
              href={challenge.sample_sol}
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-700 hover:underline break-all"
            >
              {challenge.sample_sol}
            </a>
          </p>
        </section>
      )}

    </div>
  );
}
