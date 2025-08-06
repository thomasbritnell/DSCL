// frontend/src/app/layout.js

import "../app/globals.css"; // Imports Tailwind and global CSS
import React from "react";
import { LoginProvider } from "../components/LoginContext";

/**
 * Metadata for the app (used by Next.js)
 */
export const metadata = {
  title: "Data Science Challenge Library",
  description: "Browse DS challenges by difficulty & subcategory",
};

/**
 * RootLayout wraps all pages in the app, sets up global styles and metadata.
 * @param {Object} props
 * @param {React.ReactNode} props.children - Page content
 * @returns {JSX.Element}
 */
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        {/* Additional <link> or <meta> tags can be added here */}
      </head>
      <body className="bg-gray-50 text-gray-900">
        <LoginProvider>
          {children}
        </LoginProvider>
      </body>
    </html>
  );
}
