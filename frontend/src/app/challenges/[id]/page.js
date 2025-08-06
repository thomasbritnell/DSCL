// frontend/src/app/challenges/[id]/page.js

import React from "react";
import Link from "next/link";
import ChallengeDetail from "@/components/ChallengeDetail";

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

// The ChallengeDetail component has been moved to a client component in the components directory
