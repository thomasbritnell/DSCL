/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'http://backend:5000/api/:path*', // Use localhost for Azure multi-container
      },
    ];
  },
};

export default nextConfig;
