"use client";

import React, { useState, useEffect } from "react";
import { useLogin } from "@/components/LoginContext";
import { useRouter } from "next/navigation";
import Link from "next/link";

export default function NewChallengePage() {
  const router = useRouter();
  const { user, loading } = useLogin();
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState(null);

  // Form data
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    difficulty: "Easy",
    subcategory: "Data-Analytics",
    technology: "",
    dataset_url: "",
    dataset_description: "",
    overview: "",
    task: "",
    outcomes: "",
    image_1: "",
    image_2: "",
    sample_sol: ""
  });

  // Check for admin access
  useEffect(() => {
    if (!loading && (!user || user.userType !== "admin")) {
      router.push("/");
    }
  }, [user, loading, router]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    setError(null);
    
    try {
      const res = await fetch("/api/admin/challenges", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        credentials: "include",
        body: JSON.stringify(formData)
      });
      
      if (!res.ok) {
        const errorData = await res.json();
        throw new Error(errorData.error || "Failed to create challenge");
      }
      
      router.push("/admin/challenges");
    } catch (err) {
      setError(err.message);
      setIsSubmitting(false);
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
    <div className="max-w-4xl mx-auto px-4 py-8 bg-white">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-black">Add New Challenge</h1>
        <Link href="/admin/challenges" className="text-blue-700 hover:underline">
          Back to Manage Challenges
        </Link>
      </div>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit} className="space-y-6">
        <div>
          <label htmlFor="title" className="block text-sm font-medium text-black">
            Title <span className="text-red-600">*</span>
          </label>
          <input
            type="text"
            id="title"
            name="title"
            value={formData.title}
            onChange={handleChange}
            required
            className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-black"
          />
        </div>

        <div>
          <label htmlFor="difficulty" className="block text-sm font-medium text-black">
            Difficulty <span className="text-red-600">*</span>
          </label>
          <select
            id="difficulty"
            name="difficulty"
            value={formData.difficulty}
            onChange={handleChange}
            required
            className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-black"
          >
            <option value="Easy">Easy</option>
            <option value="Medium">Medium</option>
            <option value="Hard">Hard</option>
          </select>
        </div>

        <div>
          <label htmlFor="subcategory" className="block text-sm font-medium text-black">
            Subcategory <span className="text-red-600">*</span>
          </label>
          <select
            id="subcategory"
            name="subcategory"
            value={formData.subcategory}
            onChange={handleChange}
            required
            className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-black"
          >
            <option value="Data-Analytics">Data Analytics</option>
            <option value="Data-Visualization">Data Visualization</option>
            <option value="AI-ML">AI/ML</option>
            <option value="Case-Studies">Case Studies</option>
          </select>
        </div>

        <div>
          <label htmlFor="technology" className="block text-sm font-medium text-black">
            Technology
          </label>
          <input
            type="text"
            id="technology"
            name="technology"
            value={formData.technology}
            onChange={handleChange}
            className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-black"
            placeholder="Python, R, etc."
          />
        </div>

        <div>
          <label htmlFor="description" className="block text-sm font-medium text-black">
            Description
          </label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleChange}
            rows={4}
            className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-black"
          />
        </div>

        <div>
          <label htmlFor="dataset_url" className="block text-sm font-medium text-black">
            Dataset URL
          </label>
          <input
            type="text"
            id="dataset_url"
            name="dataset_url"
            value={formData.dataset_url}
            onChange={handleChange}
            className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-black"
          />
        </div>

        <div>
          <label htmlFor="dataset_description" className="block text-sm font-medium text-black">
            Dataset Description
          </label>
          <textarea
            id="dataset_description"
            name="dataset_description"
            value={formData.dataset_description}
            onChange={handleChange}
            rows={4}
            className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-black"
          />
        </div>

        <div>
          <label htmlFor="overview" className="block text-sm font-medium text-black">
            Overview
          </label>
          <textarea
            id="overview"
            name="overview"
            value={formData.overview}
            onChange={handleChange}
            rows={4}
            className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-black"
          />
        </div>

        <div>
          <label htmlFor="task" className="block text-sm font-medium text-black">
            Task
          </label>
          <textarea
            id="task"
            name="task"
            value={formData.task}
            onChange={handleChange}
            rows={6}
            className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-black"
          />
        </div>

        <div>
          <label htmlFor="outcomes" className="block text-sm font-medium text-black">
            Outcomes
          </label>
          <textarea
            id="outcomes"
            name="outcomes"
            value={formData.outcomes}
            onChange={handleChange}
            rows={4}
            className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-black"
          />
        </div>

        <div>
          <label htmlFor="image_1" className="block text-sm font-medium text-black">
            Image 1 URL
          </label>
          <input
            type="text"
            id="image_1"
            name="image_1"
            value={formData.image_1}
            onChange={handleChange}
            className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-black"
          />
        </div>

        <div>
          <label htmlFor="image_2" className="block text-sm font-medium text-black">
            Image 2 URL
          </label>
          <input
            type="text"
            id="image_2"
            name="image_2"
            value={formData.image_2}
            onChange={handleChange}
            className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-black"
          />
        </div>

        <div>
          <label htmlFor="sample_sol" className="block text-sm font-medium text-black">
            Sample Solution URL
          </label>
          <input
            type="text"
            id="sample_sol"
            name="sample_sol"
            value={formData.sample_sol}
            onChange={handleChange}
            className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-black"
          />
        </div>

        <div className="pt-5">
          <div className="flex justify-end">
            <Link
              href="/admin/challenges"
              className="rounded-md border border-gray-300 bg-white py-2 px-4 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            >
              Cancel
            </Link>
            <button
              type="submit"
              disabled={isSubmitting}
              className="ml-3 inline-flex justify-center rounded-md border border-transparent bg-blue-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            >
              {isSubmitting ? "Creating..." : "Create Challenge"}
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}
