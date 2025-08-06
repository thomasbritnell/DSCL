"use client";

import React, { useState, useEffect } from "react";
import { useLogin } from "@/components/LoginContext";
import { useRouter } from "next/navigation";
import Link from "next/link";

export default function ManageChallengesPage() {
  const router = useRouter();
  const { user, loading } = useLogin();
  const [challenges, setChallenges] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [editingChallenge, setEditingChallenge] = useState(null);
  const [isDeleting, setIsDeleting] = useState(false);
  const [deleteId, setDeleteId] = useState(null);

  // Check for admin access
  useEffect(() => {
    if (!loading && (!user || user.userType !== "admin")) {
      router.push("/");
    }
  }, [user, loading, router]);

  // Fetch challenges
  useEffect(() => {
    if (user?.userType === "admin") {
      fetchChallenges();
    }
  }, [user]);

  const fetchChallenges = async () => {
    try {
      setIsLoading(true);
      // Use the admin API endpoint
      const res = await fetch("/api/admin/challenges", {
        credentials: "include" // Include cookies for auth
      });
      if (!res.ok) {
        throw new Error("Failed to fetch challenges");
      }
      const data = await res.json();
      setChallenges(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleDelete = async (id) => {
    try {
      setIsDeleting(true);
      setDeleteId(id);
      const res = await fetch(`/api/admin/challenges/${id}`, {
        method: "DELETE",
        credentials: "include"
      });
      
      if (!res.ok) {
        throw new Error("Failed to delete challenge");
      }
      
      setChallenges(challenges.filter(c => c.id !== id));
    } catch (err) {
      setError(err.message);
    } finally {
      setIsDeleting(false);
      setDeleteId(null);
    }
  };

  const confirmDelete = (id) => {
    if (window.confirm("Are you sure you want to delete this challenge? This cannot be undone.")) {
      handleDelete(id);
    }
  };

  // If still loading auth status or not an admin, don't show page content
  if (loading || !user || user.userType !== "admin") {
    return (
      <div className="max-w-6xl mx-auto px-4 py-8 bg-white">
        {loading ? (
          <p className="text-center text-black">Loading...</p>
        ) : (
          <p className="text-center text-red-600">You don&apos;t have permission to access this page.</p>
        )}
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8 bg-white">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-black">Manage Challenges</h1>
        <Link href="/" className="text-blue-700 hover:underline">
          Back to Home
        </Link>
      </div>

      <div className="mb-6">
        <Link 
          href="/admin/challenges/new" 
          className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
        >
          Add New Challenge
        </Link>
      </div>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {isLoading ? (
        <p className="text-center text-black">Loading challenges...</p>
      ) : (
        <div className="overflow-x-auto">
          <table className="min-w-full bg-white border border-gray-200">
            <thead>
              <tr className="bg-gray-100 text-black">
                <th className="py-2 px-4 border-b text-left">ID</th>
                <th className="py-2 px-4 border-b text-left">Title</th>
                <th className="py-2 px-4 border-b text-left">Difficulty</th>
                <th className="py-2 px-4 border-b text-left">Subcategory</th>
                <th className="py-2 px-4 border-b text-left">Actions</th>
              </tr>
            </thead>
            <tbody>
              {challenges.map((challenge) => (
                <tr key={challenge.id} className="text-black hover:bg-gray-50">
                  <td className="py-2 px-4 border-b">{challenge.id}</td>
                  <td className="py-2 px-4 border-b">{challenge.title}</td>
                  <td className="py-2 px-4 border-b">{challenge.difficulty}</td>
                  <td className="py-2 px-4 border-b">{challenge.subcategory}</td>
                  <td className="py-2 px-4 border-b">
                    <div className="flex space-x-2">
                      <Link 
                        href={`/admin/challenges/edit/${challenge.id}`} 
                        className="bg-blue-600 text-white px-2 py-1 rounded text-sm hover:bg-blue-700"
                      >
                        Edit
                      </Link>
                      <button
                        onClick={() => confirmDelete(challenge.id)}
                        className="bg-red-600 text-white px-2 py-1 rounded text-sm hover:bg-red-700"
                        disabled={isDeleting && deleteId === challenge.id}
                      >
                        {isDeleting && deleteId === challenge.id ? "Deleting..." : "Delete"}
                      </button>
                      <Link 
                        href={`/challenges/${challenge.id}`} 
                        className="bg-gray-600 text-white px-2 py-1 rounded text-sm hover:bg-gray-700"
                        target="_blank"
                      >
                        View
                      </Link>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
