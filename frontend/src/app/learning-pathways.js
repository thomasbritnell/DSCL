// frontend/src/app/learning-pathways.js
"use client";

import React, { useEffect, useState } from "react";
import { usePathname } from "next/navigation";
import Link from "next/link";
import ChallengeCard from "../components/ChallengeCard";
// Pathways are now fetched from backend API

/**
 * LearningPathwaysPage displays groups of challenge cards for each pathway.
 * @returns {JSX.Element}
 */
export default function LearningPathwaysPage() {
  const pathname = usePathname();
  const [challenges, setChallenges] = useState([]);
  const [pathways, setPathways] = useState([]);

  // Fetch all challenges and pathways once for mapping
  useEffect(() => {
    fetch("/api/challenges")
      .then((res) => res.json())
      .then((data) => setChallenges(data));
    fetch("/api/pathways")
      .then((res) => res.json())
      .then((data) => setPathways(data));
  }, []);

  // Helper to get challenge objects by ID
  function getChallengesByIds(ids) {
    return challenges.filter((ch) => ids.includes(ch.id));
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8 bg-white text-black">
      {/* Navigation Bar */}
      <nav className="mb-8 flex items-center">
        <div className="flex space-x-4">
          <Link
            href="/"
            className={
              `text-blue-700 font-semibold hover:underline px-4 py-2 rounded ${pathname === "/" ? "border-2 border-blue-700 bg-blue-50" : ""}`
            }
            style={pathname === "/" ? { boxShadow: "0 0 0 2px #3b82f6" } : {}}
          >
            All Challenges
          </Link>
          <Link
            href="/learning-pathways"
            className={
              `text-blue-700 font-semibold hover:underline px-4 py-2 rounded ${pathname === "/learning-pathways" ? "border-2 border-blue-700 bg-blue-50" : ""}`
            }
            style={pathname === "/learning-pathways" ? { boxShadow: "0 0 0 2px #3b82f6" } : {}}
          >
            Learning Pathways
          </Link>
        </div>
      </nav>
      <h1 className="text-3xl font-bold text-center mb-10">Learning Pathways</h1>
      {pathways.map((pathway) => (
        <section key={pathway.name} className="mb-12">
          <h2 className="text-2xl font-semibold mb-6">{pathway.name}</h2>
          <div className="flex flex-row items-center space-x-6 overflow-x-auto pb-4">
            {getChallengesByIds(pathway.challengeIds).map((challenge, idx, arr) => (
              <React.Fragment key={challenge.id}>
                <Link href={`/challenges/${challenge.id}`} className="block">
                  <ChallengeCard challenge={challenge} />
                </Link>
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
