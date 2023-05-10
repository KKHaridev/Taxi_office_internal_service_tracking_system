import React from "react";
import { Breadcrumb } from "@components/Breadcrumb";
import { CardHolder } from "@components/Card/CardHolder";
import { useAuth } from "@context/AuthContext";

export const Dashboard = () => {
  const auth = useAuth();
  const cardData = [
    {
      title: "Earnings",
      number: `&#8377; ${auth?.user.earnings.total_earnings}`,
    },

    {
      title: "Rides",
      number: auth?.user.total_rides,
    },
  ];
  return (
    <>
      <Breadcrumb />
      <CardHolder cardData={cardData} />
    </>
  );
};
