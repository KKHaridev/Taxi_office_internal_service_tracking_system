import React from "react";
import { Breadcrumb } from "@components/Breadcrumb";
import { CardHolder } from "@components/Card/CardHolder";
import { useAuth } from "@context/AuthContext";
import { BsCurrencyDollar } from "react-icons/bs";
import { RiUserReceived2Fill } from "react-icons/ri";

export const Dashboard = () => {
  const auth = useAuth();
  const cardData = [
    {
      icon: BsCurrencyDollar,
      title: "Earnings",
      number: `&#8377; ${auth?.user?.user_id}`,
    },

    {
      icon: RiUserReceived2Fill,
      title: "Rides",
      number: auth?.user?.user_id,
    },
  ];
  return (
    <>
      <Breadcrumb />
      <CardHolder cardData={cardData} />
    </>
  );
};
