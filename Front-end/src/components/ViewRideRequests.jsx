import React from "react";
import { Breadcrumb } from "./Breadcrumb";
import { useParams } from "react-router-dom";
import { useData } from "../hooks/useData";

export const ViewRideRequests = () => {
  let { id } = useParams();
  const { isLoading, error, data } = useData(
    "req",
    `req_rides/${id}`,
  );
console.log(data);
  if (isLoading) return "Loading...";

  if (error) return "An error has occurred: " + error.message;
  return (
    <>
      <Breadcrumb />
    </>
  );
};
