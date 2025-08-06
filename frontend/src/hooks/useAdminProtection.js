'use client';

import { useLogin } from "@/components/LoginContext";
import { useRouter } from "next/navigation";
import { useEffect } from "react";

export function useAdminProtection() {
  const { user, loading } = useLogin();
  const router = useRouter();

  useEffect(() => {
    if (!loading && (!user || user.userType !== "admin")) {
      router.push("/");
    }
  }, [user, loading, router]);

  return { isAdmin: !loading && user?.userType === "admin", loading };
}
