import React from "react";
import { Breadcrumb } from "@components/Breadcrumb";
import { CardHolder } from "@components/Card/CardHolder";
import { useAuth } from "@context/AuthContext";
import { BsCurrencyDollar } from "react-icons/bs";
import { RiUserReceived2Fill } from "react-icons/ri";
import { useData } from "../hooks/useData";
import { Text, Flex } from "@chakra-ui/react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export const optionsearning = {
  responsive: true,
  scales: {
    y: {
      min: 0,
      ticks: {
        stepSize: 100,
      },
    },
  },
  plugins: {
    legend: {
      position: "top",
    },
    title: {
      display: true,
      text: "Past 4 Days Earnings",
    },
  },
};

export const optionsride = {
  responsive: true,
  scales: {
    y: {
      min: 0,
      ticks: {
        stepSize: 100,
      },
    },
  },
  plugins: {
    legend: {
      position: "top",
    },
    title: {
      display: true,
      text: "Past 4 Days Rides",
    },
  },
};

export const Dashboard = () => {
  const { isLoading, error, data } = useData("dashboard", `api/dashboard`);

  if (isLoading) {
    return (
      <>
        <Breadcrumb />
        <Text mt={6}>Loading</Text>
      </>
    );
  }
  if (error) {
    return (
      <>
        <Breadcrumb />
        <Text mt={6}>No Data Available</Text>
      </>
    );
  }
  const cardData = [
    {
      icon: BsCurrencyDollar,
      title: "Earnings",
      number: `&#8377; ${data?.total_earnings}`,
    },

    {
      icon: RiUserReceived2Fill,
      title: "Rides",
      number: `${data?.total_rides}`,
    },
  ];
  const earnings = {
    labels: Object.values(data.daily_totals).map((item, index) => item.date),
    datasets: [
      {
        label: "Earings",
        data: Object.values(data.daily_totals).map(
          (item, index) => item.total_earnings
        ),
        backgroundColor: ["#D2FF28", "#C84C09", "#5C80BC", "#FF8811"],
      },
    ],
  };
  const rides = {
    labels: Object.values(data.daily_totals).map((item, index) => item.date),
    datasets: [
      {
        label: "Rides",
        data: Object.values(data.daily_totals).map(
          (item, index) => item.total_rides
        ),
        backgroundColor: ["#5C80BC", "#D2FF28", "#C84C09", "#FF8811"],
      },
    ],
  };
  return (
    <>
      <Breadcrumb />
      <Flex overflowY={"scroll"} flexDirection={{ lg: "column", "2xl": "row" }}>
        <CardHolder cardData={cardData} />
        <Flex
          w={700}
          marginLeft={{ base: "0", md: "30px" }}
          alignItems="center"
          justifyContent="center"
          flexDir="column"
          gap="15px"
          bg="white"
          borderRadius="7px"
          boxShadow="0px 4px 4px rgba(0, 0, 0, 0.25)"
          mt={"15px"}
          padding={4}
        >
          <Line options={optionsearning} data={earnings} />
          <Line options={optionsride} data={rides} />
        </Flex>
      </Flex>
    </>
  );
};
