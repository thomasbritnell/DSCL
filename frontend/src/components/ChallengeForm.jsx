'use client';

import { useState, useEffect } from 'react';
import { useAdminProtection } from '@/hooks/useAdminProtection';
import { useRouter } from 'next/navigation';

export default function ChallengeForm({ challengeId = null }) {
  const router = useRouter();
  const { isAdmin, loading } = useAdminProtection();
  
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    difficulty: 'Easy',
    subcategory: '',
    technology: '',
    dataset_url: '',
    dataset_description: '',
    overview: '',
    task: '',
    outcomes: '',
    image_1: '',
    image_2: '',
    sample_sol: ''
  });
  
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);
  const [loadingData, setLoadingData] = useState(challengeId !== null);

  // Fetch challenge data if editing an existing challenge
  useEffect(() => {
    if (challengeId && isAdmin) {
      setLoadingData(true);
      fetch(`/api/challenges/${challengeId}`)
        .then(response => {
          if (!response.ok) throw new Error('Failed to fetch challenge');
          return response.json();
        })
        .then(data => {
          setFormData(data);
          setLoadingData(false);
        })
        .catch(err => {
          setError(`Error loading challenge: ${err.message}`);
          setLoadingData(false);
        });
    }
  }, [challengeId, isAdmin]);

  // Handle form input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    setError(null);
    setSuccess(null);

    try {
      const url = challengeId 
        ? `/api/admin/challenges/${challengeId}`
        : '/api/admin/challenges';
      
      const method = challengeId ? 'PUT' : 'POST';
      
      const response = await fetch(url, {
        method,
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify(formData)
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to save challenge');
      }

      const data = await response.json();
      setSuccess(`Challenge ${challengeId ? 'updated' : 'created'} successfully!`);
      
      // Redirect after a brief delay to show success message
      setTimeout(() => {
        router.push('/admin/challenges');
      }, 1500);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  if (loading || !isAdmin) {
    return <div className="max-w-6xl mx-auto px-4 py-8 bg-white">
      <p className="text-black text-center">Loading...</p>
    </div>;
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8 bg-white">
      <h1 className="text-3xl font-bold text-black mb-6">
        {challengeId ? 'Edit Challenge' : 'Create New Challenge'}
      </h1>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {success && (
        <div className="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded mb-4">
          {success}
        </div>
      )}

      {loadingData ? (
        <div className="text-black text-center">Loading challenge data...</div>
      ) : (
        <form onSubmit={handleSubmit} className="space-y-6 text-black">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Basic Info Section */}
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium mb-1" htmlFor="title">
                  Title*
                </label>
                <input
                  type="text"
                  id="title"
                  name="title"
                  value={formData.title}
                  onChange={handleChange}
                  required
                  className="w-full px-3 py-2 border border-gray-300 rounded-md"
                />
              </div>

              <div>
                <label className="block text-sm font-medium mb-1" htmlFor="description">
                  Short Description
                </label>
                <textarea
                  id="description"
                  name="description"
                  value={formData.description || ''}
                  onChange={handleChange}
                  rows={3}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md"
                />
              </div>

              <div>
                <label className="block text-sm font-medium mb-1" htmlFor="difficulty">
                  Difficulty*
                </label>
                <select
                  id="difficulty"
                  name="difficulty"
                  value={formData.difficulty}
                  onChange={handleChange}
                  required
                  className="w-full px-3 py-2 border border-gray-300 rounded-md"
                >
                  <option value="Easy">Easy</option>
                  <option value="Medium">Medium</option>
                  <option value="Hard">Hard</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium mb-1" htmlFor="subcategory">
                  Subcategory*
                </label>
                <input
                  type="text"
                  id="subcategory"
                  name="subcategory"
                  value={formData.subcategory}
                  onChange={handleChange}
                  required
                  placeholder="e.g., Data-Visualization, AI-ML"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md"
                />
              </div>

              <div>
                <label className="block text-sm font-medium mb-1" htmlFor="technology">
                  Technology
                </label>
                <input
                  type="text"
                  id="technology"
                  name="technology"
                  value={formData.technology || ''}
                  onChange={handleChange}
                  placeholder="e.g., Python, R, JavaScript"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md"
                />
              </div>
            </div>

            {/* Dataset Section */}
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium mb-1" htmlFor="dataset_url">
                  Dataset URL
                </label>
                <input
                  type="text"
                  id="dataset_url"
                  name="dataset_url"
                  value={formData.dataset_url || ''}
                  onChange={handleChange}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md"
                />
              </div>

              <div>
                <label className="block text-sm font-medium mb-1" htmlFor="dataset_description">
                  Dataset Description
                </label>
                <textarea
                  id="dataset_description"
                  name="dataset_description"
                  value={formData.dataset_description || ''}
                  onChange={handleChange}
                  rows={3}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md"
                />
              </div>
            </div>
          </div>

          {/* Challenge Details Section */}
          <div className="border-t pt-6 space-y-4">
            <h2 className="text-xl font-semibold">Challenge Details</h2>
            
            <div>
              <label className="block text-sm font-medium mb-1" htmlFor="overview">
                Overview
              </label>
              <textarea
                id="overview"
                name="overview"
                value={formData.overview || ''}
                onChange={handleChange}
                rows={4}
                className="w-full px-3 py-2 border border-gray-300 rounded-md"
              />
            </div>

            <div>
              <label className="block text-sm font-medium mb-1" htmlFor="task">
                Task Description
              </label>
              <textarea
                id="task"
                name="task"
                value={formData.task || ''}
                onChange={handleChange}
                rows={4}
                className="w-full px-3 py-2 border border-gray-300 rounded-md"
              />
            </div>

            <div>
              <label className="block text-sm font-medium mb-1" htmlFor="outcomes">
                Expected Outcomes
              </label>
              <textarea
                id="outcomes"
                name="outcomes"
                value={formData.outcomes || ''}
                onChange={handleChange}
                rows={4}
                className="w-full px-3 py-2 border border-gray-300 rounded-md"
              />
            </div>

            <div>
              <label className="block text-sm font-medium mb-1" htmlFor="sample_sol">
                Sample Solution
              </label>
              <textarea
                id="sample_sol"
                name="sample_sol"
                value={formData.sample_sol || ''}
                onChange={handleChange}
                rows={6}
                className="w-full px-3 py-2 border border-gray-300 rounded-md font-mono text-sm"
              />
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label className="block text-sm font-medium mb-1" htmlFor="image_1">
                  Image URL 1
                </label>
                <input
                  type="text"
                  id="image_1"
                  name="image_1"
                  value={formData.image_1 || ''}
                  onChange={handleChange}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md"
                />
              </div>

              <div>
                <label className="block text-sm font-medium mb-1" htmlFor="image_2">
                  Image URL 2
                </label>
                <input
                  type="text"
                  id="image_2"
                  name="image_2"
                  value={formData.image_2 || ''}
                  onChange={handleChange}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md"
                />
              </div>
            </div>
          </div>

          <div className="flex justify-end space-x-4 pt-4 border-t">
            <button
              type="button"
              onClick={() => router.push('/admin/challenges')}
              className="px-4 py-2 border border-gray-300 rounded-md hover:bg-gray-100"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={isSubmitting}
              className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50"
            >
              {isSubmitting ? 'Saving...' : challengeId ? 'Update Challenge' : 'Create Challenge'}
            </button>
          </div>
        </form>
      )}
    </div>
  );
}
