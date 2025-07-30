// frontend/src/app/learning-pathways.js
"use client";

import React, { useEffect, useState } from "react";
import Link from "next/link";
import ChallengeCard from "../components/ChallengeCard";
import { LEARNING_PATHWAYS } from "./pathwaysData";

/**
 * LearningPathwaysPage displays groups of challenge cards for each pathway.
 * @returns {JSX.Element}
 */
export default function LearningPathwaysPage() {
  const [challenges, setChallenges] = useState([]);

  // Fetch all challenges once for mapping
  useEffect(() => {
    fetch("/api/challenges")
      .then((res) => res.json())
      .then((data) => setChallenges(data));
  }, []);

  // Helper to get challenge objects by ID
  function getChallengesByIds(ids) {
    return challenges.filter((ch) => ids.includes(ch.id));
  }

  return (
    <div className="max-w-5xl mx-auto px-4 py-10">
      <h1 className="text-3xl font-bold text-center mb-10 text-black">Learning Pathways</h1>
      <Link href="/" className="text-blue-700 font-medium hover:underline mb-8 inline-block">← Back to All Challenges</Link>
      {LEARNING_PATHWAYS.map((pathway) => (
        <section key={pathway.name} className="mb-12">
          <h2 className="text-2xl font-semibold mb-6 text-black">{pathway.name}</h2>
          <div className="flex flex-row items-center space-x-6 overflow-x-auto pb-4">
            {getChallengesByIds(pathway.challengeIds).map((challenge, idx, arr) => (
              <React.Fragment key={challenge.id}>
                <ChallengeCard challenge={challenge} />
                {idx < arr.length - 1 && (
                  <span className="text-2xl text-gray-400">→</span>
                )}
              </React.Fragment>
            ))}
          </div>
        </section>
      ))}
    </div>
  );
}
