import React from "react";
import { useAuth } from "../context/AuthContext";
import { Navigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

export const RequireLogin = ({ children }) => {
  const auth = useAuth();
  const path = useLocation();
  const admin = path.pathname.includes("admin");
  if (!auth.user) {
    return <Navigate to={admin ? "/admin/login" : "/login"} replace={true} />;
  }
  return children;
};
