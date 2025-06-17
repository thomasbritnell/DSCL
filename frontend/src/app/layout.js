// frontend/src/app/layout.js

import "../app/globals.css"; // ← imports Tailwind (and any other global CSS)
import React from "react";

export const metadata = {
  title: "Data Science Challenge Library",
  description: "Browse DS challenges by difficulty & subcategory",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        {/* You can put additional <link> or <meta> tags here if needed */}
      </head>
      <body className="bg-gray-50 text-gray-900">
        {children}
      </body>
    </html>
  );
}
