import React from "react";
import { useAuth } from "../context/AuthContext";
import { Navigate } from "react-router-dom";

export const RequireLogin = ({ children }) => {
  const auth = useAuth();
  if (!auth.user) {
    return <Navigate to="/login" replace={true} />;
  }
  return children;
};
