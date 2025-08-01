// frontend/src/app/challenges/[id]/page.js

import React from "react";
import Link from "next/link";

/**
 * ChallengeDetailPage fetches and displays details for a single challenge.
 * Shows badges, images, dataset info, and solution link.
 * @param {Object} props
 * @param {Object} props.params - Route params (contains challenge id)
 * @returns {JSX.Element}
 */
export default async function ChallengeDetailPage({ params }) {
  // Get challenge id from route params
  const { id } = params;
  const challengeId = parseInt(id);

  // Fetch challenge data from Flask API
  const baseUrl = "http://backend:5000";
  const res = await fetch(`${baseUrl}/api/challenges/${id}`, {
    cache: "no-store",
  });

  // If challenge not found, show error message
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

  // Parse challenge data from response
  const challenge = await res.json();

  // Fetch all pathways from backend
  const pathwaysRes = await fetch(`${baseUrl}/api/pathways`, { cache: "no-store" });
  let pathway = null;
  let pathwayChallenges = [];
  if (pathwaysRes.ok) {
    const pathways = await pathwaysRes.json();
    pathway = pathways.find(p => p.challengeIds.includes(challengeId));
    if (pathway) {
      // Fetch all challenges in the pathway for their titles
      const idsParam = pathway.challengeIds.join(",");
      const challengesRes = await fetch(`${baseUrl}/api/challenges?ids=${idsParam}`, { cache: "no-store" });
      if (challengesRes.ok) {
        pathwayChallenges = await challengesRes.json();
      }
    }
  }

  return <ChallengeDetail challenge={challenge} pathway={pathway} pathwayChallenges={pathwayChallenges} />;
}

function abbreviateTitle(title) {
  // Abbreviate to first 18 chars, add ellipsis if longer
  return title.length > 18 ? title.slice(0, 15) + "…" : title;
}

function ChallengeDetail({ challenge, pathway, pathwayChallenges }) {
  return (
    <div className="max-w-3xl mx-auto px-4 py-10 bg-white">
      {/* Back to all challenges */}
      <Link href="/" className="text-blue-700 font-medium hover:underline mb-6 inline-block">
        ← Back to all challenges
      </Link>

      {/* Pathway Navigation (if applicable) */}
      {pathway && (
        <div className="mb-8">
          <h2 className="text-xl font-semibold mb-2 text-black">Pathway: {pathway.name}</h2>
          <div className="flex flex-row items-center space-x-4 overflow-x-auto pb-2">
            {pathway.challengeIds.map(cid => {
              const ch = pathwayChallenges.find(c => c.id === cid);
              const label = ch ? abbreviateTitle(ch.title) : `Challenge ${cid}`;
              return cid === challenge.id ? (
                <span key={cid} className="font-bold text-blue-700 text-lg underline">{label}</span>
              ) : (
                <Link key={cid} href={`/challenges/${cid}`} className="text-blue-700 font-medium hover:underline">
                  {label}
                </Link>
              );
            })}
          </div>
        </div>
      )}

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
